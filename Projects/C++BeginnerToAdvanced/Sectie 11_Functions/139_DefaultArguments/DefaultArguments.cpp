// 2-5-2026: Om verschillende overloaded functions te combineren

// Function overloading: C++ kiest tussen meerdere functies met dezelfde naam op basis van parameters.
// Templates: één functie of class die werkt voor meerdere datatypes door type-generatie tijdens compilatie.
// Default Arguments: Soms 2 parameters, soms 3. Maar dezelfde functie gebruiken.
// Auto gebruiken lijkt erop. Kan vanaf C++20

#include <iostream>
#include <stdlib.h>

using namespace std;

int optellen(int a, int b, int c=0)
{
    return a+b+c;
}

// Als ik deze erbij zou zetten is dit functionoverloading (en dan boven moet je c=0 weghalen)
// int optellen(int a, int b, int c)
// {
//     return a+b+c;
// }

int main()
{
    int a = 5;
    int b = 11;
    int c = 13;

    int answer1 = optellen(a,b);
    int answer2 = optellen(a,b,c);

    cout<<"uitkomst met 2 parameters: " <<answer1<<endl; 
    cout<<"uitkomst met 3 parameters: " <<answer2<<endl; 

    return 0;

};    

