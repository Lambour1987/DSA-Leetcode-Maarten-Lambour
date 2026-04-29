//24-4-2026: Nog een keer opnieuw. Het werkt maar kan dus sneller: Je hoeft maar tot wortel n te gaan
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int nummer;
    cout<<"Geef een nummer op om te bepalen of het een priemgetal is "<<endl;
    cin>>nummer;
    int count = 0;//tel het aantal priemgetallen
    // Zou er een efficientere methode zijn?
    // Als het getal 2 tot n modules ergens een nul bevat is het geen prime nummer
    for(int i=2; i<nummer;i++)
    {
        if(nummer%i==0)
        {
            cout<<"Getal "<<nummer<<" is geen priemgetal. Want "<<nummer<<" / "<<i<<" = "<<nummer/i<<endl;
            count++;
        }
    }
    if(count==0)
    {
        cout<<"Getal "<<nummer<<" is een priemgetal "<<endl;
    }
        
    return 0;
};