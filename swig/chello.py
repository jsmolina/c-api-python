import timeit
import hello

if __name__ == "__main__":
   print timeit.timeit("fib(100)", "from hello import fib")
