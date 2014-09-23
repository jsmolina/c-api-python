all:
	swig -python -c++ -o _hello_module.cc hello.i 
	python setup.py build_ext --inplace
clean:
	rm -f _*.so
	rm -f hello.py
