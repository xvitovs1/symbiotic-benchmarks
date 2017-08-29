#include<stdlib.h>

int* getArray(size){
    int* array = malloc(size * sizeof(int));
    
    for (int i = 0; i < size; i++) {
        array[i] = 0;
    }

    free(array);

    return array;
}

int main(void) {
    int size = 10;
    int* array = getArray(size);

    for (int i = 0; i < size; i++) {
        array[i] = 1;
    }

    free(array);

    return 0;
}
