
// Eigen uitwerkign == Gebruik een temporary Vector == O(n) extra space. 
// Niet optimaal maar goede practise

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

// Singly Linked List Node
struct LijstKnooppunt //als je ';' achter struct Lijstknooppunt zet, dan is het een Forward Declaration
{
    int waarde;
    LijstKnooppunt *volgende;

    // Default Constructor
    LijstKnooppunt() : waarde(0),volgende(nullptr) {};
    // Parameterized Constructor
    LijstKnooppunt(int x) : waarde(x),volgende(nullptr) {};
    // Parameterized Constructor met volgende pointer
    LijstKnooppunt(int x, LijstKnooppunt *volgende): waarde(x), volgende(volgende) {}

} // Hier niets?



class Solution
{
    public: 
        LijstKnooppunt* MergeLists(LijstKnooppunt*list1, LijstKnooppunt*list2)
        {
            // Maak een vector aan: dynamisch want lengte Linked Lists zijn nog niet bekend:
            // De omvang weten we niet dus is nul. We kunnen hem niet vullen
            vector<int>samengevoegd;

            // Een pointer 'k' aanmaken is overbodig: we gebruiken pushback voor de vector
            // int k = 0;
            
            // Check of lists niet leeg zijn. Als een van de lists leeg is, return
            // de headpointer van de andere list (Dit heet een one liner statement)
            // NIet nodig want dit lossen we al op met while loop
            // if(!list1) return list2;
            //if(!list2) return list1;

            //Niet kan: list1 || list2 !=nullptr. ! heeft voorrang: operator-precedence
            //Wel kan while(list1||list2)
            // Deze loop loopt zolang beide lijsten nog elementen hebben. Daarna moet je de loop uit
            while(list1 !=nullptr || list2 !=nullptr)
            {
                if(list1->waarde<=list2->waarde)
                {
                    samengevoegd.push_back(list1->waarde);
                    list1 = list1->volgende;
                }
                else //Als list2 een grotere waarde heeft dan list1
                {
                    samengevoegd.push_back(list2->waarde);
                    list2 = list2->volgende;

                }
            }
            // Hier dus de vraag of ik bij ongelijkte lengtes het resterende deel 
            // gewoon plak in de vector. Dit deel:
            // --> binnen de whileloop?
            // --> binnen de while loop if statement?
            // --> buiten de while loop? Dit dus
            // Blijkbaar zoals die nu is
            while(list2!=nullptr)
            {
                samengevoegd.push_back(list2->waarde);
                list1 = list1->volgende;    
            }
            while(list1!=nullptr)
            {
                samengevoegd.push_back(list1->waarde);
                list2 = list2->volgende;
            }

            //Nu alle waarden in de vector staan, moeten we deze terugkopieren naar
            //de linked list of we maken een nieuwe list:
            //We maken een dummy die als startpunt fungeert.
            
            // Ik noem de dummy 'startpunt': dit is geen pointer maar een lokaal 
            // object op de stack: deze mag op stack
            LijstKnooppunt startpunt(0);

            //Nu verwijzen we een pointer genaamd 'Knooppunt' naar de dummy
            //op de stack door het adres van de dummy door te geven
            LijstKnooppunt *Knooppunt =&startpunt;

            //Voor ieder element uit de vector voegen we
            //een knooppunt toe in de heap: Start Knooppunt
            //staat op de heap. Wijst naar stack

            for(int val: samengevoegd)
            {
                Knooppunt->volgende = new LijstKnooppunt(val);
                Knooppunt = Knooppunt ->volgende;
            }
            return Knooppunt->volgende;

        }

        // Debug Helper: Print linked list
        void PrintLijst(LijstKnooppunt* head)
        {
            while(head!=nullptr)
            {
                cout<<head->waarde << "-> ";
                head = head->volgende;
            }
            cout << "nullptr" << endl;
        }

};

int main()
{
    // Maak lijst 1: 1 -> 3 -> 5
    // Wijs een pointer naar Lijstknooppunt (lijst1 kan dan adres opslaan van Lijstknooppunt)
    // Maak geneste linked list
    LijstKnooppunt * lijst1 = new LijstKnooppunt(1, new LijstKnooppunt(3, new LijstKnooppunt(5)));
    
    // Maak lijst 2: 2-> 4 -> 6
    LijstKnooppunt *lijst2  = new LijstKnooppunt(2, new LijstKnooppunt(4, new LijstKnooppunt(6)));

    // We maken een object sol aan
    Solution sol;

    //We gaan lijst1 en lijst2 printen
    sol.PrintLijst(lijst1);
    sol.PrintLijst(lijst2);

    //Nu roepen we de functie MergeLists op en een pointer wordt teruggegeven
    LijstKnooppunt *MergeLists(LijstKnooppunt lijst1, LijstKnooppunt lijst2)

    cout << "Merged list: ";
    sol.PrintLijst(MergeLists);

    return 0;
}

