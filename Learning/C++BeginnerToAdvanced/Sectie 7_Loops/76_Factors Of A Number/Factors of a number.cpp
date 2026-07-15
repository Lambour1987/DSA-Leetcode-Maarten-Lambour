#include <iostream>

using namespace std;

// Geef een getal in, bijv n=8
// 23-4-2026: Optimalisatie is mogelijk (met formule?). Nog doen.
// Hij klopt nog niet helemaal geloof ik.


int main()
{
    int n;
    cout<<"Geef een getal: "<<endl;
    cin>>n;

    // kan ook met while loop
    // Begin met int i=1 anders deel je door 
    for(int i=1; i<n;i++)
    {
        if(n%i==0)
        {
            cout<<"getal "<<n<<" is door "<<i<<" te delen zodat je een hele integer krijgt, namelijk: " << n/i <<endl;
        }
    }
    return 0;
};
