// 3-5-2026: Return by address
// Nog eens doen

//BELANGRIJK
// Stack + value
// Je functie krijgt een kopie van de data op zijn eigen stack. 
// Die kopie bestaat alleen tijdens de functie. Als je iets wil 
// bewaren in main, moet je het teruggeven via return.

// Stack + reference
// Je functie krijgt een alias naar een variabele die in main bestaat. 
// Je werkt direct op die originele data, dus er is geen kopie nodig.

// Heap
// Je maakt data aan die niet bij een functie hoort maar in een globale geheugenruimte (heap). 
// Die data blijft bestaan na de functie en je krijgt een pointer terug om er toegang toe te houden.

#include <stdlib.h>
#include <iostream>

using namespace std;

// Doel: maak in heap een array van elementen. start met 1 en ga tot en met 5

// BELANGRIJK: We gebruiken hier heap + pointers omdat de data moeten blijven bestaan nadat
// de functie klaar is
int* fun(int size)
{
    // maak een integer variabele in heap ter grootte van de omvang van een array van 5 elementen
    int*pointer = new int[size];

    for(int i=0;i<size;i++)
    {
        pointer[i]=i+1; // let op dus niet pointer[i]=pointer[i]]+1
    }
    cout<<"Pointer adres: "<<pointer<<endl;
    // adres weer terug naar main function
    return pointer;
};



int main()
{
    int* q = fun(5);

    for(int i = 0; i < 5; i++)
    {
        cout << q[i] << endl;
    }

    delete[] q; // belangrijk!

}
