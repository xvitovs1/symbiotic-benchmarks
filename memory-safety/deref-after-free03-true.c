#include<stdlib.h>

int main(void) {
    int* p = malloc(10 * sizeof(int));

    for(int i = 0; i <= 10; i++) {
        if(i == 10) {
            free(p);
        }
        else {
            p[i] = 1;
        }
    }

    return 0;
}
