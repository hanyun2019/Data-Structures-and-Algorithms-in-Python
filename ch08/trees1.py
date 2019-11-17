# Haowen Huang refreshed on Nov 17, 2019
# Chapter 8: Trees
# 树
# /Users/Algorithms/python/dsa/ch08

# 8.1 General Trees 
# Two nodes that are children of the same parent are siblings. A node v is external if v has no children. 
# A node v is internal if it has one or more children. External nodes are also known as leaves.

# The Tree ADT (Abstract Data Type) 

# A Tree Abstract Base Class in Python
# In discussing the object-oriented design principle of abstraction in Section 2.1.2, 
# we noted that a public interface for an abstract data type is often managed in Python via duck typing. 

# 8.2 Binary Trees
# A binary tree is an ordered tree with the following properties:
# 1. Every node has at most two children.
# 2. Each child node is labeled as being either a left child or a right child. 
# 3. A left child precedes a right child in the order of children of a node.

# The subtree rooted at a left or right child of an internal node v is called a left subtree or right subtree, respectively, of v. 
# A binary tree is proper if each node has either zero or two children. Some people also refer to such trees as being full binary trees. 
# Thus, in a proper binary tree, every internal node has exactly two children. A binary tree that is not proper is improper.

# A Recursive Binary Tree Definition
# Incidentally, we can also define a binary tree in a recursive way such that a binary tree is either empty or consists of:
# • A node r, called the root of T , that stores an element
# • A binary tree (possibly empty), called the left subtree of T 
# • A binary tree (possibly empty), called the right subtree of T

