#include<stdlib.h>

int main(void) {
    int* p = malloc(sizeof(int));

    free(p);

    p = malloc(sizeof(int));

    *p = 1; 

    free(p);

    return 0;
}
