//23-4-2026
#include <iostream>

using namespace std;

// Dus int main en niet void main. Want aan het einde van het programma moet main retourneren
// aan windows.
int main()
{
    int n;
    cout<<"Geef een getal"<<endl;
    cin>>n;
    int resultaat = (n*(n-1))/2+n;
    cout<<"Het resultaat is: "<< resultaat;
    return 0;
};