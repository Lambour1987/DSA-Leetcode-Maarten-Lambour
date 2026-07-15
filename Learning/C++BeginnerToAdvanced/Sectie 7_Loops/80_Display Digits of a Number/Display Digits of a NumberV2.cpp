//26-4-2026: Op deze manier, kan het niet. Dus: wat ik hier doe is
// zonder '/' werken maar wel iedere keer de 'i' verhogen *10.

#include <iostream>
#include <stdlib.h>

using namespace std;


int main()
{
    int getal;
    cout<<"voer getal in: "<<endl;
    cin>>getal;
    int uitkomst;
    int i = 10;
    while(getal%i)
    {
        uitkomst = getal%i;
        cout<<"oorspronkele getal was : "<<getal<<" uitkomst is "<<uitkomst<<endl;
        i = i *10;
        cout<<"De modulus is : "<<i<<"%"<<endl;
    }
    return 0;
}