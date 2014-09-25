# Boostexample

An example on how to use Boost.Python in order to write Python extensions in
C++.

## Build the extension

```
$ bin/python setup.py build_ext -i
running build_ext
building 'boostexample.mean' extension
/usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -pipe -Os -fwrapv -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/local/include -I/opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c boostexample/mean.cpp -o build/temp.macosx-10.9-x86_64-2.7/boostexample/mean.o
/usr/bin/clang++ -bundle -undefined dynamic_lookup -L/opt/local/lib -Wl,-headerpad_max_install_names -L/opt/local/lib/db46 build/temp.macosx-10.9-x86_64-2.7/boostexample/mean.o -L/opt/local/lib -lboost_python-mt -o build/lib.macosx-10.9-x86_64-2.7/boostexample/mean.so
copying build/lib.macosx-10.9-x86_64-2.7/boostexample/mean.so -> boostexample
```

## Use the extension

To calculate Fibonacci numbers:

```
>>> import boostexample.fib

>>> %timeit boostexample.fib.fib2(100)
100000 loops, best of 3: 5.1 µs per loop

```

To calculate a mean:

```
$ bin/python
Python 2.7.8 (default, Jul 13 2014, 17:11:32)
[GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import boostexample.mean
>>> mean = boostexample.mean.Mean()
>>> mean.compute([1.0, 2.0])
1.5
```
