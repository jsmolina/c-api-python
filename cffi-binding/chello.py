from timeit import Timer
from cffi import FFI

ffi = FFI()



if __name__ == "__main__":
    with open("hellomodule.h") as header:
        ffi.cdef(header.read())
    lib = ffi.dlopen("fib.so")
    s = lib.fib(47)
    print([s[i] for i in range(47)])

    t = Timer(lambda: lib.fib(47))
    print(t.timeit())
