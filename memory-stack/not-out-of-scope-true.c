#include<stdlib.h>
#include<stdio.h>

int main(void) {
	int *myPointerA = NULL;
	int *myPointerB = NULL;


	int myNumberA = 7;
	myPointerA = &myNumberA;

	int myNumberB = 3;
	myPointerB = &myNumberB;

	int sumOfMyNumbers = *myPointerA + *myPointerB;
	printf("%d", sumOfMyNumbers);

	return 0;
}
