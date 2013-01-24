// string_piece.hpp - BasicStringPiece<T> class declaration and definition
// based on base/string_piece.h from Chromium copyright The Chromium Authors
//
// Additional changes are licensed under the same terms as Chromium and
// copyright (c) 2012 Yuri Agafonov. All rights reserved.
//
//// +----------------------------------------------------------------------------
//// |
//// | Copyright (c) 2006-2008 The Chromium Authors. All rights reserved.
//// | Use of this source code is governed by a BSD-style license that can be
//// | found in the LICENSE file.
//// | Copied from strings/stringpiece.h with modifications
//// |
//// | A string-like object that points to a sized piece of memory.
//// |
//// | Functions or methods may use const StringPiece& parameters to accept either
//// | a "const char*" or a "string" value that will be implicitly converted to
//// | a StringPiece.  The implicit conversion means that it is often appropriate
//// | to include this .h file in other files rather than forward-declaring
//// | StringPiece as would be appropriate for most other Google classes.
//// |
//// | Systematic usage of StringPiece is encouraged as it will reduce unnecessary
//// | conversions from "const char*" to "string" and back again.
//// +----------------------------------------------------------------------------

#ifndef __CPCL_STRING_PIECE_HPP_
#define __CPCL_STRING_PIECE_HPP_

#include <iosfwd> // char_traits
#include <string>

namespace cpcl {

template<class Char>
struct empty_string {
	static Char const* value() { return (Char const*)NULL; }
};
template<>
struct empty_string<char> {
	static char const* value() { return ""; }
};
template<>
struct empty_string<wchar_t> {
	static wchar_t const* value() { return L""; }
};

template<class Char, class Traits = std::char_traits<Char> >
class BasicStringPiece {
 public:
  typedef size_t size_type;
	// replace BasicStringPiece<Char, Traits> with SelfType ??? typedef BasicStringPiece<Char, Traits> SelfType;

 private:
  Char const *ptr_;
  size_type   length_;

 public:
  BasicStringPiece() : ptr_(NULL), length_(0) {}
  BasicStringPiece(Char const *str)
    : ptr_(str), length_((str == NULL) ? 0 : Traits::length(str)) {}
	/*BasicStringPiece(std::basic_string<Char> const &str)*/
	template<class StringCharTraits, class Allocator>
	BasicStringPiece(std::basic_string<Char, StringCharTraits, Allocator> const &str)
    : ptr_(str.data()), length_(str.size()) {}
  BasicStringPiece(Char const *offset, size_type len)
    : ptr_(offset), length_(len) {}

  // data() may return a pointer to a buffer with embedded NULs, and the
  // returned buffer may or may not be null terminated.  Therefore it is
  // typically a mistake to pass data() to a routine that expects a NUL
  // terminated string.
  Char const* data() const { return ptr_; }
  size_type size() const { return length_; }
  size_type length() const { return length_; }
  bool empty() const { return length_ == 0; }

  void clear() {
    ptr_ = NULL;
    length_ = 0;
  }
  void set(Char const *data, size_type len) {
    ptr_ = data;
    length_ = len;
  }
  void set(Char const *str) {
    ptr_ = str;
    length_ = str ? Traits::length(str) : 0;
  }
  void set(void const *data, size_type len) {
    ptr_ = reinterpret_cast<Char const*>(data);
    length_ = len;
  }

  Char operator[](size_type i) const { return ptr_[i]; }

  void remove_prefix(size_type n) {
		n = n < length_ ? n : length_; // (std::min)(n, length_); - std::min use _DEBUG_LT check for strict weak ordering: (a < b) -> b >= a -> !(b < a)
		// i.e. operator<(T const&, T const&) valid if and only if for any T a,b: (a < b && b < a) == false
    ptr_ += n;
    length_ -= n;
  }
  void remove_suffix(size_type n) {
    length_ -= n < length_ ? n : length_; // (std::min)(n, length_);
  }

