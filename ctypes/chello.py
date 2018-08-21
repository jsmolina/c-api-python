import timeit
#from ctypes import cdll, POINTER, c_ulong, cast, pointer, c_int
import ctypes
from timeit import Timer



def fib(array):
   array_size = len(array)
   array = (ctypes.c_ulong * array_size)(*array)
   fib_lib.fib(array_size, array)
   return array


if __name__ == "__main__":
   fib_lib = ctypes.cdll.LoadLibrary("fib.so")

   fib_lib.fib.restype = None
   fib_lib.fib.argtypes = (ctypes.c_int,
                                 ctypes.POINTER(ctypes.c_ulong))

   res = [0] * 50
   print(fib(res)[:])


   array = (ctypes.c_ulonglong * 50)(*res)

   t = Timer(lambda: fib_lib.fib(50, array))
   print(t.timeit())
