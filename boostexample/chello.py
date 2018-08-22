import timeit
import boostexample.fib

print("result!")
print(boostexample.fib.fib2(47))

print(timeit.timeit("boostexample.fib.fib2(47)", "import boostexample"))
