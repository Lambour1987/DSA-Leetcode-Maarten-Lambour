// Linked List

#include <iostream>

using namespace std;

//struct heeft standaard Public members, public schrijven niet nodig.
//struct heeft 3 constructors
struct ListNode
{
    int value;
    ListNode *next;
    //Default constructor: members geinitialiseerd op nul en nullptr
    ListNode() : value(0), next(nullptr) {}
    //Constructor met waarde x, en pointer naar nullptr
    ListNode(int x) : value(x), next(nullptr) {}
    //Constructor met waarde en pointer naar next ipv naar nullptr.
    ListNode(int x, ListNode *next): value(x), next(next) {}

}

class Solution
{
    public:
        ListNode* ReverseList(ListNode*head)
        {
            // we maken een Listnode met een pointer head;
            // we initialiseren 3 pointers: Links, Midden, Rechts
            // we maken een DummyNode
            // er is ook een headNode en eventueel een tailnode maar we veranderen die pas aan het eind?

            // We wijzen de linker pointer toe aan de nullptr
            ListNode *links = nullptr;

            // We wijzen midden en rechter pointer toe aan de head pointer
            ListNode *midden = head;
            

            // Rechts beweegt eerst, dus zolang we niet op een nullptr uitkomen verschuiven we de pointer naar rechts
            while(midden)
            {
                ListNode *rechts = midden->next;
                //Omdraaien: Midden volgende node verwijzen we naar de linkerpointer
                midden->next = links;
                //Verschuif Pointer: Linker pointer verschuiven we naar rechts (waar de middenpointer op staat)
                links = midden;
                //Verschuif Pointer: Midden pointer verschuiven we naar rechts (waar de rechterpointer op staat)
                midden = rechts;
                
            }
            return links;
        }
}

// Helper functie om een lijst te printen
// Waar we bij een array ostream gebruiken doen we hier dus iets anders.

//Functie hoeft niet te retourneren en de input is een poitner naar de eerste node
void printLijst(ListNode* head)
{
    //Zolang we nog niet bij het einde van de lijst zijn, drukken we het waarde-gedeelte
    //van de node af.
    while(head)
    {
        cout<<head->value <<"->";
    }   head = head->next;

    cout<< "nullptr" << endl;
}




int main()
{
    // We gaan de Linked List maken: Nieuwe nodes voegen we toe in heap geheugen met 'New' (in C: malloc)
    // De struct Node heeft een waarde en een value

    ListNode* node4 = {4};
    ListNode* node3 = {3,n4};
    ListNode* node2 = {2,n3};
    ListNode* node1 = {1,n2};

    ListNode* head = n1;

    cout << "Originele lijst: ";
    printList(head);

    Solution sol;
    ListNode* reversed = sol.ReverseList(head);

    cout << "Omgekeerde lijst: ";
    printList(reversed);

    return 0;
}