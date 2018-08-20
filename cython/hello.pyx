import timeit
from cpython cimport array


def fib(n):
   cdef int first = 0
   cdef int second = 1
   cdef array.array result = array.array('Q', [])
   cdef int next
   cdef int c

   array.resize(result, n)

   for c in range(0, n):
      if c <= 1:
         next = c
      else:
         next = first + second
         first = second
         second = next
      result.data.as_longs[c] = next
   return result

if __name__ == "__main__":
   print timeit.timeit("fib(10)", "from __main__ import fib")
