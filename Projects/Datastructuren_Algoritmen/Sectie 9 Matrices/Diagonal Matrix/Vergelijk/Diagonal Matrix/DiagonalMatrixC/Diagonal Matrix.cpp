//30-4-2026: bestandsnaam is wel cpp maar volgens mij college in C. 
// Overigens deze zelf gemaakt.

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int Array[5][5] = {{1,0,0,0,0},{0,7,0,0,0},{0,0,13,0,0},{0,0,0,19,0},{0,0,0,0,25}};
    int i;
    int j;
    // cout<<"geef een getal n "<<endl;
    // cin>>n;

    for(i=0; i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            cout<<Array[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;

    cout<<"De diagonale getallen zijn:"<<" ";
    for(i=0; i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            if(i==j)
                cout<< Array[i][j]<<" ";
        }
    }
}