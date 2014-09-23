#!/bin/sh
python setup.py build
cp build/lib.macosx-10.9-intel-2.6/*.so .
python chello.py

