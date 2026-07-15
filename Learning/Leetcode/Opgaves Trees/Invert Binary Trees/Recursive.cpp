//14-4-2026: Recursief steeds een naar beneden en swappen. 
// Nog doen: zoals ik inituitief denk:: eerst naar het einde en bij het einde swappen:
// Dat is volgens chatgpt linked list denken. Want er is geen 'einde' boom of 'laatste' node.
// Elke node is een mini einde.

#include <iostream>
#include <stdlib.h>
#include <algorithm>

struct BoomKnooppunt
{
    int waarde;
    BoomKnooppunt* linkerkind;
    BoomKnooppunt* rechterkind;
    BoomKnooppunt(): waarde(), linkerkind(nullptr), rechterkind(nullptr){};
    BoomKnooppunt(int x): waarde(x), linkerkind(nullptr), rechterkind(nullptr){};
    // Hier geen derde constructor nodig, zoals bij linked list
    // Wat wel mag, maar is anders dan bij LL:
    BoomKnooppunt(int x, BoomKnooppunt*left, BoomKnooppunt*rechts);

};

// Geen destructor nodig?

class Solution
{
    public:
        BoomKnooppunt*InvertBinaryTree(BoomKnooppunt*Wortel)
        {
            //Basecase: als er geen nodes zijn (net als bij linked list)
            //Dat is ook als je dus helemaal door de boom bent heengelopen en 
            //bij een van de uiteinden bent. Dus er is gewoon 1 basecase. Return nullptr
            if(!Wortel) return nullptr;
            //Bij reverse linked list maakten we een newHead die we zetten op head.
            //Met head gaan we de boom door. Hier: 

            
            //Als we nog niet bij het einde zijn swappen we de huidige node
            std::swap(Wortel->linkerkind, Wortel->rechterkind);

            // Waar bij recursief oproepen van Linked List nog iets voor het isteken hadden
            // staan doen we dat hier niet. Iets bijv met (New=InvertBinaryTree(Wortel->linkerkind))
            InvertBinaryTree(Wortel->linkerkind);

            InvertBinaryTree(Wortel->rechterkind);


        }
        return Wortel;

};

//Hulpfunctie om de tree Recursief en Pre Order te printen
//Functie hoeft niks terug te geven
//Dit is normale recursion:
//Belangrijk: printen gaat dus Pre-Order: Vergelijk even met die
//Andere opgave met DFS boom doorlopen
void printPreorder(BoomKnooppunt*Wortel)
{   
    // Als leeg is return
    if(!Wortel) return;

    std::cout<<Wortel->waarde<< " ";
    printPreOrder(Wortel->linkerkind);
    printPreOrder(Wortel->rechterkind);

}



int main()
{
    // We maken een object aan de heap (naamloos)
    // We hebben wel een pointervariabele Wortel die een adres opslaat
    BoomKnooppunt* Wortel = new BoomKnooppunt(1);

    //Maak kinderen aan: Wortel->linkerkind is vergelijkbaar met
    //head->next van een linked list
    Wortel->linkerkind = new BoomKnooppunt(2);
    Wortel->rechterkind = new BoomKnooppunt(3);

    Wortel->linkerkind->linkerkind = new BoomKnooppunt(4);
    Wortel->linkerkind->rechterkind = new BoomKnooppunt(5);

    Wortel->rechterkind->linkerkind = new BoomKnooppunt(6);
    Wortel->rechterkind->rechterkind = new BoomKnooppunt(7);

    std::cout << "Orgineel:  ";
    printPreorder(Wortel);
    std::cout<<std::endl;

    Solution s;
    Wortel = s.InvertBinaryTree(Wortel)

    std::cout<<"Inverted: ";
    printPreorder(Wortel);
    std::cout<<std::endl;

    return 0;

}
