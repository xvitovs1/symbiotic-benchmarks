#include <stdlib.h>

int main(void) {
    int* p = malloc(10 * sizeof(int));
    p[0] = 1;
    free(p);
    p = realloc(p, 20 * sizeof(int));
    return 0;
}
