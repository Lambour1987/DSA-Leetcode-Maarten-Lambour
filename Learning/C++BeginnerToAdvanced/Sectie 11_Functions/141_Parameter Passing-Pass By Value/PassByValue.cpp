//3-5-2026

#include <iostream>
#include <stdlib.h>

using namespace std;


// BELANGRIJK: Dit is dus pass by value en geeft niet het goede resultaat:
// Je maakt kopieen die je niet returned. Die verwdijwen dan na uitvoer
// van de functie uit het geheugen. Als je dat wel wilt moet je een pair van int teruggeven.

// BELANGRIJK: Bij print gebruiken we vaak pass by value: juist omdat je gewoon wilt printen.
// dan maak je een kopie. Want '&' meegeven lijkt erop alsof je de variabele wilt aanpassen

void swap(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
    cout<<" Integer b binnen swapfunctie is nu: "<<b<<endl;
    cout<<" Integer a binnen swapfunctie is nu: "<<a<<endl;
}

int main()
{
    int a = 5;
    int b = 6;
    swap(a,b);
    cout<<" Integer b in hoofdfunctie is nu: "<<b<<endl;
    cout<<" Integer a in hoofdfunctie is nu: "<<a<<endl;
    return 0;
}