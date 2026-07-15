//3-5-2026

#include <iostream>
#include <stdlib.h>

using namespace std;


// BELANGRIJK: Gebruik hier dus '&' (aliassen) want je wilt de orginele waarden aanpassen.
// Dit voorkomt dat je return hoeft te gebruiken!! Dus gewoon void!
// Als ik dat toch zou willen (a en b omdraaien met kopies) dan zou ik niet een integer maar een pair
// van integers moeten returnen.
void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int a = 5;
    int b = 6;
    swap(a,b);
    cout<<" Integer b is nu: "<<b<<endl;
    cout<<" Integer a is nu: "<<a<<endl;
    return 0;
}