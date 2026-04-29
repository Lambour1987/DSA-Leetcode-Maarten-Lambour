// 23-4-2026: Perfect Number

// 24-4-2026: Dit kan sneller: dit is denk ik een leetcode dus daar uitwerken
// Ook nog in for loop uitwerken

// Dus opnieuw de factoren van een nummer bepalen
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int nummer;
    cout<<"geef een nummer: "<<endl;
    cin>>nummer;
    int i=1; //Dus initialiseer omdat we het in een while loop willen zetten
    int bedrag = 0;
    int som = 0;
    
    while(i<nummer)
    {
        if(nummer%i==0)
        {
            bedrag = nummer/i;
            cout<<"de integer is:"<<bedrag<<endl;
            som = som+i;
            cout<<"de som is: "<<som<<endl;
        }
        i++;
        
    }
    if(som==nummer)
        {

            cout<<"De som is "<<som<<" en het nummer is "<<nummer<<" Het gaat om een perfect nummer"<<endl;
        }
        else
            cout<<"De som is "<<som<<" en het nummer is "<<nummer<<" Het is geen perfect nummer"<<endl;


    return 0;
};