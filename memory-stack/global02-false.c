#include<stdlib.h>

int* globalVariable = 4;

int main(void) {
 free(globalVariable);
 return 0;
}
