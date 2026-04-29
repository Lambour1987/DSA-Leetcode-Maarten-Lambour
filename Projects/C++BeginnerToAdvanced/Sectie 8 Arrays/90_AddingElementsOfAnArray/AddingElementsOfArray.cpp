// 28-4-2026: Adding All Elements of An Array

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int A[]={4,8,6,9,5,2,7};
    int sum=0;

    for(int element:A)
    {
        sum += element;
        cout<<"Huidige som is: "<<sum<<endl;
    }

    cout<<"De totale som is: "<<sum<<endl;
    return 0;
}