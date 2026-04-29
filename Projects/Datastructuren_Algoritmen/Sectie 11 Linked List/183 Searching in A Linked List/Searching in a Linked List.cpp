
#include <iostream>
#include <stdlib.h>

using namespace std;

struct Knooppunt
{
    int waarde;
    struct Knooppunt * volgende;
//Hieronder dus een globale pointer die in meerdere functies te gebruiken is
//BELANGRIJK: Globaal gedeclareerd dus het is niet nodig om deze als argument mee te geven
// aan een functie.
}*Eerste;

// We gaan een linked list maken


// We hebben als input een array en een integer lengte
void Create(int Array[], int lengte)
{
    int i = 0;
    struct Knooppunt *Temp, *Laatste;
    Eerste = (struct Knooppunt*)malloc(sizeof(struct Knooppunt));
    Eerste->waarde=Array[0];
    Eerste->volgende = NULL;
    Laatste = Eerste;
   
    for(i = 1; i<lengte;i++)
    {
        Temp = (struct Knooppunt*)malloc(sizeof(struct Knooppunt));
        Temp->waarde = Array[i];
        Temp->volgende = NULL;
        Laatste->volgende = Temp;
        Laatste = Temp;
    }

};

// Eigen gemaakte versie van Lineair zoeken: Iteratief
struct Knooppunt* LineairZoekenV1(struct Knooppunt* Eerste, int target)
{
    while(Eerste)
    {
        if(Eerste->waarde == target)
        {
            return Eerste;
        }
        Eerste=Eerste->volgende;
    }
    return NULL;
}

// Eigen gemaakte versie van Lineair zoeken: Recursief. 
// Basecase, ifstatement, gedeelte na bereiken basecase (terug op callstack)
// pointer = pointer->volgende.
// BELANGRIJK: bij zoeken van maximaal gaan we de hele lijst door naar het eind,
// en dan weer terug. Want dan pas kunnen we het maximaal bepalen. Hier, kan je
// tijdens het verloop al bepalen of het getal dat je nodig hebt er is, dus
// hoef je niet noodzakelijk naar het einde toe te bewegen
struct Knooppunt* LineairZoekenV2(struct Knooppunt* Eerste, int target)
{
    // Basecase: Als de Node Leeg is. Dat is of aan het begin of aan het eind
    if(Eerste==NULL)
    {
        // Als we aan het einde van de lijst komen dan returneren we 0.
        return NULL;
    }
    // Dan hier pas target gaan zoeken: Als gevonden return target 
    if(Eerste->waarde==target)
    {
        return Eerste;
    }
    // Niet gevonden: 
    return LineairZoekenV2(Eerste->volgende, target);
};



int main()
{

}