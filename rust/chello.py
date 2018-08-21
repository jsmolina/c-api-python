import timeit
from rust_fib import fib

print("result!")
print(fib(47))

print(timeit.timeit("fib(47)", "from rust_fib import fib"))
