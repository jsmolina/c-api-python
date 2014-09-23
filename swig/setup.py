from distutils.core import setup, Extension

extension_mod = Extension("_hello", ["_hello_module.cc", "hellomodule.c"])

setup(name = "hello", ext_modules=[extension_mod])
