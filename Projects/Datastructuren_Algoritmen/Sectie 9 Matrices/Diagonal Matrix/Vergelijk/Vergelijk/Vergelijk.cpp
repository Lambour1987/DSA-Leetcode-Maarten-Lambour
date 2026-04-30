//30-4-2026: vergelijk met dit; 
// Deze even opnieuw gedaan: komt uit de andere cursus.
// Kan weg 

#include <stdlib.h>
#include <iostream>

using namespace std;


// Let op: Als je de accolades weghaalt krijg je een ander resultaat
int main()
{
    int i;
    int count=0;
    for(int i=0; i<5;i++)
    {
        for(int j=0; j<5;j++)
        {
            count++;
            cout<<count<<" ";
        }
        cout<<endl;
    }
}