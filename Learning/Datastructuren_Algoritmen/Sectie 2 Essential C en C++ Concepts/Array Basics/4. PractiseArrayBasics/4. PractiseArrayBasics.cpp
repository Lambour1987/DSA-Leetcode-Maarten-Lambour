//13-4-2026: nog een keertje netjes maken
#include <iostream>

using namespace std;


int main()
{
    // 4 bytes for integer
    // 1 byte: 8 bits. Dus integer kan aannemen
    // -2^31 tot +2^31-1
    // -2,147,483,648 tot 2,147,483,647

    int A[5];
    A[0]=12;
    A[1]=15;
    A[2]=25;

    int B[] = {2,4,5,6,7};
    int C[8] = {2,4,5,6,7};
    
    // Minder kan niet
    // int D[4] = {2,4,5,6,7};

    // 5 integers * 4 bytes = 20
    // Met sizeof printen we de omvang
    // endl is newline;
    cout<<sizeof(A)<<endl;

    cout<<A[1]<<endl;
    cout<<"We printen B dat is "<<B<<endl;
    cout<<"We printen C dat is "<<C<<endl; 

    // We printen A, A[4] is binnen bounds, maar niet
    // Geinitialiseerd dus uitkomst garbage(random)
    cout<<"We printen een element A: "<<A[4]<<endl;

    // B printen met out of bounds: Uitkomst 32758: dat is de waarde
    // Die in dat stuk geheugen staat
    cout<<"We printen een element B met out of bounds: "<<B[5]<<endl;
    cout<<"We printen een element C: "<<C[3]<<endl;

    //printf kan ook
    printf("%d\n", A[2]);

    return 0;
}


// Wat kan je nog meer zetten:
// A[7] = {2,4,5,6,7,8,10}
// A[10] = {2,4,5,6,7,8,10}
// A[5] = {}