  int compare(BasicStringPiece<Char, Traits> const &x) const {
    int r = Traits::compare(ptr_, x.ptr_, (std::min)(length_, x.length_));
    if (r == 0) {
      if (length_ < x.length_) r = -1;
      else if (length_ > x.length_) r = +1;
    }
    return r;
  }

	/*std::basic_string<Char, std::char_traits<Char> > as_string() const {*/
	std::basic_string<Char> as_string() const {
    // std::string doesn't like to take a NULL pointer even with a 0 size.
		return std::basic_string<Char>(!empty() ? data() : empty_string<Char>::value(), size());
  }

  // Does "this" start with "x"
  bool starts_with(BasicStringPiece<Char, Traits> const &x) const {
    return ((length_ >= x.length_) &&
            (Traits::compare(ptr_, x.ptr_, x.length_) == 0));
  }

  // Does "this" end with "x"
  bool ends_with(BasicStringPiece<Char, Traits> const &x) const {
    return ((length_ >= x.length_) &&
            (Traits::compare(ptr_ + (length_ - x.length_), x.ptr_, x.length_) == 0));
  }

  // standard STL container boilerplate
  typedef Char value_type;
  typedef const Char* pointer;
  typedef const Char& reference;
  typedef const Char& const_reference;
  typedef ptrdiff_t difference_type;
  static const size_type npos;
  typedef const Char* const_iterator;
  typedef const Char* iterator;
  typedef std::reverse_iterator<const_iterator> const_reverse_iterator;
  typedef std::reverse_iterator<iterator> reverse_iterator;
  iterator begin() const { return ptr_; }
  iterator end() const { return ptr_ + length_; }
  const_reverse_iterator rbegin() const {
    return const_reverse_iterator(ptr_ + length_);
  }
  const_reverse_iterator rend() const {
    return const_reverse_iterator(ptr_);
  }

  size_type max_size() const { return length_; }
  size_type capacity() const { return length_; }

	BasicStringPiece<Char, Traits> substr(size_type pos, size_type n = (size_type)(-1)/*npos*/) const {
		if (pos > size())
			pos = size();
		if (n > size() - pos)
			n = size() - pos;
		return BasicStringPiece<Char, Traits>(data() + pos, n);
	}

