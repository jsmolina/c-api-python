#include <boost/python.hpp>

using namespace boost::python;

unsigned long fibonacci(unsigned long number)
{
   if ( ( number == 0 ) || ( number == 1 ) )
      return number;
   else 
      return fibonacci(number - 1) + fibonacci(number - 2);
}

list fib2(int n) {
   int first = 0, second = 1, next, c;
   list result;

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
      result.append(next);
   }
   return result;
}

BOOST_PYTHON_MODULE(fib)
{
    def("fibonacci", fibonacci);
    def("fib2", fib2);
}
