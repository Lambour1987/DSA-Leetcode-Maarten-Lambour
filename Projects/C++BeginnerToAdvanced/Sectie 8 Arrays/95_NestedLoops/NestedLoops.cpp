// 28-4-2026: dus eigenlijk een 2d array
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int i;
    int j;
    for(i=0; i<3;i++)
    {
        cout<<endl;
        for(j=0;j<=3;j++)
        {
            cout<<i<<j<<" ";
        }
    }
}