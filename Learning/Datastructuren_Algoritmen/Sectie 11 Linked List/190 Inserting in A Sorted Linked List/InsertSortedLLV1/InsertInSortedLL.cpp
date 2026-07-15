// 29-4-2026: Insert In A Sorted Linked List: Hier dus met 2 pointers
// 30-4-2026: Bewaar & Zelf debuggen
// 2-5-2026: Nog verbeteren c.f. Abdul Bari. Hij doet 2 pointers (of 3 incl temp)


// Stappenplan
// De list bouwen voordat we gaan inserten. Omdat een Node meerdere members heeft, is het handiger deze in 
// een container (struct Node) te plaatsen zodat we alleen de struct Node hoeven mee te geven.
// 1) Bouw de Node 
// Waarde + Pointer naar volgende Node + Constructor (geen destructor?) + Pointer naar Node?
// 2) Creeer een Linked List
// --> Als input een gesorteerde array 

// 2.1) Eerste Node Aanmaken
//
//
// 2.2) Volgende Nodes aanmaken
//
//
//


// 3) Nieuwe node invoegen tussen andere nodes in, aan het begin of aan het einde
// 4) Nieuwe Node temp aanmaken met waarde en pointer wijzen naar

#include <iostream>
#include <stdlib.h>

using namespace std;


// Bouw de node
struct Node
{
    int data;
    struct Node * next;
}// Globale pointer First, Last; 
*First=nullptr, *Second=nullptr, *Third=NULL;
// Constructor?
// Destructor?

void Create(int ArrayA[], int size)
{
    // Maak een Last pointer aan die verwijst naar de struct Node
    struct Node*Last = nullptr; // wat als je deze naar niks wijst?
    // Maak een pointer temp aan die wijst naar null
    struct Node*temp = nullptr;
    // First is globaal dus kan je gewoon gebruiken zonder als parameter toe te voegen?
    First=(struct Node*)malloc(sizeof(struct Node));
    // Voeg data veld toe: de eerste waarde uit de array (index 0)
    First->data = ArrayA[0];
    // Verwijs naar volgende node (dat is niks, want laatste Node)
    First->next = nullptr;
    // Verwijs Last naar de First Node door het adres van First aan Last te geven
    Last = First;
    // We gaan eerst de volledige array door: start vanaf 1 want de eerste hebben we al aangemaakt
    // Kan niet want we moeten de size weten voor de array: for(int i = 1; i<ArrayA[length];i++)
    // Voor iedere nieuw aan te maken node maken we een temp variabele aan in heap
    for(int i= 1; i<size; i++)
    {
        // Maak temp variabele aan in heap
        temp = (struct Node*)malloc(sizeof(struct Node));
        //Voeg dataveld van tijdelijke variabele toe
        temp->data = ArrayA[i];
        //Voeg volgende veld van tijdelijke variabele toe
        temp->next = nullptr;
        // Verbindt de nodes
        Last->next = temp;
        // Verplaats Last pointer
        Last = temp;
    }

}

// Display onder Create gezet maakt dat uit?
// Display een lijst van nodes. Gebruik als input een array
void Display(int ArrayA[])
{
    // We maken een pointer aan die wijst naar de reeds bestaande struct Node
    struct Node*huidig = First;
    // Zolang data->next van huidige node niet gelijk is aan null, print de data, en ga naar
    // volgende node
    while(huidig->next!=nullptr)
    {
        cout<<huidig->data;
        // Heb je net als met itereren zoiets hier als i+=1;?
        huidig=huidig->next;
    }
}

// Sorted Insert: als parameter zou ik zeggen: we hebben de lijst al gemaakt dus de pointer naar die lijst is de input
// Daarnaast wil je een waarde toevoegen tussen de bestaande lijst.
// 30-4-2026: Deze opnieuw doen: 1 pointer zoekt 1 onthoudt.
void SortedInsert(struct Node*First, int waarde)
{
    // Tijdelijke pointer
    struct Node*temp;
    // eerst temp node aanmaken in heap
    temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data=waarde;
    temp->next=nullptr;
    // 2 pointers nodig en een tijdelijke variabele node aanmaken, want gesorteerd dus: 
    // Dummy hier niet nodig want?
    // Pointer Tweede op head(first), een pointer Eerst op head->next;
    // Bij nader inzien ongelukkkig gekozen termen.
    struct Node*Eerste = First->next;
    struct Node*Tweede = First;
    //BELANGRIJK: wat doen we:
    //We lopen door de linked list heen zolang de data van Eerste en Tweede hoger zijn dan de
    //in te voegen waarde. 
    //We lopen door de lijst totdat de waarde van de data-Eerste hoger is dan de in te voegen waarde
    //en de waarde van de data-Tweede lager is dan de in te voegen waarde
    // OF: we lopen gewoon door de lijst tot aan het eind en als waarde Eerst hoger en Tweede kleiner dan stop (makkelijker)
    while(Eerste !=nullptr)
    {
        // Voor de eerste node inserten (daar staat pointer 'Tweede' op). 
        // Kan denk ik ook (if(Tweede->data<waarde)) Maar dit ligt eraan of pointer 'Tweede' nog op de eerste Node staat?
        if(First->data<waarde)
        {
            //Temp node volgende naar first
            temp->next = First;
            //Verplaats First pointer terug (naar temp): het adres van temp naar first
            temp = First;
        }
        
        // Tussenvoegen
        // Kan dit ook? if(Eerste->data<temp->waarde&&Tweede->data>temp->waarde)        
        else if(Eerste->data<waarde&&Tweede->data>waarde)
        {
            // Dan nieuwe node tussen tweede eerste node
            // Verwijs tweede next naar temp
            Tweede->next=temp;
            temp->next=Eerste;
        }
        // als het om de laatste node gaat
        else
        {
            //Verwijs laatste (eerste) node naar temp
            Eerste->next = temp;
            //Verplaats Eerste naar temp door adres van temp door te geven aan last
            Eerste = temp;
        }
    }

}


int main()
{
    // Getal 5 overslaan
    int ArrayA[] = {10,20,30,40,50};
    Create (ArrayA,7); // Let op volgens mij dus hoef je niet te zetten Create (ArrayA[])

    int waarde = 15;
    SortedInsert(First, waarde);

    return 0;
};