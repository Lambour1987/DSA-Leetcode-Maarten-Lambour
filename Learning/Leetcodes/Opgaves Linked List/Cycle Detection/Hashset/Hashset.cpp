// 10-4-2026: Oplossing Cycle Detection met Hashset
// Mogelijkheid de hashset ook toe te passen bij disjoint Union set?

#include <iostream>
#include <stdlib.h>
#include <unordered_set>

using namespace std;


// Struct Listnode maken (zonder ';' anders is het een forward declaration)

struct Knoop
{
    int waarde;
    struct Knoop *volgende;
    
    // Default constructor
    Knoop(): waarde(), volgende(nullptr) {};

    // Parameterized constructor
    Knoop(int x): waarde(x), volgende(nullptr){} ;
    Knoop(int x, Knoop *volgende): waarde(x), volgende(volgende){};

}
// Maken we geen destructor?

class Solution
{
    public:
    // De index die als in input wordt gegeven hoeft niet als parameter te worden opgenomen
        bool CycleDetection(Knoop*head)
        {
            // Gebruik een hashset om de index op te slaan, eerste node is 1
            // Dus we slaan nodes op in de set.
            // Hashset lengte is niet te bepalen
            unordered_set<Knoop*> seen;

            // Hoewel we als een pointer 'head' hebben, initialiseren we er nog 
            // een om door de linked list te lopen
            Knoop*huidig = head;

            // Zolang head niet nul is, kunnen we doorgaan
            while(huidig!=nullptr)
            {
                // Zoek in hashset, als gevonden return true
                // Dus: voeg toe aan hashset binnen if statement als(in hashset staat) of daarbuiten
                // 
                if(seen.find(huidig) !=seen.end())
                {
                    return true;
                }   
                // Niet gevonden, dan toevoegen aan hashset
                else
                {
                    seen.insert(huidig);
                    
                    huidig = huidig->volgende;

                }


            }
            return  false;
            
        }
};

int main()
{
    Solution s;

    // Maak een simpele linked list: 1 -> 2 -> 3 -> nullptr
    Knoop* n3 = new Knoop(3);
    Knoop* n2 = new Knoop(2, n3);
    Knoop* n1 = new Knoop(1, n2);

    cout << "Cycle? " << (s.CycleDetection(n1) ? "Ja" : "Nee") << endl;

    return 0;
}