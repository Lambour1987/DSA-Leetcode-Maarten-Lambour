// 13-4-2026: Het idee is om de waarden uit de lists naar een array te zetten
// De array die kan makkelijker swappen

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

struct Knooppunt
{
    int waarde;
    Knooppunt *volgende;
    // Default Constructor
    Knooppunt() : waarde(0), volgende(nullptr){};
    // Parameterized constructor
    Knooppunt(int x) : waarde(x), volgende(nullptr){};
    Knooppunt(int x, Knooppunt *volgende) : waarde(x), volgende(volgende){};

};

class Solution
{
public:
    Knooppunt* ReorderList(Knooppunt*head)
    {
        // Als de lijst leeg is, hoeft er niks te gebeuren
        // Let op je moet het hoofd dus retourneren hier (niet false of iets anders)
        if(!head) return head;

        // Initialiseer eerst een array om de knooppunten in op te slaan
        // Dus niet de waarden?
        vector<Knooppunt*>array;

        //De waarden vanuit de Linked Lists naar een array
        //Zolang de pointer het eind nog niet heeft bereikt
        Knooppunt* huidig = head;

        while(huidig !=nullptr)
        {   
            // Kopieer de waarde van huidig naar de array
            // Dus niet array[j] = Knooppunt->waarde;
            // Omdat het niet een array van integers is maar een array van pointers.
            // We voegen toe aan de array met pushback
            // We hebben hier dus ook geen array pointer nodig
            array.push_back(huidig);

            // incrementeer huidig pointer
            huidig = huidig->volgende;
            

            
        }
        //Nu gaan we door de array van Knooppunten lopen: we nemen een pointer links en een pointer rechts
        //Deze laten we naar het midden lopen
        int links=0, rechts=array.size()-1;

        while(links<rechts)
        {
            // De huidige Node (van de array) verbinden we met de achterste Node
            // Dus de array van pointers. Pointers hebben weer een 'volgende'
            array[links]->volgende= array[rechts];
            links++;

            // Als we in het midden zijn aangekomen verbreken we de lus
            // Hiervoor gebruiken we break
            if(links>=rechts)
            {
                break;
            }
            // Verbind de achterste node met de volgende voorste node
            array[rechts]->volgende = array[links];
            rechts--;
        }
        // Sluit de lijst af: voorkom dat er een cyclus ontstaat
        array[links]->volgende = nullptr;

        return head;
    }
};

// Helper functie om de lijst te printen
// Hier dus niet ostream& operator maar het is een lijst, dus we willen
// de data van iedere node printen

void printLijst(Knooppunt* head)
{
    Knooppunt* huidig = head;
    while(huidig)
    {
        cout<< huidig->waarde << "";
        huidig = huidig->volgende;
    }
    cout << endl;
}


int main()
{
    // We gaan 5 Knooppunten maken: 5 pointers naar knooppunten. 
    // Ieder knooppunt moeten we toevoegen op de heap

    Knooppunt *n1 = new Knooppunt(1);
    Knooppunt *n2 = new Knooppunt(2);
    Knooppunt *n3 = new Knooppunt(3);
    Knooppunt *n4 = new Knooppunt(4);
    Knooppunt *n5 = new Knooppunt(5);

    // Linked List bouwen door de knooppunten naar elkaar te laten verwijzen

    n1->volgende = n2;
    n2->volgende = n3;
    n3->volgende = n4;
    n4->volgende = n5;

    // Head knooppunt verwijzen we naar n1
    Knooppunt * head = n1;

    cout<< "Orgineel: ";
    printLijst(head);

    Solution s;
    // Bij ReorderList had ik geen 'public' gezet dus het was private.
    head = s.ReorderList(head);

    cout<< "Reordered: ";
    printLijst(head);

    return 0;


}

