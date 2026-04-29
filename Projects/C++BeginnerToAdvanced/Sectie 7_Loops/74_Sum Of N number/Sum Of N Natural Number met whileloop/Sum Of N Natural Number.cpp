// 23-4-2026: 

#include <iostream>

using namespace std;

int main()
{
    int getal;
    int sum = 0;
    int i=1;
    cout<<"Geef een getal: "<<endl;
    cin>>getal;

    while(i<=getal)
    {
        sum = sum + i;
        i++;
        cout<<sum<<endl;
    }
    // als we cout<<sum<<endl; hier zetten krijgen we 1x de output (45)
    return 0;
};