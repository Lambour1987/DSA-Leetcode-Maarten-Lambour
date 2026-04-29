//16-4-2026: We bouwen een Linked List vanuit een array
// Printen doet het nog nei

// Van de inputarray moeten we een linked list maken. Die bestaat uit nodes.
// Dus we moeten een struct Nodes maken

//Kort: 1e Node creeren in heap en vullen, daarna volgende nodes creeeren en vullen
//Eigen vraag: kan je niet meteen beginnen met het maken van een temp node? en zeggen
// van nul tot einde reeks waarde vullen en doorverwijzen. Dat kan wel schijnt. 
// En is ook logischer. 

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

struct Knooppunt
{
    int waarde;
    Knooppunt* volgende;
  // We declareren een pointer naar de struct Node, met beginwaarde 0.
  // Direct na de struct. Dan hoeven we deze niet in de functie te zetten.
  // Globale variabele pointer.
} *Eerste = NULL;

// Functie die als input heeft een array en als output een pointer naar een knooppunt:
// Omdat we de pointer al gedeclareerd hebben (*First) gebruiken we hier void als output.
// First is dus een globale variabele. We geven eveneens de lengte van de array mee omdat
// C dit niet automatisch herkent. Let ook op hoe we inv vector<int> int getallen met [] zetten.
void CreateLinkedList(int getallen[], int lengte)
{
    // Declaratie 
    int i = 0;

    // We wijzen lokale variabelen toe aan de struct: De tijdelijke node is bedoelt 
    // om te blijven wijzen naar de nieuwe te creereen node en de laatste moet wijzen
    // naar de net eerder gemaakte node.
    struct Knooppunt *Tijdelijke, *Laatste;

    // We maken eerst een nieuwe node aan waarin de eerste waarde van de array aan
    // wordt gegeven.
    // Deze heeft de omvang van een struct Node: malloc(size(*struct Knooppunt)) en geeft
    // terug een pointer (adress) naar deze struct.
    Eerste=(struct Knooppunt*)malloc(sizeof(struct Knooppunt));

    // Dit knooppunt krijgt de eerste waarde van de array getallen
    Eerste->waarde = getallen[0];

    // Het volgende adres wijst nu nog naar nul: 
    Eerste->volgende = NULL;

    // Laatste pointer wijst nu naar de eerste node [waarde 2,wijst naar nul]
    // Door het adres van eerste toe te wijzen naar laatste
    Laatste = Eerste;
    
    // We moeten nu de rest van de nodes maken: Creeren in heap, vullen met waarde en doorverwijzen
    // Dit is steeds de laatste node. Dus de eerstvorige moeten we verwijzen naar de node die we aanmaken
    // En doorverschuiven
    for(i=1; i<lengte;i++)
    {
        Tijdelijke = (struct Knooppunt*) malloc (sizeof(struct Knooppunt));
        Tijdelijke->waarde = getallen[i];
        // Blijven volgende steeds verwijzen naar nul
        Tijdelijke->volgende = NULL;
        // Het vorige (laatste) knooppunt moet wijzen naar het zojuist aangemaakte knooppunt
        // Ook de laatste pointer moet wijzen naar de zojuist aangemaakte.
        Laatste->volgende = Tijdelijke;
        Laatste = Tijdelijke;

    }

};

// Hier dus display doen
// Je hoeft niet te retourneren
void Display(struct Knooppunt *Eerste)
{
    // Zelf gedaan: Een nieuwe pointer verwijzen naar eerste, die de lijst doorloopt
    // omdat 'eerste' niet helemaal een duidelijke naam is:

    Knooppunt*DoorlopendePointer = Eerste;

    // Zolang de lijst nog niet aan het einde is, willen we de waarden printen
    // We starten bij het begin: dat is dus: het hoofd. 
    // Zolang deze niet verwijst naar een nullptr zijn we nog niet bij het einde
    // Denk eraan we gebruiken hier dus C en niet C++. Dus gebruik NULL ipv Nullptr.
    while(DoorlopendePointer!=NULL)
    {
        // Print waarde.
        printf("De volgorde is %d\n ", DoorlopendePointer->waarde);
        // Ga naar de volgende
        DoorlopendePointer = DoorlopendePointer->volgende;
    }

}

// dus bij het doorgeven van een parameter(knooppunt): 
// niet het woord 'struct' maar wel knooppunt
void RecursieveDisplay(Knooppunt*Eerste)
{
    // zelfde idee, maar recursief: dus 
    Knooppunt*DoorlopendePointer = Eerste;


    if(DoorlopendePointer!=NULL)
    {
        //geen 'return' recursivedisplay, want geen return (void)
        RecursieveDisplay(DoorlopendePointer->volgende);
        printf("De recursieve volgorde is: %d\n", DoorlopendePointer->waarde);
    }

};

