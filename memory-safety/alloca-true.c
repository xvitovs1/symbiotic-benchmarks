#include <alloca.h>
#include <stdlib.h>

int main(void){
	int *p = alloca(10 * sizeof(int));
	p[5] = 1;
	return 0;
}
