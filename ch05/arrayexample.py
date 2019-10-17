# Kelvin modified on Oct 17, 2019
# Chapter 5: Array-Based Sequences
# 基于数组的序列
# /Users/Algorithms/python/kelvin-practice/ch05

## 5.1 Python’s Sequence Types
# Python’s various “sequence” classes, namely the built-in list(列表类), tuple(元组类), and str classes(字符串类).
# 

## 5.2 Low-Level Arrays

import array
import sys
x = [1, 3, 5, 7, 9]
print(sys.getsizeof(x))
y = array.array('i', [1, 2, 3, 4, 5])
print(sys.getsizeof(y))


