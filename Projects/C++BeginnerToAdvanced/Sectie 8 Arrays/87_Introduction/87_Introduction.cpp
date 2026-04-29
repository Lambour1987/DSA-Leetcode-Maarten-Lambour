//28-4-2026: Hier even de verschillende manieren om een array te maken
//28-4-2026: eigenlijk hier een degelijke template class maken voor alle varianten van Display

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;


// Er staat eigenlijk void Display(int* array, int size)
void Display1(int array[], int omvang)
{
    // Kan niet zomaar: for(const auto& numbers:A): want 'A' is geen array maar een pointer
    // naar het eerste element uit de array ookal lijkt dat niet zo.
    for(int i=0; i<omvang;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

// Bij een vector kunnen we gewoon for each loop gebruiken

void Display2(vector<int>array)
{
    for(const auto& num: array)
    {
        cout<<num<<" ";
    }
    cout<<endl;
}

void Display3(float array[],int omvang)
{
    for(int i=0; i<omvang; i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

void Display4(string array[], int omvang)
{
    // Dus hier de letter uit de string. Dus char uit array.
    for(int i=0; i<omvang; i++)
    {
        // is dus eigenlijk de array van strings
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

void Display5(char array[], int omvang)
{
    // Dus hier de letter uit de string. Dus char uit array.
    for(int i=0; i<omvang; i++)
    {
        // is dus eigenlijk de array van strings
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

void Display6(string array[], int omvang)
{
    for(int i=0; i<omvang;i++)
    {
        //Door 'const' erbij te doen kan je de letter niet wijzigen.
        for(const char letter:array[i])
        {
            cout<<letter<<" ";
        }
        // Door naar de volgende letter en regel
        cout<<endl;
    }
    //cout<<" ";
}

// Dus als we de array niet als parameter meegeven, dan werkt een for each loop wel
// Daarnaast kunnen we met & de oorspronkelijke array aanpassen
void Display7()
{
    int G[]={1,2,3,4,5,6,7};
    //"We itereren door de oorspronkelijke array. Bij de eerste iteratie wordt een element
    // gemaakt wat steeds wordt overschreven."
    cout<<"Geen overschrijving van de orginele array: "<<endl;
    for(auto element:G)
    {
        cout<<element<<" ";
        
    }
    cout<<endl;

    cout<<"Wel overschrijving van de orginele array: array wordt nu: "<<endl;
    for(auto& element:G)
    {
         ++element;
         cout<<element<<" ";
    }
    cout<<endl;

};

int main()
{
    // Tijdens runtime op de stack
    int A[] = {1,2,3,4,5,6};
    int B[5] = {1,2,3,4,5};
    int C[5] = {1,2,3,4};
    vector<int> D = {1,2,3,4,5,6};
    float E[] = {1.0,2.1,3.2,4.3,5.4};
    // of: F[5] ={"A","B","C","D","E"}; Het is een string object dus alles tussen " "
    // kan uit meerdere letters bestaan. Let op: " " dubbele aanhalingstekens
    string F[] ={"AAA","BBB","CCC","DDD","EEE"};
    // Hier geen object dus wat niet kan:  char G[] = {'AA','BB','CC','DD','EE'};
    // Let op dus enkele aanhalingstekens
    char G[] = {'A','B','C','D','E'};
    // Volgende: check of we zonder de lengte door te geven toch door de elementen kunnen gaan van de array
    int H[] = {1,2,3,4,5,6,7,8,9,10};


    // BELANGRIJK: Je moet dus zelf de lengte van een array meegeven bij A[]. Je kan de
    // lengte niet eenvoudig bepalen want eigenlijk geef je een pointer naar een array door
    // ook zoals met een linked list kan dat niet. Daarom heb je een for each loop nodig?
    Display1(A,6);
    // Hier verandert een B in een pointer, dus: je moet alsnog de lengte die in dit geval bekend is,
    // meegeven
    Display1(B,5);
    // Hier maar 5 getallen, en je vraagt er 6 te printen. Uitkomst is geen adres maar een 'garbage' value.
    Display1(C,6);
    // Bij de vector is de omvang al bekend, en kan je gewoon een for each loop gebruiken
    Display2(D);
    // We geven weer een float door. De laatste waarde is niet bekend en geeft weer een garbage value.
    Display3(E,6);
    // We geven dus meerdere strings door, we willen dus de 5 strings printen. Willen we ook nog de letters
    // van iedere string hebben dan gebruiken we dus een for each loop.
    Display4(F,5);
    // Als je had char G[] = {'AQ','BQ','CQ','DQ','EQ'}; dan print hij 5x Q. Dus steeds de laatste letter want char
    Display5(G,5);
    // We geven weer array F door, maar printen nu per karakter
    Display6(F,5);
    // Probeer nu met for each loop elementen te printen, zonder size door te geven: Dat kan dus niet want C maakt
    // er een pointer van. Daarom roepen we deze Display functie gewoon op, zonder parameters mee te geven.
    Display7();
};


