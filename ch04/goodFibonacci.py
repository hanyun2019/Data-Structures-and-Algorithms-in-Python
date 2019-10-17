# Kelvin modified on Sep 19, 2019
#
# An Efficient Recursion for Computing Fibonacci Numbers
# We can compute Fibonacci much more efficiently using a recursion 
# in which each invocation makes only one recursive call. 
#

def good_fibonacci(n):
    counter(good_fibonacci)
    if n<= 1:
        return n, 0
    else:
        (a, b) = good_fibonacci(n-1)
        return a+b, a

def counter(func):
    func.count += 1

num_called = list()
for i in range(30):
    good_fibonacci.count = 0
    good_fibonacci(i)
    num_called.append(good_fibonacci.count)

if __name__ == '__main__':
    for i in num_called:
        print(i)
