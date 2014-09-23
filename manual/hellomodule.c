#include <stdio.h>
#include <stdlib.h>

int * fib(int n) {
   int first = 0, second = 1, next, c;
   int * result = (int *) malloc(sizeof(int) * n); 
   printf("First %d terms of Fibonacci series are :-\n",n);
 
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

int main() {
   int c;
   int * result = fib(20);
   for(c = 0; c < 20; c++) {
       printf("%d\n", result[c]);
   }
   free(result);
}
