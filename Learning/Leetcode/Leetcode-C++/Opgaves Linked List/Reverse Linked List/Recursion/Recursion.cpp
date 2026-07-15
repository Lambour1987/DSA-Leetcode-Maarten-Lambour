//14-4-2026: afmaken of een keer opnieuw doen. Recursie implementatie begrijp ik nog niet

#include <iostream>
#include <stdlib.h>

using namespace std;

struct ListNode
{
    int waarde;
    struct ListNode *volgende;
    ListNode(): waarde(), volgende(){};
    ListNode(int x): waarde(x), volgende(){};
    ListNode(int x, ListNode*volgende): waarde(x), ListNode(volgende){};

}


class Soluction
{
    public:
    {
        Listnode* ReverseList(ListNode*head)
        {

            // Basisgeval: Lijst is leeg (dit is dus de basecase)
            // Dus Basecase 1) Lege lijst, Basecase 2) Einde lijst
            // BELANGRIJK: We laten Head door de lijst heenlopen
            if(!head)
            {
                return nullptr;
            }

            //BELANGRIJK: newhead beweegt niet: We Initialiseren
            //hem hier gewoon. En dit zou technisch gezien ook gewoon
            // op ListNode*newhead = nullptr: kunnen zijn. Vraag ChatGPT
            // Maakt code veiliger en leesbaarder en vorokomt uninitialized variable issues/
            // We gebruiken newHead pas aant einde van de recursie
            ListNode * newhead = head;
            
            // Hier gaan we met head door naar het einde (basecase 2)
            // Belangrijk: dus hier kijken of Volgende Node bestaat, 
            // niet (if !head)
            if(head->next)
            {
                // Hiermee roepen we recursief steeds ReverseList op
                // De uitkomst slaan we op in NewHead 
                NewHead = ReverseList(head->next);

                // BELANGRIJK: Vanaf hier gaan we TERUG uti de recursie
                // Koppel het volgende element terug naar het huidige element
                head->next->next = head;

            }
            // nog doen
            head->next = nullptr;
           
        // nog doen
        return newHead;

        }
    }
};

int main()
{
    // Nodes aanmaken op heap
    ListNode k1 = new ListNode;
    ListNode k2 = new ListNode;
    ListNode k3 = new ListNode;
    ListNdoe k4 = new ListNode;


}

