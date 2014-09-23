import timeit
from ctypes import cdll, POINTER, c_int, cast
from numpy.ctypeslib import ndpointer
from timeit import Timer

if __name__ == "__main__":
   fib_lib = cdll.LoadLibrary("fib.so")
   fib_lib.fib.restype = ndpointer(dtype=c_int, shape=(100,))
   t = Timer(lambda: fib_lib.fib(100))
   print t.timeit()
