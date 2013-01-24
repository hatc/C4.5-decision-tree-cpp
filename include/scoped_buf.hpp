// scoped_buf.hpp - `greedy` buffer for storage within the current scope
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

#ifndef __CPCL_SCOPED_BUF_HPP
#define __CPCL_SCOPED_BUF_HPP

#include <stddef.h>
#include <algorithm>
// #include "dumbassert.h"

namespace cpcl {

template<class T, size_t Count>
struct ScopedBuf {
	template<class U, size_t N> friend struct ScopedBuf;

	ScopedBuf() : p_capacity(Count), p_size(0), p(NULL), p_owner(true) {}
	~ScopedBuf() { Release(); }

	T* Alloc(size_t v) {
		if (p_capacity < v) {
			Release();
			if (v > Count) {
				p = new T[v];
				p_capacity = v;
		 }
		}
		p_size = v;
		return Data();
	}
	void Attach(T *p_, size_t p_size_) {
		Release();
		p = p_;
		p_capacity = p_size = p_size_;
		p_owner = false;
	}
	void Release() {
		if ((p) && p_owner) {
			delete [] p;
			//p_capacity = Count;
		}
		p = NULL;
		p_capacity = Count;
		p_size = 0;
		p_owner = true;
	}
	T* Data() {
		// DUMBASS_CHECK_EXPLANATION(p_size, "ScopedBuf::Data(): buffer is empty");
		return (p) ? p : buf;
	}
	size_t Size() const { return p_size; }

	//// template<N> - memcpy(tmp, buf, Count); memcpy(buf, r.buf, !!!N);
	//void swap(ScopedBuf<T, Count> &r) {
	//	// T tmp[max(Count, N)];
	//	T tmp[Count];
	//	memcpy(tmp, buf, Count); memcpy(buf, r.buf, Count); memcpy(r.buf, tmp, Count);
	//	std::swap(p, r.p);
	//	std::swap(p_owner, r.p_owner);
	//	std::swap(p_size, r.p_size);
	//	std::swap(p_capacity, r.p_capacity);
	//}
	template<size_t N>
	void swap(ScopedBuf<T, N> &r) {
		/*unsigned char tmp[N < Count ? N : Count];
		memcpy(tmp, buf, sizeof(tmp));
		memcpy(buf, r.buf, sizeof(tmp));
		memcpy(r.buf, tmp, sizeof(tmp));*/
		// DUMBASS_CHECK_EXPLANATION((p || !p_size) && (r.p || !r.p_size), "can't swap static buffer"); // if (!p && p_size) || (!r.p && r.p_size) assert(False)
		std::swap(p, r.p);
		std::swap(p_owner, r.p_owner);
		std::swap(p_size, r.p_size);
		std::swap(p_capacity, r.p_capacity);
	}

private:
	T buf[Count];
	T *p;
	bool p_owner;
	size_t p_size;
	size_t p_capacity;

	ScopedBuf(ScopedBuf<T, Count> const&);
	void operator=(ScopedBuf<T, Count> const&);
};

template<class T>
struct ScopedBuf<T, 0> {
	template<class U, size_t N> friend struct ScopedBuf;

	ScopedBuf() : p_capacity(0), p_size(0), p(NULL), p_owner(true) {}
	~ScopedBuf() { Release(); }

	T* Alloc(size_t v) {
		if (p_capacity < v) {
			Release();
			p = new T[v];
			p_capacity = v;
		}
		p_size = v;
		return Data();
	}
	void Attach(T *p_, size_t p_size_) {
		Release();
		p = p_;
		p_capacity = p_size = p_size_;
		p_owner = false;
	}
	void Release() {
		if ((p) && p_owner) {
			delete [] p;
		}
		p = NULL;
		p_capacity = p_size = 0;
		p_owner = true;
	}
	T* Data() const {
		// DUMBASS_CHECK_EXPLANATION(p_size, "ScopedBuf::Data(): buffer is empty");
		return p;
	}
	size_t Size() const { return p_size; }

	//void swap(ScopedBuf<T, 0> &r) {
	//	std::swap(p, r.p);
	//	std::swap(p_owner, r.p_owner);
	//	std::swap(p_size, r.p_size);
	//	std::swap(p_capacity, r.p_capacity);
	//}
	template<size_t N>
	void swap(ScopedBuf<T, N> &r) {
		// DUMBASS_CHECK_EXPLANATION(r.p || !r.p_size, "can't swap static buffer"); // if (!r.p && r.p_size) assert(False)
		std::swap(p, r.p);
		std::swap(p_owner, r.p_owner);
		std::swap(p_size, r.p_size);
		std::swap(p_capacity, r.p_capacity);
	}

private:
	T *p;
	bool p_owner;
	size_t p_size;
	size_t p_capacity;

	ScopedBuf(ScopedBuf<T, 0> const&);
	void operator=(ScopedBuf<T, 0> const&);
};

template<class T, size_t N, size_t K>
inline void swap(ScopedBuf<T, N> &l, ScopedBuf<T, K> &r) {
	l.swap(r);
}

} // namespace cpcl

/*namespace std {
template<class T, size_t N, size_t K>
inline void swap(cpcl::ScopedBuf<T, N> &l, cpcl::ScopedBuf<T, K> &r) {
	l.swap(r);
}
}*/

#endif // __CPCL_SCOPED_BUF_HPP
