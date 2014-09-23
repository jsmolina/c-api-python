#!/bin/sh
gcc -shared hellomodule.c -framework Python -o hellomodule.so