int IteratiefTellen(Knooppunt*Eerste)
{
    // Voor het overzicht bouw ik weer een doorlopende pointer die geinitieerd wordt op 'Eerst'
    Knooppunt*DoorlopendePointer= Eerste;
    // Totaal bijhouden in een variabele
    int aantal = 0;
    // Zolang we niet bij het einde zijn print de waarde
    while(DoorlopendePointer!=NULL)
    {
        aantal += 1;
        DoorlopendePointer=DoorlopendePointer->volgende;
    }
    return aantal;
};

//BELANGRIJK: Dus we houden een totaalbij. Omdat we if doen, moet dit totaal eigenlijk
//buiten de functie al gedefinieerd worden. Eigenlijk moet dat ook met de pointer
// maar ik gebruik nu even 'eerste'. DIT HOEFT NIET DUS.
int RecursiefTellen(Knooppunt*Eerste, int totaal)
{
    if(Eerste !=NULL)
    {
        // Een variabele totaal bijhouden (in main) is overbodig: recursief telt namelijk zelf al!
        // Dus het kan weg mara mag wel. Dus nog eens uitwerken
        totaal++;
        Eerste=Eerste->volgende;
        // Dus opnieuw oproepen en gebruik 'return': want retourneert een 'int'.
        return RecursiefTellen(Eerste,totaal);
    }
    return totaal;
};

//16-4-2026 Dus nog een keer hier RecursiefTellen maken zonder extra variabele

int IteratieveSom(Knooppunt*Eerste)
{
    //Doorlopende pointer maken
    Knooppunt* DoorlopendePointer = Eerste;

    //Som bijhouden
    int som = 0;

    //Zolang we het einde van de loop nog niet hebben bereikt
    while(DoorlopendePointer!=NULL)
    {
        som = som + DoorlopendePointer->waarde;
        DoorlopendePointer = DoorlopendePointer->volgende;
    }
    return som;
}

// Recursieve som: we gaan nu geen extra variabele bijhouden zoals bij Recursief Tellen
// Want niet nodig

int RecursieveSom(Knooppunt*Eerste)
{   
    // Dus omdat we een int willen returnen: zet return neer.
    // We geven steeds aan dat we naar de volgende willen
    if(Eerste!=NULL)
    {
        return RecursieveSom(Eerste->volgende)+Eerste->waarde;
    }
    return 0;
}

int max(struct Knooppunt*Eerste)
{
    int max = INT32_MIN; 

    // mag ook: while(Eerste)
    while(Eerste!=NULL)
    {
        // Declareer dan deze als minimum zo klein mogelijk, omdat de LL negatieve waarden
        // Kan hebben
        if(Eerste->waarde>max)
        {
            max = Eerste->waarde;
            Eerste = Eerste->volgende;
        }
    }
    return max;
}

// Recursive Max functie: Dit werkt dus zo: We lopen eerst door hele LL heen.
// Dan hebben we alle getallen gehad en daarna bepalen we pas wat het maximum is.
// Dit is anders dan bij Recursief zoeken. waar je gewoon 1 maal door de lijst heen gaat.
int RMaxV1(struct Knooppunt* Eerste)
{
    // In de officiele uitwerking staat nog:
    // int x = 0; Dit is overbodig

    // Als 'Eerste' nul wordt dan zijn we aan het einde van de lijst.  
    if(Eerste==NULL)
    {
        // Aan het einde van de lijst returnen we het minimum aan de
        // vorige Node op de call stack 
        return INT32_MIN;
    }
    else // Dat is als we nog niet aan het einde zijn
    // Dan roepen we de functie opnieuw aan
    {
        int max = RMaxV1(Eerste->volgende);
    
        if(max>Eerste->waarde)
        {
            return max;
        }
        else
        {
            return Eerste->waarde;
        }
    }
};




// Eigen uitwerkingvan RMax, met extra parameter max
int RMaxV2(struct Knooppunt* Eerste, int max)
{
    if (Eerste == NULL)
    {
        return max;
    }

    if (Eerste->waarde > max)
    {
        max = Eerste->waarde;
    }

    return RMaxV2(Eerste->volgende, max);
}





int main()
{
    int getallen[] = {2,3,4,5,6,7,8};
    int lengte = 7;
    // We roepen de functie op met getallen en lengte als argument. We doen niet OOP dus geen object.
    // We retourneren het resultaat in
    CreateLinkedList(getallen, lengte);

    // We kunnen hier 'Eerste' gebruiken omdat het een globale variabele is.
    Display(Eerste);
    RecursieveDisplay(Eerste);
    int AntwoordIteratiefTellen=IteratiefTellen(Eerste);
    printf("Het aantal nodes is..:%d\n", AntwoordIteratiefTellen);

    //Initialiseren variabele buiten de recursieve functie
    int RecursiefAantal = 0;
    int AntwoordRecursiefTellen = RecursiefTellen(Eerste, RecursiefAantal);

    int AntwoordIteratiefSom = IteratieveSom(Eerste);
    printf("De som van de nodes is %d\n", AntwoordIteratiefSom);


    



}