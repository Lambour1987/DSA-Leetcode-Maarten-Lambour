//28-4-2026: merge arrays. Hier los gemaakt van het volledige programma 
//er komen best wat aantekeningen bij kijken

#include <iostream>
#include <stdlib.h>

using namespace std;

int Array[] Merge(ArrayA,ArrayB)
{
    // Nieuwe array aanmaken ter grootte van array A + B
    // Check of dit klopt
    
    
    // Initialiseer i,j,k op 0;
    int i=0;
    int j=0;
    int k=0;

    // Loop over array A heen en loop tegelijk over array B heen.

    // Ga door zolang 1 van beide (i of j) het eind van de array heeft bereikt
    while(i< ArrayA.length() || j<ArrayB.length())
    {
        if(ArrayA[i]<ArrayB[j])
        {
            ArrayC[k] = ArrayA[i];
            i++;
            k++;
        }
        else // if Array[j]<Array[i]
        {   
            ArrayC[k]=ArrayC[j];
            j++;
            k++;
        }
    
        // Ik zou zeggen: de rest van Array A of B zou automatisch meegenomen worden
        // als de omvang van de arrays gelijk was. Stel:
        // array A[]={2,5,13,22,29,33,34}
        // array B[]={3,8,14,15,0,0,0}
        // Dan hebben beiden evenveel capaciteit dan hoef je de rest van de code uit de uitwerking
        // niet erbij te beschrijven. En de omvang van Array C is dan niet lengte array A + lengte array B maar
        // omvang Array A + omvang Array B
        // Hier uitwerking aanhouden.
    }

}


int main()
{
    int ArrayA[] = {3,8,16,20,25};
    int ArrayB[] = {4,10,12,22,23};
    int ArrayC[] = Merge(ArrayA,ArrayB);


}