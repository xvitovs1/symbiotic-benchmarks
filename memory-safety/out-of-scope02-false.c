#include<stdlib.h>
#include<stdio.h>

int main(void) {
	int *myPointerA = NULL;
	int *myPointerB = NULL;
	
	if(__VERIFIER_nondet_int())
	{
		int myNumberA = 7;
		myPointerA = &myNumberA;
		// scope of myNumber ends here
	}

	int myNumberB = 3;
	myPointerB = &myNumberB;

	int sumOfMyNumbers = *myPointerA + *myPointerB; // myPointerA is out of scope
	printf("%d", sumOfMyNumbers);

	return 0;
}
