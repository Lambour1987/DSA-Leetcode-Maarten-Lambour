// 24-4-2026 Display Digits of a number
// Gebruik Modules, delen
// BELANGRIJK: For Each loop kan niet! want het gaat hier om een integer, niet een array
// dus door een lijst van strings kan je wel met een for loop gaan. Voor individuele letters
// vervolgens met een for each loop. Maar bij een integer kan je dan alleen door de getallen
// lopen met % . en er was dan ook weer een opgave waarin je ipv delen juist iets anders
// moest gebruiken. Dus dat is nog sneller.

#include <iostream>
#include <stdlib.h>

using namespace std;

//n=1742

int main()
{
    int getal;
    cout<<"Voer een getal in: "<<endl;
    cin>>getal;

    //zolang de integer niet leeg is
    int i = 10;
    int rest;
    // Zolang de integer nog niet leeg is.
    // Van het nieuwe getal moet ook een getal af zijn anders wordt die nooit leeg.
    // while getal>0 kan ook
    while(getal != 0)
    {
        rest = getal%10;
        getal = getal/10;
        cout<<" Huidige getal is: "<<getal;
        cout<<" Het restgetal is: "<<rest<<endl; 
        
    }

};



