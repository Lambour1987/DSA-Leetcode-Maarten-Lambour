// Deze oplossing: nog kijken of deze oplossing is gegeven. Is niet de meest praktische
// maar kan wel.
#include <iostream>
#include <sdtlib.h>

using namespace std;



struct LijstKnoop
{
    int waarde;
    int *volgende;
    // Default Constructor
    LijstKnoop(): waarde(), volgende(nullptr){};
    // Parameterized Constructor
    LijstKnoop(int x) : waarde(x), volgende(nullptr){};
    LijstKnoop(int x, LijstKnoop *volgende): waarde(x), LijstKnoop(volgende){};

};

class Solution
{
    public:
    {
        LijstKnoop* RemoveFromEnd(LijstKnoop*head)
        {
            // Eerst de lijst Reversen: dat kan met 3 pointers (of 2 met temp node)
            // Ik geloof een dummy node erbij

            // Eerst een dummy aanmaken
            LijstKnoop Dummy = new LijstKnoop;

            // Dan naar de dummy verwijzen
            LijstKnoop*dummy;
            
            
            LijstKnoop*last



            // Achteraan starten


            // Tellen

        }
    }
}

