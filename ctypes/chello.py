import ctypes
from timeit import Timer


def fib(array):
   array_size = len(array)
   array = (ctypes.c_ulong * array_size)(*array)
   fib_lib.fib(array_size, array)
   return array


if __name__ == "__main__":
   SIZE = 47

   fib_lib = ctypes.cdll.LoadLibrary("fib.so")

   fib_lib.fib.restype = None
   fib_lib.fib.argtypes = (ctypes.c_int,
                                 ctypes.POINTER(ctypes.c_ulong))

   res = [0] * SIZE
   print(fib(res)[:])


   array = (ctypes.c_ulonglong * SIZE)(*res)

   t = Timer(lambda: fib_lib.fib(SIZE, array))
   print(t.timeit())
