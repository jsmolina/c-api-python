import timeit
from numba import jit


@jit(nopython=True, cache=True)
def fib(n):
   first = 0
   second = 1
   result = []

   for c in range(0, n):
      if c <= 1:
         next = c
      else:      
         next = first + second
         first = second
         second = next
      result.append(next)
   return result

if __name__ == "__main__":
   r = fib(47)
   print('length {}'.format(len(r)))
   print('result={}'.format(r))

   print(timeit.timeit("fib(47)", "from __main__ import fib"))

