// file_stream.hpp - declaration of IOStream and FileStream objects
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

#ifndef __CPCL_FILE_STREAM_HPP
#define __CPCL_FILE_STREAM_HPP

#include "basic.h"

#ifdef _MSC_VER
#include <io.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <share.h>
#include <stdlib.h>
#include <stdio.h>

inline int open(char const *filename, int oflag, int pmode) {
	int shflag(_SH_DENYNO);
	if (oflag & _O_CREAT)
		shflag = _SH_DENYWR;
	int fd;
	::_sopen_s(&fd, filename, oflag | _O_BINARY, shflag, pmode);
	return fd;
}
inline int close(int fd) {
	return ::_close(fd);
}
typedef int ssize_t;
inline ssize_t read(int fd, void *buffer, unsigned int count) {
	return ::_read(fd, buffer, count);
}
inline ssize_t write(int fd, void const *buffer, unsigned int count) {
	return ::_write(fd, buffer, count);
}
typedef __int64 int64_t;
typedef int64_t off64_t;
inline off64_t lseek64(int fd, off64_t move_to, int move_method) {
	return _lseeki64(fd, move_to, move_method);
}
inline char const* strerror_r(int errnum, char *buffer, size_t numberOfElements) {
	if (strerror_s(buffer, numberOfElements, errnum) && numberOfElements)
		*buffer = 0;
	return buffer;
}
#else
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <cerrno>
#include <cstring> // strerror_r

typedef long long int64_t;
#endif

// #include "io_stream.h"
#include "string_piece.hpp"

namespace cpcl {

class IOStream {
public:
	virtual ~IOStream()
	{}

	virtual bool operator!() const { return false; }
	// virtual IOStream* Clone() = 0; // returns a new stream object with its own seek pointer that references the same bytes as the original stream
	// virtual unsigned long CopyTo(IOStream *output, unsigned long size); // return number of bytes written to output
	virtual unsigned long Read(void *data, unsigned long size) = 0;
	virtual unsigned long Write(void const *data, unsigned long size) = 0;
	virtual bool Seek(int64_t move_to, unsigned long move_method, int64_t *position) = 0;
	virtual int64_t Tell() = 0;
	virtual int64_t Size() = 0;
};

class FileStream : public IOStream {
	bool state;
	int fd;

	FileStream(int fd_);
	FileStream(FileStream const&);
	void operator=(FileStream const&);
public:
	// std::wstring path;

	virtual bool operator !() const { return !state; }
	// WStringPiece Path() const;

	// FileStream(); - for clone ?
	virtual ~FileStream();
	
	// virtual IOStream* Clone();
	virtual unsigned long Read(void *data, unsigned long size);
	virtual unsigned long Write(void const *data, unsigned long size);
	virtual bool Seek(int64_t move_to, unsigned long move_method, int64_t *position);
	virtual int64_t Tell();
	virtual int64_t Size();

	// static std::wstring ExpandPath(cpcl::WStringPiece const &v); // \\\\?\\v
	// static std::string FileStream::ExpandPath(StringPiece const &v)
	// static void ExpandPath(std::wstring *v); // \\\\?\\v

	/*static bool FileStreamCreate(cpcl::WStringPiece const &path,
		unsigned long access_mode, unsigned long share_mode,
		unsigned long disposition, unsigned long attributes,
		FileStream **v);*/
	static bool Create(char const *filepath, FileStream **v);
	// static bool CreateTemporary(FileStream **v);
	static bool Read(char const *filepath, FileStream **v);
	static bool ReadWrite(char const *filepath, FileStream **v);
};

/*inline*/ unsigned long FileStream::Read(void *data, unsigned long size) {
	ssize_t r = read(fd, data, size);
	state = (r != -1);
	if (!state) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::Read(): read fails: " << s << std::endl;
		r = 0;
	}
	return static_cast<unsigned long>(r);
}

/*inline*/ unsigned long FileStream::Write(void const *data, unsigned long size) {
	ssize_t r = write(fd, data, size);
	state = (r != -1);
	if (!state) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::Write(): write fails: " << s << std::endl;
		r = 0;
	}
	return static_cast<unsigned long>(r);
}

/*inline*/ bool FileStream::Seek(int64_t move_to, unsigned long move_method, int64_t *position) {
	off64_t r = lseek64(fd, static_cast<off64_t>(move_to), static_cast<int>(move_method));
	// state = (r != (off_t)-1); - Seek method not change IOStream state, because its returns result
	if ((off64_t)-1 == r) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::Seek(): lseek(move_to = " << static_cast<off64_t>(move_to)
			<< ", move_method = " << static_cast<int>(move_method) << ") fails: "
			<< s << std::endl;
		r = 0;
		return false;
	}

	if (position)
		*position = r;
	return true;
}

/*inline*/ int64_t FileStream::Tell() {
	int64_t r;
	state = Seek(0, SEEK_CUR, &r);
	if (!state)
		r = -1;
	return r;
}

/*inline*/ int64_t FileStream::Size() {
	int64_t r;
	int64_t offset = Tell();
	if (!state)
		return -1;
	state = Seek(0, SEEK_END, &r);
	if (!state)
		return -1;
	state = Seek(offset, SEEK_SET, 0);
	return r;
}

//IOStream* FileStream::Clone() {
//	FileStream *r;
//	/*if (!FileStream::FileStreamCreate(path,
//		GENERIC_READ,
//		FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
//		OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, &r))
//		r = NULL;
//	else
//		r->Seek(Tell(), FILE_BEGIN, NULL); - check can open more that one descriptor to same file with compatible access mode*/
//	return r;
//}

FileStream::FileStream(int fd_) : fd(fd_), state(true)
{}
FileStream::~FileStream() {
	close(fd);
}

bool FileStream::Create(char const *filepath, FileStream **v) {
	int fd = open(filepath, O_CREAT | O_EXCL | O_RDWR, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH);
	if (-1 == fd) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::Create(" << filepath << "): open fails: " << s << std::endl;
		return false;
	}
	if (v)
		*v = new FileStream(fd);
	return true;
}

bool FileStream::Read(char const *filepath, FileStream **v) {
	int fd = open(filepath, O_RDONLY, 0);
	if (-1 == fd) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::Read(" << filepath << "): open fails: " << s << std::endl;
		return false;
	}
	if (v)
		*v = new FileStream(fd);
	return true;
}

bool FileStream::ReadWrite(char const *filepath, FileStream **v) {
	int fd = open(filepath, O_RDWR, 0);
	if (-1 == fd) {
		char buf[0x100];
		char const *s = strerror_r(errno, buf, arraysize(buf));
		std::cerr << "FileStream::ReadWrite(" << filepath << "): open fails: " << s << std::endl;
		return false;
	}
	if (v)
		*v = new FileStream(fd);
	return true;
}

} // namespace cpcl

#endif // __CPCL_FILE_STREAM_HPP
