// iterator_adapter.hpp - template wrappers to create STL compatible iterators
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

#ifndef __CPCL_ITERATOR_ADAPTER_HPP
#define __CPCL_ITERATOR_ADAPTER_HPP

#include <iterator>
#include <stdexcept> // std::runtime_error

namespace cpcl {

// Postincrement and dereference implemented through look-ahead value, and require iterator::value_type must be a model of CopyConstructible.
// i.e.:
// self_type& operator++() { // preincrement
//  if (!i.Next(&this->v))
//   i = 0;
// }
//
// self_type /*void*/ operator++(int) { // postincrement
//  self_type tmp = *this;
//  ++*this; // preincrement and dereference have same precedence and right to left associativity, so first dereference evaluted and self_type& returned and then ++self_type applied 
//  return tmp;
// }
//
// value_type const& operator*() const {
//  return this->v;
// }
//
// so, *it++ is operator++(it, int) { copy_it = copy this; operator++(it); return copy_it } and operator*(copy_it)
// because value_type is CopyConstructible, copy_it own v

// value_type may be a model of DefaultConstructible, but this is not required, so we can use in-place new:
//  unsigned char value_storage[sizeof(value_type)];
//  value_type *value; // look-ahead value
//
// value_type const& operator*() const { // no point - if value_type is not DefaultConstructible, it must be CopyConstructible
//  if (!it)
//   throw std::exception("input_iterator_adapter is not dereferencable");
//  return *value;
// }
//
// void GetValue() {
//  if (value) 
//   value->~value_type();
//  // value_type* Iterator::Next()
//  value_type *v = it->Next();
//  if (!v)
//   it = (Iterator*)0;
//  else
//   value = new (value_storage) value_type(*v);
// }
//
// or
//
// void GetValue() {
//  Iterator &it = *it;
//  if (it != end)
//   value = new (value_storage) (*it);
//  ++it;
// }
// but, because EnumeratorType::Next(value_type*), value_type implicit must be DefaultConstructible

template<class Iterator/*no requirements for Iterator type*/, class Value = typename Iterator::value_type>
struct InputIteratorAdapter : std::iterator<std::input_iterator_tag, Value> {
	typedef InputIteratorAdapter<Iterator, Value> Self;
	Iterator *it;
	Value value; // look-ahead value
	
	InputIteratorAdapter() : it(0)//, value() - for primitive types may left uninitialized because operator*() check it; for user types default ctor is called in any case
	{}
	InputIteratorAdapter(Iterator *it_) : it(it_) {
		GetValue();
	}
	// compiler generated copy constructor and assignment operator is ok

	Value operator*() const {
		if (!it)
			throw std::runtime_error("InputIteratorAdapter is not dereferencable"); // throw std::exception("InputIteratorAdapter is not dereferencable", 0);
		return value;
	}

	bool operator==(Self const &r) const {
		return it == r.it;
	}
	bool operator!=(Self const &r) const {
		return !(*this == r);
	}

	Self& operator++() { // preincrement
		if (!it)
			throw std::runtime_error("InputIteratorAdapter is not incrementable"); // throw std::exception("InputIteratorAdapter is not incrementable", 0);

		GetValue();
		return *this;
	}
	
	Self /*void*/ operator++(int) { // postincrement
		Self tmp = *this; // Iterator pointer && value copy
		++*this;
		return tmp;
	}

private:
	void GetValue() {
		if (!it->Next(&value))
			it = 0;
	}
};

//struct InputIteratorAdapter : std::iterator<std::input_iterator_tag, Value> {
// ...
//protected:
//	void GetValue() {
// ...
//};
//template<class Iterator/*CopyConstructible*/, class Value = typename Iterator::value_type>
//struct InputIteratorCopyAdapter : InputIteratorAdapter<Iterator, Value> {
//	unsigned char it_storage[sizeof(Iterator)];
//
//	InputIteratorCopyAdapter() : InputIteratorAdapter<Iterator, Value>()
//	{}
//	InputIteratorCopyAdapter(Iterator const &r) : InputIteratorAdapter<Iterator, Value>() {
//		it = new (it_storage) Iterator(r); // Iterator -> TrivialIterator -> Assignable -> CopyConstructible
//		// why this-> ? if a base class of the class template depends on a template-parameter, 
//		// the base class scope is not examined during unqualified name lookup
//		this->GetValue();
//	}
//	
//	InputIteratorCopyAdapter(InputIteratorCopyAdapter<Iterator, Value> const &r) : InputIteratorAdapter<Iterator, Value>() {
//		if (r.it)
//			it = new (it_storage) Iterator(*r.it);
//	}
//};
// this implementation work, but we need specialized version of GetValue for copy it_storage

template<class Iterator/*CopyConstructible - assume lightweight copy constructor*/, class Value = typename Iterator::value_type>
struct InputIteratorCopyAdapter : std::iterator<std::input_iterator_tag, Value> {
	typedef InputIteratorCopyAdapter<Iterator, Value> Self;
	unsigned char it_storage[sizeof(Iterator)];
	Iterator *it;
	Value value; // look-ahead value

	InputIteratorCopyAdapter() : it(0)
	{}
	InputIteratorCopyAdapter(Iterator const &r) {
		it = new (it_storage) Iterator(r); // Iterator -> TrivialIterator -> Assignable -> CopyConstructible
		GetValue();
	}
	~InputIteratorCopyAdapter() {
		Release();
	}

	InputIteratorCopyAdapter(Self const &r) : it(0) {
		if (r.it) {
			it = new (it_storage) Iterator(*r.it);
			value = r.value;
		}
	}
	Self& operator=(Self const &r) {
		if (r.it != it) {
			Release();
			if (r.it) {
				it = new (it_storage) Iterator(*r.it);
				value = r.value;
			}
		}
		return *this;
	}
	
	Value operator*() const {
		if (!it)
			throw std::runtime_error("InputIteratorCopyAdapter is not dereferencable");
		return value;
	}

	bool operator==(Self const &r) const {
		return it == r.it;
	}
	bool operator!=(Self const &r) const {
		return !(*this == r);
	}

	Self& operator++() { // preincrement
		if (!it)
			throw std::runtime_error("InputIteratorCopyAdapter is not incrementable");

		GetValue();
		return *this;
	}
	
	Self /*void*/ operator++(int) { // postincrement
		Self tmp = *this; // Iterator object complete copy && value copy
		++*this;
		return tmp;
	}

private:
	void GetValue() {
		if (!it->Next(&value))
			Release();
	}

	void Release() {
		if (it) {
			it->~Iterator();
			it = 0;
		}
	}
};

//template<class ValueType>
//struct ForwardIteratorAdapter : std::iterator<std::forward_iterator_tag, ValueType> {
//	if enumerator is a model of CopyConstructible.
//};

} // namespace cpcl

#endif // __CPCL_ITERATOR_ADAPTER_HPP
