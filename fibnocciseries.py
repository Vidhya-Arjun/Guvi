#fibonacci series using lambda function
# Each number = sum of the previous two.
# Formula:
# F(n) = F(n−1) + F(n−2)
fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
print([fib(i) for i in range(10)]) #looping through for looping through n