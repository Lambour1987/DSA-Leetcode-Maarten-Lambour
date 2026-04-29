//26-4-2026: er is dus nog een snellere methode die modulus gebruikt

#include <iostream>
#include <stdlib.h>

using namespace std;


int main()
{
    int getal1;
    int getal2;
    cout<<"geef getal A: ";
    cin>>getal1;
    cout<<"geef getal B: ";
    cin>>getal2;

    //als getal 1 groter is dan getal 2, trek 2 van 1 af
    while(getal1 !=getal2)
    {
        if(getal1>getal2)
        {
            getal1=getal1-getal2;
            cout<<"getal A is nu "<<getal1<<endl;
        }
        else //als getal 2 groter is dan getal 1, trek 1 van 2 af
        {
            getal2=getal2-getal1;
            cout<<"getal B is nu "<<getal2<<endl;

        }
    }
    cout<<"getal A is "<<getal1<<endl;
    cout<<"getal B is "<<getal2<<endl;

    return 0;
}