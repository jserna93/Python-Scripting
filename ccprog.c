#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>  


int main(int argc, char *argv[]) {

    int *arrayPtr = NULL; // Fix typo and initialization
    int sum = 0; // Initialize sum variable
    int threshold = 170; 
    // Check if there are command line arguments
    if (argc < 2) {
        printf("Usage: %s <element1> <element2> ...\n", argv[0]);
        return 1;
    }

    arrayPtr = (int *)malloc((argc - 1) * sizeof(int));

    // Check if memory allocation was successful
    if (arrayPtr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Read elements from command line, convert to integers, and accumulate sum
    for (int arg = 1; arg < argc; arg++) {
        arrayPtr[arg - 1] = atoi(argv[arg]);
        sum += arrayPtr[arg - 1];
    }

    for (int i = 0; i < argc - 1; i++) {
        if (arrayPtr[i] > threshold) {
            printf("255 ");
        } else {
            printf("0 ");
        } 
  
   }
    printf("\n");

   // Print the sum
  //  printf("\nSum is %d\n\n", sum);

    // Free dynamically allocated memory
    free(arrayPtr);

    return 0;
}

