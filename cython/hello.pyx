import timeit

def fib(n):
   cdef int first = 0
   cdef int second = 1
   result = []
   cdef int next
   cdef int c
   #print "First %d terms of Fibonacci series are :-" %n;
 
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
   print timeit.timeit("fib(10)", "from __main__ import fib")

