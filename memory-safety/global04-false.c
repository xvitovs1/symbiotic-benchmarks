#include <stdio.h>

int array[10];

// function returns array of numbers
int* getNumbers() {

   for (int i = 0; i < 10; ++i) {
      array[i] = i;
   }

   return array;
}

int* getNumbers2() {
	int* numbers = getNumbers();
	int numbers2[10];
	for (int i = 0; i < 10; ++i) {
		numbers2[i] = numbers[i];
	}

	return numbers2;
}

int main (void) {

   int *numbers = getNumbers2();
	
   numbers[0] = 100;

   return 0;
}
