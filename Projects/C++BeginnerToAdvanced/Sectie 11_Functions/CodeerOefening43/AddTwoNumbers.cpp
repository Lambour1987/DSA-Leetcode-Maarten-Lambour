// Function for Adding 2 numbers
// Write a function for adding 2 Number.
// you have to write a complete function as explained on white board.
// Main is calling a function add(10,5) and you have to implement add() function
// function should return the result
// Note: for help you can check solution

#include <stdlib.h>
#include <iostream>

using namespace std;

int AddTwoNumbers(int getal1, int getal2)
{
    // int resultaat 0 doen? of getal
    int result = 0;
    // Dus meteen getal1 + getal2
    return getal1+getal2;
}


int main()
{
    int x;
    int y;
    cout<<"Geef nummers: "<<endl;
    cin>>x;
    cin>>y;
    int result = AddTwoNumbers(x,y);
    // BELANGRIJK: We zouden dus het resultaat ook in de functie AddTwoNumbers kunnen weergeven. Dat is
    // geen goede ontwerpkeuze.
    cout<<result<<endl;

};