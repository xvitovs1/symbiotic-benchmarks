#include <stdlib.h>

int main(void) {
    int* p = malloc(10 * sizeof(int));
    p[0] = 1;
    p = realloc(p, 20 * sizeof(int));
    p[21] = 1;
    free(p);
    return 0;
}
