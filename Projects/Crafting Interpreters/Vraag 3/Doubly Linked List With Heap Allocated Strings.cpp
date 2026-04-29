// Vraag 2: Get a “Hello, world!” program written and running in Java. Set up whatever
// Makefiles or IDE projects you need to get it working. If you have a debugger, get
// comfortable with it and step through your program as it runs.

// Do the same thing for C. To get some practice with pointers, define a doubly-linked
// list of heap-allocated strings. Write functions to insert, find, and delete items from
// it. Test them.

// Dus: Schrijf hello world in C. In Heap dus een Linked list maken (volgens mij altijd)
// En dan zou ik zeggen: het dataveld van de linkedlist is een string (dus in de struct een string 'waarde' ipv
// een int 'waarde')

#include <stdlib.h>
#include <iostream>

using namespace std;

struct Node
{
    string Woord;
    Node* volgende;
    Node* vorige;
};

// head moet hier naar verwijzen.


int main()
{
    /
}