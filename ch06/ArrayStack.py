# Haowen Huang refreshed on Nov 22, 2019
# Chapter 06: Stacks, Queues, and Deques
# /Users/Algorithms/python/dsa/ch06

# 6.1.2 Simple Array-Based Stack Implementation
# The list class already supports adding an element to the end with append method, and removing the last element with the pop method, 
# so it is natural to align the top of the stack at the end of the list.

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    
    def __init__(self):
        """Create an empty stack."""
        self._data = []                     # nonpublic list instance
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                # new item stored at the end of list
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack. 
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]               # the last item in the list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()             # remove last item from list


if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print("\nlen(S): \n", len(S))
    print("\nS.pop(): \n", S.pop())
    print("\nS.is_empty(): \n", S.is_empty())
    print("\nS.pop(): \n", S.pop())
    print("\nS.is_empty(): \n", S.is_empty())
    