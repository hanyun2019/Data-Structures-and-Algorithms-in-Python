# Kelvin modified on Oct 17, 2019
# Chapter 5: Array-Based Sequences: Implementing a Dynamic Array
# 基于数组的序列
# /Users/Algorithms/python/kelvin-practice/ch05

## 5.3.1 Implementing a Dynamic Array

import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    
    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k):
        if not 0<= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


