// 3-5-2026


#include <iostream>

using namespace std;

// niet de getallen a en b worden gekopieerd, maar de adressen van a en b.
// Dus bij reference krijg je de variabelen zelf, bij value een kopie en bij address het adres.
// BELANGRIJK: Gebruik pointers alleen als reference of kopie niet toereikend zijn.
// Bijv. bij linked list.
void swap(int*a, int*b)
{
    cout<<"Binnen de swapfunctie voorafgaand uitvoeren swap is de uitkomst van a: "<<*a<<endl;
    cout<<"Binnen de swapfunctie voorafgaand uitvoeren swap de uitkomst van b: "<<*b<<endl;

    int temp = *a;
    *a = *b;
    *b = temp;
    cout<<"Binnen de swapfunctie na uitvoeren swap is de uitkomst van a: "<<*a<<endl;
    cout<<"Binnen de swapfunctie na uitvoeren swap is de uitkomst van b: "<<*b<<endl;
}


int main()
{
    int a = 7;
    int b = 8;
    swap(&a,&b);
    cout<<"Binnen de mainfunctie is de uitkomst van a: "<<a<<endl;
    cout<<"Binnen de mainfunctie is de uitkomst van b: "<<b<<endl;

    return 0;
}