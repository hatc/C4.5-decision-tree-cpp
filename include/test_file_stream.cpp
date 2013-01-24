// Copyright (C) 2012-2013 Yuri Agafonov
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 
// 1. Redistributions of source code must retain the above copyright notice, this
// list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
// this list of conditions and the following disclaimer in the documentation
// and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
// ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
// SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#include "stdafx.h"

#include <stdlib.h>
#include <ctime>
#include <list>
#include <vector>
#include <memory>
#include <algorithm>
#include <iostream>
// #include <cassert>

#include <scoped_buf.hpp>
// #include <memory_stream.h>
#include <file_stream.hpp>

// #include <timer.h>
inline unsigned int TimedSeed() {
	time_t t;
	return static_cast<unsigned int>(::time(&t));
}

namespace cpcl {

inline void dumbassert(char const *s, char const *file, unsigned int line) {
	std::cout << "epic fail: " << s << " at " << file << ":" << line << std::endl;
	throw std::exception();
}

}

#define assert(Expr) (void)((!!(Expr)) || (cpcl::assert(#Expr, __FILE__, __LINE__),0))

/*FileStream
Read():
 precondition: size > 0, file pointer at EOF
 postcondition: state = true, Read() return 0

 precondition: size > 0, file pointer beyond EOF
 postcondition: state = true, Read() return 0

Write():
 precondition: file opened with read-only access
 postcondition: state = false, Write() return 0

 precondition: size > 0, file pointer beyond EOF
 postcondition: state = true, Write() return number of bytes written, intervening bytes(between EOF and file pointer before Write() called) in file uninitialized

Seek():
 precondition: file pointer valid, move_to beyond EOF
 postcondition: state = true, file pointer beyond EOF, return true

 precondition: file pointer valid, move_to before begin of file, i.e. move_to < 0 && SEEK_SET
 postcondition: state = true, file pointer unchanged, return false
*/

typedef std::vector<int> DataChunk;
typedef std::list<DataChunk> DataChunks;
inline void test_read_stream(cpcl::IOStream *input, DataChunks &data_chunks) {
	// assert(!data_chunks.empty());
	cpcl::ScopedBuf<int, 0> buf;
	for (DataChunks::const_iterator i = data_chunks.begin(), tail = data_chunks.end(); i != tail; ++i) {
		size_t n = i->size() * sizeof(*i->begin());
		assert(input->Read(buf.Alloc(n), n) == n);
		assert(memcmp(buf.Data(), &*i->begin(), n) == 0);
	}
	size_t i(0), n = std::max(1, rand() % data_chunks.size());
	assert(input->Seek(0, SEEK_SET, 0));
	size_t offset(0);
	for (; i < n; ++i) {
		DataChunk &data_chunk = data_chunks[i];
		size_t offset_ = data_chunk.size() * sizeof(*data_chunk.begin());
		assert(input->Seek(offset_, SEEK_CUR, 0));
		offset += offset_;
	}
	DataChunk &data_chunk = data_chunks[i];
	n = data_chunk.size() * sizeof(*data_chunk.begin());

	assert(input->Read(buf.Alloc(n), n) == n);
	assert(memcmp(buf.Data(), &*data_chunk.begin(), n) == 0);

	assert(input->Seek(offset, SEEK_SET, 0));
	assert(input->Read(buf.Alloc(n), n) == n);
	assert(memcmp(buf.Data(), &*data_chunk.begin(), n) == 0);
}
inline void test_write_stream(cpcl::IOStream *output, size_t output_size_cap, DataChunks &data_chunks) {
	assert(data_chunks.empty()); // test_write_stream supposed to create random data_chunks
	output_size_cap /= 4; // sizeof(DataChunk::value_type) == sizeof(int)
	assert(output_size_cap > 0);
	size_t d = std::max(output_size_cap / 0x100, size_t(0x100));
	if (output_size_cap > 0x100)
		output_size_cap -= rand() % d;
	while (!!output_size_cap) {
		size_t n = std::min(0x100 + (rand() % d), output_size_cap);
		output_size_cap -= n;
		
		data_chunks.push_back(DataChunk());
		DataChunk &data_chunk = data_chunks.back();
		data_chunk.reserve(n);
		std::generate_n(std::back_inserter(data_chunk), data_chunk.capacity(), rand);
	}

	for (DataChunks::const_iterator i = data_chunks.begin(), tail = data_chunks.end(); i != tail; ++i) {
		size_t n = i->size() * sizeof(*i->begin());
		assert(output->Write(&*i->begin(), n) == n);
	}
}

