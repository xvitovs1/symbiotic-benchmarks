#include<stdlib.h>

int main(void) {
    int p[10];
    p[0] = 1;
    realloc(p, 20*sizeof(int));
    free(p);
    return 0;
}
