#  Copyright Joel de Guzman 2002-2007. Distributed under the Boost
#  Software License, Version 1.0. (See accompanying file LICENSE_1_0.txt
#  or copy at http://www.boost.org/LICENSE_1_0.txt)
#  Hello World Example from the tutorial

import hello_ext

if __name__ == "__main__":
   print timeit.timeit("fib(10)", "from hello_ext import fib")

