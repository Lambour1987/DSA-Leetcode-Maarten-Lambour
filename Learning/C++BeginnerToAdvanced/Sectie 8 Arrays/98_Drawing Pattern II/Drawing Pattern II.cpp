// 29-4-2026: Moet er dus zo uitzien:
//                                  hulp 
//     0   1   2   3                0   1   2   3   
// 0   X                         0  0.0 0.1 0.2 0.3 
// 1   X   X                     1  1.0 1.1 1.2 1.3 
// 2   X   X   X                 2  2.0 2.1 2.2 2.3
// 3   X   X   X   X             3  3.0 3.1 3.2 3.3

// 29-4-2026: nog eens doen. Dus geen while loop want er is een vast
// patroon waarin je print: we weten van te voren hoe vaak we printen:
// Beter Doe meteen alles in 1 programmaatja (alle row en column major)    

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;
    cout<<"geef n: "<<endl;
    cin>>n;

    // Patroon 1
    for(int i = 0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(j<=i)
            {
                cout<<"X"<<" ";
            }
        }
        cout<<endl;
    }

    //Patroon 2
    for()

    return 0;
};
