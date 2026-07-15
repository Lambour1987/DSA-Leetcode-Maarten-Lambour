// 2-5-2026: Function for finding max three numbers

// Function for Finding maximum of 3 numbers
// Write a function for Maximum of 3 Numbers.
// Main is calling a function Max(7,10,5) and you have to implement Max() function
// function should return Maximum of 3 number
// Note: for help you can check solution


// Oplossingen:
// BELANGRIJK: Hier gewoon de if statements want losse integers
// Als het een array was:
// Ook kan Eerst sorteren, dan eerste of laatste getal pakken
// Ook een ingebouwde max
// Of gewoon zelf max bijhouden


#include <iostream>
#include <stdlib.h>

using namespace std;

int FindMax(int a, int b, int c)
{
    if(a>b)
    {
        // a is groter dan b
        if(a>c)
        {
            // a is groter dan c: a is de grootste
            return a;        
        }
        else// a is groter dan b maar kleiner dan c; dan is c de grootste
        {
            return c;
        }
    }
    else // a is kleiner dan b. Dus b of c is de grootste
    {
        if(b>c)// b is de grootste
        {
            return b;
        }
        else // c is grootste
        {
            return c;
        }
    }
    return 0;
}

int main()
{
    int a;
    int b;
    int c;
    cout<<"geef 3 nummers: "<<endl;
    cin>>a;
    cin>>b;
    cin>>c;

    int result = FindMax(a,b,c);
    cout<<result;

    // is overbodig
    return 0;
}