//26-4-2026: Reversing a number

// 26-4-2026: nog checken zitten nog foutje sin

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int getal;
    cout<<"geef een getal: "<<endl;
    cin>>getal;
    int i=10;
    int rest = 0;
    int reverse = 0;

    while(getal>0)
    {
        cout<<"tijdes de loop is het getal "<<getal<<endl;
        cout<<"tijdes de loop is de restwaarde "<<rest<<endl;
        rest = getal%i;
        getal = getal/10;
        // BELANGRIJK: met de formule n*10+d kan je een getal toevoegen aan 
        // een integer.
        // Kan niet met bitoperators. 
        reverse = reverse * 10 + rest;
        cout<<"tijdes de loop is de reverse "<<reverse<<endl;
    }

    cout<<"na de loop is het getal "<<getal<<endl;
    cout<<"na de loop is de restwaarde "<<rest<<endl;
    cout<<"na de loop is de reverse "<<reverse;


    return 0;
}