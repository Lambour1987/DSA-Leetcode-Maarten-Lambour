// 2-5-2026: Function Template
#include <iostream>
#include <stdlib.h>

using namespace std;

// Dus beide functies zijn hetzelfde alleen de datatypen verschillen. Om te voorkomen dat we vaker
// dezelfde functie moeten schrijven kunnen we beter een template maken.

// int max(int a, int b)
// {
//     return (a>b)?a:b;
// }

// float max(float a, float b)
// {
//     return (a>b)?a:b;
// }

// Dus beter doen: dus zet neer template<class T> en dan de datatype wijzigen naar t
template<class T>
T max(T a, T b)
{
    return (a>b)?a:b;
}


int main()
{
    // int a=2;
    // int b=3;
    // float c=2.25; // je kan dus ook decimalen neerzetten terwijl datatype int is. Dan neemt die uiteraard 'int'
    // float d=3.31;

    // int uitkomst1 = max(a,b);
    // float uitkomst2 = max(c,d);
    // T uitkomst1 = max(a,b);
    // T uitkomst2 = max(c,d);
    cout<<"uitkomst 1 : "<<uitkomst1<<endl;
    cout<<"uitkomst 2 : "<<uitkomst2<<endl;
    cout<<max<<(12,14)<<endl;
    
    return 0;
}