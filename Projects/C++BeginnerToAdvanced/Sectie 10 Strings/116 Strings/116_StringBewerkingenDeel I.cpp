// Zie beneden

#include <iostream>
#include <stdlib.h>

using namespace std;


void Display(string A)
{
    for(char s:A)
    {
        cout<<s<<endl;
    }
}



int main()
{
    // Strings die niet kunnen:
    // 1) Proberen meerdere strings in 1 string te stoppen
    // string A = {"Hello","Ello","Llo","Lo","O"};
    // 2) Nog fouter: Enkele aanhalingstekens:
    // string B = {'Hello','Ello','Llo','Lo','O'};
    // 3) Of met 1 letter mag ook niet
    // string C = {'H'}
    // 4) Mag ook niet:
    // char D = {'H'};

   

    // Denk dus aan: char/string, enkele/ dubbele aanhalingstekens, accolades/ geen accolades, meerdere of enkele
    // letters in een string, meerdere woorden in een string (string of strings)
    
    //Moet:
    char A = 'H';

    // Kan niet, geen dubbele aanhalingstekens
    // char A = "H";

    // Kan niet, want een woord en moet een letter zijn
    // char A = 'Hello';

    // Kan niet, want is een woord + dubbele aanhalingstekens
    // char A = "Hello";

    // Kan niet: want meerdere letters: dit wordt uiteindelijk: char A='O', dus laatste letter
    // char A = 'H','E','L','L','O';

    // Kan niet: want meerdere letters + dubbele aanhalingstekens 
    // char A = "H","E","L","L","O";   

    // Mag wel, maar is onnodig en niet gebruikelijk {} is initialization list
    char B = {'H'};

    // Kan niet: Dubbele aanhalingstekens + accolades
    //char A = {"H"}; 

    // Kan niet: Meerdere letters + accolades
    //char A = {'Hello'};

    // Kan niet: 3 dubbel fout: woord ipv letter, dubbele aanhalingstekens en initialization list
    // char A = {"Hello"};
    
    // Kan niet: Meerdere waarden: Dit is eigenlijk
    // char A = {'H','E','L','L','O'};

    // Kan niet: Meerdere waarden    
    // char A = {'Hello','Ello','Llo','Lo','O'};

    char C[] = {'H','E','L','L','O'};
    
    // Kan niet: 
    //char A[] = {"H","E","L","L","O"};

    // Kan niet:
    // char A[] = 'H','E','L','L','O';

    // Kan niet
    //char A[] = 'Hello'

    // Dit kan weer wel
    // char D[] = "Hello";

    // 29-4-2026: nog voor strings uitwerken


    
    
    
}

