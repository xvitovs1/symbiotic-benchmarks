#include <stdio.h>
#include <alloca.h>

// function returns array of numbers
int * getNumbers() {

   int *array = alloca(10 * sizeof(int)); // array should be static

   for (int i = 0; i < 10; ++i) {
      array[i] = i;
   }

   return array;
}

int main (void) {

   int *numbers = getNumbers();

   for (int i = 0; i < 10; i++ ) {
      printf( "%d\n", *(numbers + i));
   }

   return 0;
}
