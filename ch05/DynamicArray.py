# Haowen Huang refreshed on Oct 17, 2019
# Chapter 5: Array-Based Sequences: Implementing a Dynamic Array & 
# 基于数组的序列
# /Users/Algorithms/python/dsa/ch05

## 5.3.1 Implementing a Dynamic Array

import ctypes       # provides low-level arrays

print("\n------ Array-Based Sequences: Implementing a Dynamic Array ------")
class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array
        
    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k):
        if not 0<= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                               # retrieve from array
    
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):                               # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                         # new (bigger) array
        for k in range(self._n):                        # for each existing value
            B[k] = self._A[k]
        self._A = B                                     # use the bigger array
        self._capacity = c
        
    def _make_array(self, c):                           # nopublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()                 # see ctypes documentation

    # Implementation of insert for our DynamicArray class
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # for simplicity, we assume 0<=k<=n in this version
        if self._n == self._capacity:                   # not enough room
            self._resize(2*self._capacity)              # so double capacity
        for j in range(self._n, k, -1):                 # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                              # store newest element
        self._n += 1

    # Removing Elements from a List
    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)"""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:             # found a match!
                for j in range(k, self._n - 1): # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None     # help garbage collection
                self._n -= 1                    # we have one less item
                return                          # exit immediately
        raise ValueError('Value not found')     # only reached if no match


if __name__ == "__main__":
    d = DynamicArray()
    for i in range(10):
        d.append(i)
    print("\n--- Before the insert operation ---")    
    for i in d:
        print(i)
    
    print("\n--- After the insert operation ---")
    d.insert(3, 98)
    for i in d:
        print(i)
    
    print("\n--- After the remove operation ---")
    d.remove(6)
    for i in d:
        print(i)
    
    print("\nd.__len__: ", d.__len__)
    print("\nd.__getitem__: ", d.__getitem__)

# d.__len__:  <bound method DynamicArray.__len__ of <__main__.DynamicArray object at 0x104a63050>>
# d.__getitem__:  <bound method DynamicArray.__getitem__ of <__main__.DynamicArray object at 0x104a63050>>



## 5.3.2 Amortized Analysis of Dynamic Arrays   动态数组的摊销分析

# The strategy of replacing an array with a new, larger aray might at first seem slow, 
# because a single append operation may require  Ω(𝑛)  time to perform, where  𝑛  is the current number of elements in the array. 
# However, notice that by doubling the capacity during an array replacement, 
# our new array allows us to add  𝑛  new elements before the array must be replaced again. 
# 
# In this way, there are many simple append operations for each expensive one. 
# This fact allows us to show that performing a series of operations on an initially empty dynamic array is efficient in terms of its total running time.

# Memory Usage and Shrinking an Array   内存使用和紧凑数组
# Another consequence of the rule of a geometric increase in capacity when appending to a dynamic array is that the final array size is guaranteed to be proportional to the overall number of elements. 
# That is, the data structure uses 𝑂(𝑛) memory. This is a very desirable property for a data structure.
#
# If a container, such as a Python list, provides operations that cause the removal of one or more elements, greater care must be taken to ensure that a dynamic array guarantees 𝑂(𝑛) memory usage. 
# THe risk is that repeated insertions may cause the underlying array to grow arbitrarily large, 
# and that there will no longer be a proportional relationship between the actual number of elements and the array capacity after many elements are removed.
# 
# A robust implementation of such a data structure will shrink the underlying array(紧凑底层数组), 
# on occasion, while maintaining the 𝑂(1) amortized bound on individual operations. 


## 5.3.3 Python’s List Class
# Python is not using a pure geometric progression, nor is it using an arithmetic progression for list class.

# With that said, it is clear that Python's implementation of the append method exhibits amortized constant-time behavior. We can demonstrate this fact experimentally. We can get a more accurate measure of the amortized cost per operation by performing a series of  𝑛  append operations on an initilaly empty list and determining the average cost of each. A function to perform that is given by follow:

from time import time
 
print("\n------ Array-Based Sequences: Python’s List Class ------")

def compute_average(n):
    """Perform n appends to an empty lista nd return average time elapsed."""
    
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

# 需要测试上面类时，打开下面的两行注释
# x = [compute_average(i) for i in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]]
# print("\ncompute_average(i) for i in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]]:\n", x)

# Result:
# compute_average(i) for i in [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]]:
#  [1.5974044799804688e-07, 1.0919570922851563e-07, 1.1401176452636719e-07, 8.613109588623047e-08, 7.65531063079834e-08, 7.582552433013917e-08, 7.52126407623291e-08]

# Technically the time elapsed between the start and end includes the time to manage the iteration for the for loop, in addition to the `append` calls.
# The empirical results of the experiment, for increasingly larger values of n, we see higher average cost for the smaller data sets, 
# perhasps in part due to the overhead of the loop range.
#
# There is also natural variance in measuring the amortized cost in this way, because of the impact of the final resize vent relative to n. Taken as a whole,
# there seems clear evidence that the amortized time for each `append` is independent of n.



## 5.4 Efficiency of Python's Sequence Types    Python序列类型的效率

## 5.4.1 Python's List and Tuple Classes
# Operation	            Running Time
# len(data)	                𝑂(1)
# data[j]	                𝑂(1)
# data.count(value)	        𝑂(𝑛)
# data.index(value)	        𝑂(𝑘+1)
# value in data	            𝑂(𝑘+1)
# data1==data2	            𝑂(𝑘+1)
# data[j:k]	                𝑂(𝑘−𝑗+1)
# data1 + data2	            𝑂(𝑛1+𝑛2)
# c * data	                𝑂(𝑐𝑛)

# The data1 and data2 designate instances of the list or tuple class, and 𝑛1 and 𝑛2 their respective length.  
# 𝑘 represents the index of the left most occurence ofr the containment check.

# Operation	            Running Time
# data[j] = val	            𝑂(1) 
# data.append(value)	    𝑂(1) 
# data.insert(k, value)	    𝑂(𝑛−𝑘+1) 
# data.pop()	            𝑂(1) 
# data.pop(k)	            𝑂(𝑛−𝑘) 
# data.remove(value)	    𝑂(𝑛) 
# data1.extend(data2)	    𝑂(𝑛2) 
# data.reverse()	        𝑂(𝑛) 
# data.sort()	            𝑂(𝑛log𝑛) 



# Adding Elements to a List
# That portion of the work requires Ω(n) worst-case time but only O(1) amortized time, as per append. 
# The other expense for insert is the shifting of elements to make room for the new item. 

print("\n------ Array-Based Sequences: Adding Elements to a List ------")

# Implementation of insert for our DynamicArray class
def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # for simplicity, we assume 0<=k<=n in this version
    if self._n == self._capacity:           # not enough room
        self._resize(2*self._capacity)      # so double capacity
    for j in range(self._n, k, -1):         # shift rightmost first
        self._A[j] = self._A[j-1]
    self._A[k] = value                      # store newest element
    self._n += 1

# if __name__ == "__main__":
#     d = DynamicArray()
#     for i in range(10):
#         d.append(i)
#     d.insert(3, 98)
#     for i in d:
#         print(i)



# Removing Elements from a List
# The parameterized version, pop(k), removes the element that is at index k < n of a list, 
# shifting all subsequent elements leftward to fill the gap that results from the removal. 
# The efficiency of this operation is O(n − k), as the amount of shifting depends upon the choice of index k. 
# 
# Note well that this implies that pop(0) is the most expensive call, using Ω(n) time.

def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)"""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
        if self._A[k] == value:             # found a match!
            for j in range(k, self._n - 1): # shift others to fill gap
                self._A[j] = self._A[j+1]
            self._A[self._n - 1] = None     # help garbage collection
            self._n -= 1                    # we have one less item
            return                          # exit immediately
    raise ValueError('Value not found')     # only reached if no match

# if __name__ == "__main__":
#     d = DynamicArray()
#     for i in range(10):
#         d.append(i)
#     print("\n--- Before the remove operation ---")
#     for i in d:
#         print(i)
    
#     print("\n--- After the remove operation ---")
#     d.remove(6)
#     for i in d:
#         print(i)



## 5.4.2 Python's String Class
# It is recommended to append string by using list comprehension instead of iteratively calling append, 
# which have to increase its length for every iteration and lead to 𝑂(𝑛2).
print("\n------ Array-Based Sequences: Python's String Class ------")

doc = "ABcdefGH12414523632ijklmnopqrstuvwXYZ"

# In this case, generator comprehension is preferred to list comprehension in terms of memory management.
letters = ''.join(c for c in doc if c.isalpha())
print("\n''.join([c for c in doc if c.isalpha()]): \n", letters)
# ''.join([c for c in doc if c.isalpha()]): 
#  ABcdefGHijklmnopqrstuvwXYZ



