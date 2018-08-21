#!/bin/sh
swig -python -c++ -o _hello_module.cc hello.i
python setup.py build_ext --inplace
python chello.py
