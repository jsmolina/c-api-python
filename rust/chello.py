import timeit
from rust_fib import fib

print("result!")
print(fib(50))

print(timeit.timeit("fib(50)", "from rust_fib import fib"))
