// 28-4-2026: Moet er dus zo uitzien:
// 29-4-2026: Handig. Eigenlijk nog andere varianten verzinnen

// 1 2 3 4 
// 5 6 7 8 
// 9 10 11 12
// 13 14 15 16

// Eigen variatie: geef een getal en maak een n*n matrix met getallen gevuld
// Nog een keer doen

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;
    cout<<"Geef n: "<<endl;
    cin>>n;
    int count = 0;
    
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n;j++)
        {
            cout<<count<<" ";
            count++;
        }
        cout<<endl;
    }
    return 0;
}
