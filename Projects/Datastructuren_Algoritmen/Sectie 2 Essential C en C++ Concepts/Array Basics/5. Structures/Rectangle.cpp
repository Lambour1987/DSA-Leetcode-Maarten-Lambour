

#include <iostream>
#include <stdlib>

struct Rectangle
{
    int length; //2 bytes
    int breadth; // 2 bytes
    // total 4 bytes, maar nog niet gedeclareerd
    // dus neemt geen ruimte in

}

int main()
{
    // Declartion: occupies 4 bytes
    struct Rectangle r;

    // Declartion + initialization
    // In de stack 
    struct Rectangle s{10,5};
}