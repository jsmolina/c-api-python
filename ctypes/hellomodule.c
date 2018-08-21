#include <stdio.h>
#include <stdlib.h>

void fib(int n, unsigned long * result) {
   int first = 0, second = 1, next, c;

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
   return;
}
