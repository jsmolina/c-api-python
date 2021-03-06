#include <stdio.h>
#include <stdlib.h>

unsigned long * fib(int n) {
   int first = 0, second = 1, next, c;
   unsigned long * result = (unsigned long *) malloc(sizeof(unsigned long) * n);
 
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

