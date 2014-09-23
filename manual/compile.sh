#!/bin/sh
python setup.py build
cd build/lib.macosx-10.9-intel-2.6
python chello.py
cd -
