// 2-5-2026: uitgewerkt van bord, niet van codeeroefneing
// BELANGRIJK: In c kan je geen functies hebben met dezelfde naam, maar in C++ wel indien de functies andere parameters hebbe
// Dit heeft dus FUNCTION OVERLOADING
// Voordeel: niet steeds andere namen


#include <iostream>
#include <stdlib.h>

using namespace std;


int add(int a, int b)
{
    return a+b;
}
// Functienaam en datatype hetzelfde, maar meer parameters
// Return type (hier int) niet belangrijk   
int add(int a, int b, int c)
{
    return a+b+c;
}
// Functienaam en aantal parameters hetzelfde, maar ander datatype
float add(float a, float b)
{
    return a+b;
}


int main()
{
    int nummer1,nummer2,nummer3;
    cout<<"geef nummers: "<<endl;
    // cin>>nummer1, nummer2, nummer 3; kan niet
    cin>> nummer1;
    cin>> nummer2;
    cin>> nummer3;;
    int res1 = add(nummer1,nummer2);
    int res2 = add(nummer1,nummer2,nummer3);
    cout<<"Uitkomst eerste functie: "<<res1<<endl;
    cout<<"Uitkomst tweede functie: "<<res2<<endl;
    float getal1= 1.24;
    float getal2= 1.44;
    float res3 = add(getal1,getal2);
    cout<<"Uitkomst derde functie: "<<res3<<endl;

}