// Fast & Slow Pointer: Tortoise and Haze


// Gebruik 2 pointers startend op head: fast and slow
// Geen Node, geen cycle (zelf: is basecase?)
// Als fast een einde heeft dan is er geen cycle. Slow is trager dus dat maakt niet uit.
// De waarden zijn niet relevant
// Zodra de fastpointer op het adres komt van slow pointer is er sprake van een cycle.


#include <stdlib.h>
#include <iostream>

using namespace std;

// We starten weer met een LijstKnooppunt Struct (zonder ';' anders is het forward declaration)
// We maken een default en parameterized constructor

// Nog checken: voor deze opgave: is een int waarde strict noodzakelijk? 
struct LijstKnoopPunt
{
    int waarde;
    LijstKnoopPunt*volgende;
    // Default Constructor
    LijstKnoopPunt(): waarde(), volgende(nullptr) {};
    // Parametrized Constructor
    LijstKnoopPunt(int x): waarde(x), volgende(nullptr) {};
    // Parameterized Constructor met volgende pointer
    LijstKnoopPunt(int x, LijstKnoopPunt*volgende): waarde(x), volgende(volgende) {};
};


class Solution
{
    public:
        // In de opgave staat dat de index niet als parameter hoeft te worden meegenomen
        bool CycleDetection(LijstKnoopPunt*head)
        {
            // We maken geen nieuwe nodes, dus 'new' of 'malloc' niet nodig
            // Wel maken we twee pointers die beide wijzen naar head: fast and slow
            LijstKnoopPunt*fast = head;
            LijstKnoopPunt*slow = head;

            // Met beide pointers itereren we door de linked list. Eerst controle op
            // Volgende zaken:

            // 1) Als er geen knooppunt is, dan is er geen list
            // Overbodig want dat checken we al in de while loop
            // Soms toch neerzetten voor leesbaarheid: geen list, geen cycle.
            if (head == nullptr) return false;

            // 2) Zolang fastpointer geen nul is, kan er sprake zijn van een cycle
            // Hoe zet je dit nou neer: je hoeft alleen de naam van de pointer (fast of slow)
            // neer te zetten, niet weer 'Lijstknooppunt *fast'.

            while(fast !=nullptr && fast->volgende !=nullptr)
            {
                fast = fast->volgende->volgende;
                slow = slow->volgende;

                // Belangrijk: ik had eerst: if(fast->next==slow). Maar dat kan dus niet.
                // Het is gewoon if(fast==slow)
                if(fast==slow)
                {
                    return true;
                }
                // Continue is overbodig, want dat doet het algoritme al.
                // Andersom (bijv als if(fast!=slow), continue) was ook overbodig geweest.
                else
                {
                    continue;
                }
            }
            return false;
        }
};


int main()
{
    // Aanmaak nieuwe LijstKnooppunten
    // Bij Merge Linked List deden we LijstKnooppunt * lijst1 = new LijstKnooppunt(1, new LijstKnooppunt(3, new LijstKnooppunt(5)));
    // Kan schijnbaar wel maar bij deze opgave doen we zonder nesten
    LijstKnoopPunt* n1 = new LijstKnoopPunt(1);
    LijstKnoopPunt* n2 = new LijstKnoopPunt(2);
    LijstKnoopPunt* n3 = new LijstKnoopPunt(3);
    LijstKnoopPunt* n4 = new LijstKnoopPunt(4);

    // Koppel nodes 1->2->3-4
    n1->volgende = n2;
    n2->volgende = n3;
    n3->volgende = n4;

    // Cycle 4->2
    n4->volgende = n2;

    Solution sol;

    // Bij het doorgeven van de parameter is alleen head geven voldoende
    bool answer = sol.CycleDetection(n1);

    if(answer==true)
    {
        cout<<"Cycle gevonden!"<<endl;
    }
    else
    {
        cout<<"Geen cycle gevonden!"<<endl;
    }

    return 0;
}

