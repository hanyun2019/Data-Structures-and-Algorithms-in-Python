# Kelvin modified on Sep 19, 2019
#
# An inefficient recursion for computing Fibonacci numbers
# You can see this approach requires incredibly inefficient!
#

def bad_fibonacci(n):
    counter(bad_fibonacci)
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def counter(func):
    func.count += 1

num_called = list()
for i in range(30):
    bad_fibonacci.count = 0
    bad_fibonacci(i)
    num_called.append(bad_fibonacci.count)

if __name__ == '__main__':
    for i in num_called:
        print(i)

    
    

