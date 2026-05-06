// 2-5-2026: Function Overloading for Min of Numbers
// Function Overloading for Min of Numbers
// Write Overloaded Functions for finding Minimum of numbers.
// implement following functions
// 1. Minimum of 2 integers
// 2. Minimum of 3 integers
// 3. Minimum of 2 floats

// Let dus op: bij bepalen van minimum kan je maar 2 getallen doorgeven niet meer (dit is anders dan bij een array)


#include <iostream>
#include <stdlib.h>
#include <algorithm> // schijnbaar alleen voor floats nodig

using namespace std;

int minimum(int a, int b)
{
    // ternary operator als zijn dus de haakjes, en ? betekent dan a. en : b
    return (a < b) ? a : b;

}

int minimum(int a, int b, int c)
{
    // Hier dus een geneste min
    return min(min(a,b),c);
}

float minimum(float a, float b)
{
    return (a<b)?a:b;
}

int main()
{
    int a=6;
    int b=11;
    int c=4;
    float d= 1.29;
    float e= 3.67;
    int uitkomst1 = minimum(a,b);
    int uitkomst2 = minimum(a,b,c);
    float uitkomst3 = minimum(d,e);
    cout<<"Het minimum uitkomst 1 is:"<<uitkomst1<<endl;  
    cout<<"Het minimum uitkomst 2 is:"<<uitkomst2<<endl;  
    cout<<"Het minimum uitkomst 3 is:"<<uitkomst3<<endl;  

    return 0;

};
