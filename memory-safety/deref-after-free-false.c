#include<stdlib.h>

int main(void) {
    int* a = malloc(10 * sizeof(int));

    a[0] = 1;

    free(a);

    a[0] = 1;

    return 0;
}
