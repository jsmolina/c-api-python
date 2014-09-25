from setuptools import setup, Extension


BOOST_INCLUDE = '/opt/local/include'
BOOST_LIBRARIES = '/opt/local/lib'
# os.environ['ARCHFLAGS'] = "-arch x86_64"

mean_ext = Extension(
    'boostexample.mean',
    sources=['boostexample/mean.cpp'],
    include_dirs=[BOOST_INCLUDE],
    libraries=['boost_python-mt'],
    library_dirs=[BOOST_LIBRARIES])

fib_ext = Extension(
    'boostexample.fib',
    sources=['boostexample/fib.cpp'],
    include_dirs=[BOOST_INCLUDE],
    library_dirs=[BOOST_LIBRARIES],
    libraries=['boost_python-mt'])


setup(name='boostexample',
      version='0.0.1',
      packages=['boostexample'],
      ext_modules=[mean_ext, fib_ext])
