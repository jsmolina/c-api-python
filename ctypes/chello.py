import timeit
from ctypes import cdll, POINTER, c_ulonglong, cast, pointer
#from numpy.ctypeslib import ndpointer
from timeit import Timer

if __name__ == "__main__":
   fib_lib = cdll.LoadLibrary("fib.so")

   fib_lib.fib.restype = c_ulonglong * 100
   result = fib_lib.fib(100)
   print([i for i in result])

   t = Timer(lambda: fib_lib.fib(100))
   print(t.timeit())
