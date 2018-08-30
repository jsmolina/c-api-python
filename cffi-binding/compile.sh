#!/bin/sh
gcc -o fib.so -shared -fPIC hellomodule.c
python chello.py
