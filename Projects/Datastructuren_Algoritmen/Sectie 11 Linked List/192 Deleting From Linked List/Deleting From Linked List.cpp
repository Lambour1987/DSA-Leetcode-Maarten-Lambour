// 3-5-2026// Nog doen: Recursive Display

// Eerst een list createn voordat we gaan deleten

#include <iostream>
#include <stdlib.h>

using namespace std;

// Creeer Node Structuur
// Struct dus automatisch public?
struct Node
{
    // data
    int data;
    // pointer naar volgende node
    struct Node *next;
}// Deze pointer hierzetten zorgt ervoor dat we dit niet
// als parameter hoeven mee te geven: 
*First=NULL;



// Create List gebruik als input een array en geef de omvang van de array door
void CreateList(int ArrayA[], int size)
{
    // We maken twee pointers aan: temp en last
    struct Node*Last;
    struct Node*Temp;
    // De First Pointer wijst momenteel naar null. We willen nu in heap een LL aanmaken
    // We maken een nieuwe node met omvang van de struct Node en we wijzen daar de First Pointer aan toe
    // De first pointer is al gedeclareerd. de omvang is gewoon 1 node.
    First = new Node(); 
    // We voegen het dataveld en next veld toe (wijst naar nul)
    First->data = ArrayA[0];
    First->next = nullptr; 
    // Wijs last pointer toe aan de gemaakte node door het adres van First te geven
    Last = First;
    // De rest van de nodes toevoegen aan de list. Begin bij node 1. Steeds een tijdelijke node aanmaken
    // zo vaak als de array lang is (minus 1)
    for(int i=1; i<size; i++)
    {
        Temp = new Node;
        Temp->data = ArrayA[i];
        Temp->next = nullptr; // blijft 0 tenzij we een circel gaan maken doen we niet
        // Verwijs de Node waar last op staat naar temp door het adres van temp door te geven aan Last->next.
        Last->next= Temp;
        // Verschuif Last pointer door deze het adres te geven van temp
        Last = Temp;
        
    }
};

// Voor display geven we de pointer door
void Display(struct Node*p)
{
    // Zolang we het einde van de LL niet hebben bereikt, print de waarde van de node
    {
        while(p)
        {
            cout<<p->data<<endl;
            p=p->next;
        }
    }
}

// Functie waar het hier om gaat: Delete
// Casus 1: Delete de eerste Node
// Casus 2: Delete de Node uit de gegeven positie ("index")

int Delete(struct Node* Head, int positie)
// Variabele aanmaken om straks de waarde van de positie terug te geven
    int Waarde;
// We hebben voor de eerste Node in principe geen extra pointers nodig omdat we al een first/ head pointer hebben
// en die voldoende is? Toch wel? Ja voor de eerste heb je dus wel 2 pointers nodig.
// Dus we maken om te beginnen een dummy node aan omdat we de huidige pointer willen laten starten op de eerste node
// en de vorige pointer moet dan ook ergens starten. Dus op de dummy. Misschien kan je de dummy omzeilen maar dan
// moet je denk ik moeilijk gaan doen met starten op de eerste node en op de tweede node etc. Nog uitzoeken.
// Dus Maak dummy Node. De Current verschuift met while loop, en de previous springt steeds naar current
    struct Node*Previous = New Node;
    // We zetten de current Node op First
    struct Node* Current = First;

    while(Current !=nullptr)
    {
        if(positie == 1)
        {
            // sla data uit head op als waarde;
            waarde = Head->data;
            // verschuif head door deze het adres van head next te geven
            Head = Head->next;
            // Eerste node kan verwijderd worden
            Delete positie;
        }
        else if (positie== current)// positie is tussen begin en einde
        {
            // waarde van node ophalen
            Waarde = Current->data;
            // verplaats huidige node alvast naar voren
            Current = Current->next
            Previous->Next = Current;
            Previous = Current;
            Delete overige.
            
        }
        else // Het gaat om de laatste node
        {
            waarde = Current->data;
            // vorige node moeten we dan naar null pointer laten verwijzen
            Previous->next = Nullptr;
            Delete Current;
        }    
        Previous = Current;
        Current = Current->next;
    }
}






int main()
{
    int ArrayA[]={10,20,30,40,50};
    int size = 5;
    // Dus hier: moeten we dan de return waarde in een nieuwe variabele stoppen? 
    CreateList(ArrayA,size);
    // Moeten we dit hier p noemen
    Display(struct Node *p)
};


