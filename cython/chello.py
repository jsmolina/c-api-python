import timeit
import hello

if __name__ == "__main__":
   r = hello.fib(47)
   print(f'length {len(r)}')
   print(f'result={r}')
   print(timeit.timeit("fib(47)", "from hello import fib"))
