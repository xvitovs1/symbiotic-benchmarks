#include<stdlib.h>

int* globalVariable = 0;

int main(void) {
 free(&globalVariable);
 return 0;
}
