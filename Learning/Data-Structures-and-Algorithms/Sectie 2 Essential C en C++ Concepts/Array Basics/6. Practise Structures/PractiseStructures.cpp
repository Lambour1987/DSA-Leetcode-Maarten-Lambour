#include <stdlib.h>// algemene utilities (memory, random, exit, etc)
#include <stdio.h>//(input/ output lezen en schrijven)
#include <iostream>

using namespace std;

// Defenitie van een structure
struct Rectangle
{
    int length; //2 bytes
    int breadth; // 2 bytes
    char x; //1  byte
} ; //r1,r2,r3; // Hier kan je ook al variabele declareren
// Dan wordt het een globale functie

// Buiten de mainfunctie een variabele declareren:
//struct Rectangle r1;

int main()
{
    struct Rectangle r1={10,5};

    //2 integers + char: dus in totaal 9 bytes.
    // Maar geeft dus 12: waarom? voor machine makkelijker
    // om steeds 4 bytes te lezen: alloceert meer dan nodig
    // Waarschuwing ivm datatype ofzo
    printf("%d", sizeof(r1));

    cout<<r1.length<<endl;
    cout<<r1.breadth<<endl;

    return 0;
}