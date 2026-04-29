#include <stdio.h>

using namespace std;


// Definieer een structure voor array met 3
struct Array
{
    // Maak een array 
    // Pointer naar het eerste element van een array
    int *A; 
    // Totale capaciteit
    int size; 
    // Lengte
    int length;
};

int main()
{
    struct Array arr;
    printf("Enter size of an Array: ");
    scanf("%d", &arr.size);

    return 0;
}