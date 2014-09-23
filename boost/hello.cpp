#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

int * fib(int n) {
   int first = 0, second = 1, next, c;
   int * result = (int *) malloc(sizeof(int) * n);

   for ( c = 0 ; c < n ; c++ )
   {
      if ( c <= 1 )
         next = c;
      else
      {
         next = first + second;
         first = second;
         second = next;
      }
      result[c] = next;
   }
   return result;
}

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("fib", fib);
}
