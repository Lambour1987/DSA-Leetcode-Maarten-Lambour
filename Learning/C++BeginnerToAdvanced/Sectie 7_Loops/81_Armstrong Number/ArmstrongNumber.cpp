#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int getal;
    int rest;
    int armstrong;
    int totaal=0;
    cout<<" geef een getal ";
    cin>>getal;
    while(getal>0)
    {
        rest = getal%10;
        // Let op '^'  niet zomaar te gebruiken
        armstrong = rest*rest*rest;
        cout<<" getal is "<<getal<<" en de rest is "<<rest<<" en de macht is "<<armstrong<<endl;
        totaal = totaal + armstrong;
        //25-4-2026: nog proberen: volgens mij klopt die maar wat als ik deze regel nu iets naar boven verplaats.
        getal = getal/10;
    }
    cout<<" het totaal is: "<<totaal<<endl;
    if(totaal == getal)
    {
        cout<<"getal is een armstrong nummer";
    }
    {// laatste stukje klopt nog niet
        cout<<"getal is geen armstrong nummer";

    }
};