// 26-4-2026 Je zou weer vanuit het midden kunnen bekijken maar dat is denk ik
// hier niet per se de bedoeling. Het gaat hier om een integer en niet een array.
// Dus het kan wel maar dan moet je eerst het midden bepalen door te tellen hoeveel nummers
// de integer heeft.
// Denk ook weer eens aan een graaf: welke methoden om het midden te bepalen

// Stel getallen zijn 135531: lengte ophalen. l+(r-l)/2 = m  0+(6-0)/2=3
// Stel getallen zijn 13531: lengte ophalen. l+(r-l)/2 = m  0+(5-0)/2=2. Dan starten bij index 2. (lengte is 5, maar index 2)
// links op index 2-1, rechts op index 2+1

// Ik wil een functie maken die het midden berekent. Maar als output moet die een linkerpointer en
// rechterpointer geven (links en rechts van midden). Omdat een int functie maar 1 waarde terug kan geven
// is het beter om een struct te maken.

#include <iostream>
#include <stdlib.h>

using namespace std;

struct Pointers
{
    int linkerindex;
    int rechterindex;
};


int IntegerTelFunctie(int getal)
{
    int count=0;
    while(getal !=0)
    {
        getal = getal/10;
        count++;
    
    }
    cout<<"aantal digits is: "<<count<<endl;

    return count;
}

// Deze functie moet dus 2 pointers teruggeven
// Pointers is het datatype output. dus 'struct' niet nodig om erbij te zetten
// Ook niet nodig om deze als parameter mee te geven.
Pointers BerekenMidden(int aantal)
{
    //We maken dan eerst een object aan van het type Pointers
    Pointers info;

    // Bereken hier alvast midden
    int midden = aantal/2;
    
    //Bepalen even of oneven lengte van het aantal
        if(aantal%2==0)
    {
        cout<<"Het getal is even"<<endl;
        //Linkerpointer zetten we op index-1
        info.linkerindex = midden-1;
        //Rechterpointer zetten we op de index zelf
        info.rechterindex = midden;
    }
    else
    {
        cout<<"Het getal is oneven"<<endl;
        // Linker pointer zettwen we op index midden-1
        info.linkerindex = midden-1;
        // Rechter pointer zetten we op index midden+1
        info.rechterindex = midden+1;

    }

    cout<<" de linkerpointer is: "<<info.linkerindex<<" de rechterpointer is "<<info.rechterindex<<endl;

    // dus nu returnen we het object:
    return info;
    
}

// Dus als argument de linkerpointer en rechterpointer van de struct pointers, 'info' is
// hier weer niet nodig.
bool Palindrome(Pointers linkerpointer, Pointers rechterpointer)
{
    //26-4-2026: eventueel verder uitwerken. Beetje lastig gemaakt
}



int main()
{
    int getal;
    cout<<"Voer het getal in: ";
    cin>>getal;
    int aantal = IntegerTelFunctie(getal);
    // Dus let op zet hier de naam van het struct neer
    Pointers p = BerekenMidden(aantal);


}


