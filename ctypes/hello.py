import timeit

def fib(n):
   first = 0
   second = 1
   result = []
   #print "First %d terms of Fibonacci series are :-" %n;
 
   for c in xrange(0, n):
      if c <= 1:
         next = c
      else:      
         next = first + second;
         first = second;
         second = next;     
      result.append(next);
   return result;

if __name__ == "__main__":
   print timeit.timeit("fib(100)", "from __main__ import fib")
