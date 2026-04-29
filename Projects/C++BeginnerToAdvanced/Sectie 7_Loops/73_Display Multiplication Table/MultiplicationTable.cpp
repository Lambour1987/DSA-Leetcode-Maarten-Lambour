// 22-4-2026
// Dus multiplication table: daar heb je een integer variabele voor het eerste getal.
// Een integer variabele voor het tweede getal
// Een integer variabele voor de multiplicatie
// We schrijven een functie zonder class, dus we hoeven in main geen object aan te maken.


#include <iostream>

using namespace std;


// Beter zou zijn: Display (cout) scheiden van berekening
void MultiplicatieTabel(int tafel, int aantal)
{
    for(int i = 0; i<=aantal;i++)
    {
        cout<<tafel<<"x"<<i<<"="<<tafel*i<<endl;
    }
}

int main()
{
    //roep de functie Multiplication op
    int tafel;
    cout<<"geef de tafel: ";
    cin>> tafel;
    cout<<"geef aantal keer aan dat deze uitgevoerd moet worden: ";
    int aantal;
    cin >> aantal;

    MultiplicatieTabel(tafel, aantal);
} // ';'niet nodig


// niet helemaal 1 op 1 maar vergelijkbaar
// 1. Input / Interactie
// 2. Orchestratie / Programmaflow (Uitvoerend)
// 3. Business Logic / Berekening (Beschikkend)
// 4. Presentatie / Display
// 5. Validatie / Controle (Controlerend)
// 6. Data Opslag / State (Bewarend)

// Voor ieder soort taak eigen functie: Single Responsibility