	BasicStringPiece<Char, Traits> trim(BasicStringPiece<Char, Traits> const &chars) const {
		size_type n = chars.size();
		if (0 == n)
			return *this;

		Char const *head(data()), *tail(data() + size()), *trim_chars(chars.data());
		while ((head != tail) && (Traits::find(trim_chars, n, *head)))
			++head;
		while (head != tail) {
			if (Traits::find(trim_chars, n, *(tail - 1)))
				--tail;
			else
				break;
		}

		return BasicStringPiece<Char, Traits>(head, tail - head);
	}
	BasicStringPiece<Char, Traits> trim_head(BasicStringPiece<Char, Traits> const &chars) const {
		size_type n = chars.size();
		if (0 == n)
			return *this;

		Char const *head(data()), *tail(data() + size()), *trim_chars(chars.data());
		while ((head != tail) && (Traits::find(trim_chars, n, *head)))
			++head;

		return BasicStringPiece<Char, Traits>(head, tail - head);
	}
	BasicStringPiece<Char, Traits> trim_tail(BasicStringPiece<Char, Traits> const &chars) const {
		size_type n = chars.size();
		if (0 == n)
			return *this;

		Char const *head(data()), *tail(data() + size()), *trim_chars(chars.data());
		while (head != tail) {
			if (Traits::find(trim_chars, n, *(tail - 1)))
				--tail;
			else
				break;
		}

		return BasicStringPiece<Char, Traits>(head, tail - head);
	}
};

/* static const _Elem * find(const _Elem *_First, size_t _Count, const _Elem& _Ch) */

template<class Char, class Traits>
inline bool operator==(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  if (x.size() != y.size())
    return false;

  return Traits::compare(x.data(), y.data(), x.size()) == 0;
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator==(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return x == BasicStringPiece<Char, Traits>(y);
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator==(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return BasicStringPiece<Char, Traits>(x) == y;
}
template<class Char, class Traits>
inline bool operator==(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return x == BasicStringPiece<Char, Traits>(y);
}
template<class Char, class Traits>
inline bool operator==(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return BasicStringPiece<Char, Traits>(x) == y;
}

template<class Char, class Traits>
inline bool operator!=(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  return !(x == y);
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator!=(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return !(x == BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator!=(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) == y);
}
template<class Char, class Traits>
inline bool operator!=(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return !(x == BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits>
inline bool operator!=(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) == y);
}

template<class Char, class Traits>
inline bool operator<(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  int const r = Traits::compare(x.data(), y.data(), (std::min)(x.size(), y.size()));
  return ((r < 0) || ((r == 0) && (x.size() < y.size())));
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator<(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return x < BasicStringPiece<Char, Traits>(y);
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator<(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return BasicStringPiece<Char, Traits>(x) < y;
}
template<class Char, class Traits>
inline bool operator<(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return x < BasicStringPiece<Char, Traits>(y);
}
template<class Char, class Traits>
inline bool operator<(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return BasicStringPiece<Char, Traits>(x) < y;
}

template<class Char, class Traits>
inline bool operator>(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  return y < x;
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator>(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return BasicStringPiece<Char, Traits>(y) < x;
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator>(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return y < BasicStringPiece<Char, Traits>(x);
}
template<class Char, class Traits>
inline bool operator>(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return BasicStringPiece<Char, Traits>(y) < x;
}
template<class Char, class Traits>
inline bool operator>(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return y < BasicStringPiece<Char, Traits>(x);
}

template<class Char, class Traits>
inline bool operator<=(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  return !(x > y);
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator<=(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return !(x > BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator<=(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) > y);
}
template<class Char, class Traits>
inline bool operator<=(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return !(x > BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits>
inline bool operator<=(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) > y);
}

template<class Char, class Traits>
inline bool operator>=(BasicStringPiece<Char, Traits> const &x, BasicStringPiece<Char, Traits> const &y) {
  return !(x < y);
}

template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator>=(BasicStringPiece<Char, Traits> const &x, std::basic_string<Char, StringCharTraits, Allocator> const &y) {
	return !(x < BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits, class StringCharTraits, class Allocator>
inline bool operator>=(std::basic_string<Char, StringCharTraits, Allocator> const &x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) < y);
}
template<class Char, class Traits>
inline bool operator>=(BasicStringPiece<Char, Traits> const &x, Char const *y) {
	return !(x < BasicStringPiece<Char, Traits>(y));
}
template<class Char, class Traits>
inline bool operator>=(Char const *x, BasicStringPiece<Char, Traits> const &y) {
	return !(BasicStringPiece<Char, Traits>(x) < y);
}

template<class Char, class Traits, class StreamCharTraits>
inline std::basic_ostream<Char, StreamCharTraits>& operator<<(std::basic_ostream<Char, StreamCharTraits> &output, BasicStringPiece<Char, Traits> const &piece) {
	output.write(piece.data(), static_cast<std::streamsize>(piece.size()));
	return output;
}

typedef BasicStringPiece<char, std::char_traits<char> >
	StringPiece;
typedef BasicStringPiece<wchar_t, std::char_traits<wchar_t> >
	WStringPiece;

/* require code correction/refactoring, profit/probable net output is not apparent
template<class Char, size_t N>
inline BasicStringPiece<Char> StringPieceFromLiteral(Char const (&s)[N]) {
	return BasicStringPiece<Char>(s, N - 1);
} */

template<size_t N>
inline StringPiece StringPieceFromLiteral(char const (&s)[N]) {
	return StringPiece(s, N - 1);
}
template<size_t N>
inline WStringPiece WStringPieceFromLiteral(wchar_t const (&s)[N]) {
	return WStringPiece(s, N - 1);
}

}  // namespace cpcl

#endif  // __CPCL_STRING_PIECE_HPP_
