#include <stdio.h>

// function returns array of numbers
int * getNumbers() {
	if(__VERIFIER_nondet_int()){
		static int array[10];
		for (int i = 0; i < 10; ++i) {
			array[i] = i;
		}
		return array;
	}
	else{
		int array[10];
		for (int i = 0; i < 10; ++i) {
			array[i] = i;
		}
		return array;

	}
}

int main (void) {
	int *numbers = getNumbers();

	for (int i = 0; i < 10; i++ ) {
		printf( "%d\n", *(numbers + i));
	}
	
	return 0;
}
