// 30-4-2026

// Class Diagonal Maken met pointer en integer
// Constructor met getal=2 en constructor met getal (dynamisch)
// Memberfuncties Get, Set, Display
// GetDimension
// Main: Vraag dimensie, maak object, vraag alle matrixwaarden in te voeren, 
// verander een waarde
// Voeg copy constructor toe
// Voeg destructor toe

#include <iostream>
#include <stdlib.h>

using namespace std;


class Diagonal
{
    // C++ class is standaard Private. (in struct is class standaard public)
    // Eigenschappen van diagonal zijn dus private
    private:
        int *A;
        int getal;
        

    // In public: want we moeten objecten kunnen maken.
    public:
        // Default Constructor: 
        //-->Noem classnaam tussen haakjes, 
        Diagonal()
        { //--> noem variabele zonder datatype en initialiseer
            getal = 2;
            // Bij een pointer maak aan in heap (elders gaven we daar tussen haakjes nog aan: lengthe. bijv New A(lengthA+LengthB)
            // Dus rechts van '=' maak een nieuw 'datatype' en tussen square brackets omvang. Links van '=' naam variabele (hier pointer)
            // dus variabele = new 'datatype' (omvang)
            A = new int[2];
        }
    // Parameterized Constructor: input is n
        Diagonal(int n)
        {
            this->getal = n;
            A = new int[n];
        }
    // Hier dus een destructor: dit wordt automatisch aangeroepen als object verdwijnt
        ~Diagonal()
        {
            // We deleten een array dus []A en niet 'A'
            delete []A;
        }
    // Member function declaraties/ Method Declaration in een class. (Forward Declarations meestal buiten de class)
    
    void Set
    int Get
    void Display
    int GetDimensions
}


