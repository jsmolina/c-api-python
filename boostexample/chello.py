import timeit
import boostexample.fib

print("result!")
print(boostexample.fib.fib2(47))

print(timeit.timeit("fib(47)", "from boostexample.fib import fib2"))
