#include <Python/Python.h>
//#include "hello.c"

static PyObject * fib_wrapper( PyObject *self, PyObject *args ) {
  int input;
  int * result;
  PyObject * ret;
  int i;

  // parse arguments
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }

  // run the actual function
  result = fib(input);

  ret = PyList_New(input);
  for (i = 0; i < input; i++) {
      PyList_Append(ret, PyInt_FromLong(result[i]));
  }
  // build the resulting string into a Python object.
  //ret = PyString_FromString(result);
  free(result);
  return ret;
}

static PyMethodDef HelloMethods[] = {
 { "fib", fib_wrapper, METH_VARARGS, "Calculate fibonacci" },
 { NULL, NULL, 0, NULL }
};

void inithello(void) {
  Py_InitModule("hello", HelloMethods);
};