void test_file_stream(wchar_t const *file_path) {
	srand(time(0));
	typedef std::vector<int> DataChunk;
	typedef std::list<DataChunk> DataChunks;
	DataChunks data_chunks;

	{
	cpcl::FileStream *output_;
	assert(cpcl::FileStream::Create(file_path, &output_));
	std::auto_ptr<cpcl::FileStream> output(output_);
	
	for (size_t i = 0, n = 0x100 + rand() % 0x100; i < n; ++i) {
		data_chunks.push_back(DataChunk());
		DataChunk &data_chunk = data_chunks.back();
		data_chunk.reserve(0x1000 + rand() % 0x1000);
		std::generate_n(std::back_inserter(data_chunk), data_chunk.capacity(), rand);
	}

	for (DataChunks::const_iterator i = data_chunks.begin(), tail = data_chunks.end(); i != tail; ++i) {
		size_t n = i->size() * sizeof(*i->begin()); // *i->size() * sizeof(*i->begin());
		assert(output->Write(&*i->begin(), n) == n);
	}
	}

	{
	cpcl::FileStream *input_;
	assert(cpcl::FileStream::Read(file_path, &input_));
	std::auto_ptr<cpcl::FileStream> input(input_);
	cpcl::FileStream *unused_;
	assert(cpcl::FileStream::Read(file_path, &unused_)); // check handle share work
	std::auto_ptr<cpcl::FileStream> unused(unused_);

	cpcl::ScopedBuf<int, 0> buf;
	for (DataChunks::const_iterator i = data_chunks.begin(), tail = data_chunks.end(); i != tail; ++i) {
		size_t n = i->size() * sizeof(*i->begin());
		assert(input->Read(buf.Alloc(n), n) == n);
		assert(memcmp(buf.Data(), &*i->begin(), n) == 0);
	}
	}
}

void test_file_stream_() {
	// test_file_stream(L"C:\\tmp00\\del\\antlr3-java-weka-parser\\test.dat");
	srand(TimedSeed());
	DataChunks data_chunks;

	cpcl::ScopedBuf<unsigned char, 0> buf;
	buf.Alloc(0x1000 * 0x100);
	cpcl::MemoryStream stream(buf.Data(), buf.Size());
	
	test_write_stream(&stream, buf.Size(), data_chunks);
	stream.Seek(0, SEEK_SET, 0);
	test_read_stream(&stream, data_chunks);
	
	/*wchar_t const *file_path = L"C:\\tmp00\\del\\antlr3-java-weka-parser\\test.dat";
	{
		cpcl::FileStream *output_;
		assert(cpcl::FileStream::Create(file_path, &output_));
		std::auto_ptr<cpcl::FileStream> output(output_);

		test_write_stream(output.get(), 0x1000 * 0x400, data_chunks);
	}
	{
		cpcl::FileStream *input_;
		assert(cpcl::FileStream::Read(file_path, &input_));
		std::auto_ptr<cpcl::FileStream> input(input_);
		cpcl::FileStream *unused_;
		assert(cpcl::FileStream::Read(file_path, &unused_)); // check handle share work
		std::auto_ptr<cpcl::FileStream> unused(unused_);

		test_read_stream(input.get(), data_chunks);
	}*/
}
