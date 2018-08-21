%module hello

%{
#include <stdlib.h>
#include "hellomodule.c"
%}


%typemap(out) unsigned long * fib {
  int i;
  size_t  templen = 47;
  $result = PyList_New(templen);
  for (i = 0; i < templen; i++) {
    PyObject *o = PyInt_FromLong((long)$1[i]);
    PyList_SetItem($result,i,o);
  }
}

%include "carrays.i"
%array_class(int, intp);
%include "hellomodule.c"
