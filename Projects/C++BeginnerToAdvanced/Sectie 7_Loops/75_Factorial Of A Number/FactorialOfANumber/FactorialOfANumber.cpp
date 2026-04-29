//23-4-2026

#include <iostream>

using namespace std;

int main()
{
    int i=1; // iterator start bij 1
    int f=1; // factorial start bij 1
    int t; // target
    cout<<"geef een target getal: "<<endl;
    cin>>t;

    while(i<=t)
    {
        f = f*i;
        cout<<f<<endl;
        i++;
    }
    return 0;
}