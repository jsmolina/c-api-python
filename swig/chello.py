import timeit
import hello

if __name__ == "__main__":
   print(hello.fib(47))
   print(timeit.timeit("fib(47)", "from hello import fib"))
