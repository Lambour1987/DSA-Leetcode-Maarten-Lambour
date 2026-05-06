//2-5-2026: nog een keer gedaan: nu proberen met 1 pointer
//2-5-2026: Niet echt lekker nog mara idee begint te komen: nog een keer verbeteren; Abdul Bari geeft
// ook aan dat het zo kan met 1 pointer (2 incl temp)

// 1) Maak een struct node met int data en pointer naar struct node. Wijs een eerste, tweede, derde pointer toe;
// 2) Creeer Linked list:
// 2.1) We maken een Last pointer en temp pointer aan;
// 2.2) Eerste Node: De eerste pointer moet nu ipv 0 naar heap gaan wijzen om plek te reserveren ter grootte van struct node
// 2.3) Het dataveld moet de waarde uit de array krijgen, de pointer die wijst naar volgende node moet op nul staan
// 2.4) De last pointer moet naar de first pointer wijzen: Last krijgt het adres van First  
// 2.5) Creeer volgende nodes: begin bij node 1 en ga door zolang de input array is
// 2.5.1) Maak voor ieder element uit de array een nieuwe node aan (temp) in 'heap'.
// 2.5.2) Dataveld van temp is elementwaarde, pointer next blijft naar nul;
// 2.5.3) De laatste node moet nu naar temp verwijzen
// 2.5.4) De laatste pointer moet nu naar temp verplaatst worden: Last pointer krijgt adres van Temp    

// 1) Maak een struct node met int data en pointer naar struct node. Wijs een eerste, tweede, derde pointer toe;
struct Node
{
    int data;
    struct Node *next;
}*First;

// 2) Creeer Linked list:
void Create(int ArrayA[], int size)
{
    // 2.1) We maken een Last pointer en temp pointer aan;
    struct Node *Last;
    struct Node *Temp;
    // 2.2) Eerste Node: De eerste pointer moet nu ipv 0 naar heap gaan wijzen om plek te reserveren ter grootte van struct node
    // First = (struct Node*)malloc(sizeof(struct Node))
    First = new Node();
    // 2.3) Het dataveld moet de waarde uit de array krijgen, de pointer die wijst naar volgende node moet op nul staan
    First->data=ArrayA[0];
    First->next=nullptr;
    // 2.4) De last pointer moet naar de first pointer wijzen: Last krijgt het adres van First  
    Last=First;
    // 2.4) De last pointer moet naar de first pointer wijzen: Last krijgt het adres van First      
    for(int i=1; i<size;i++)
    {
        // 2.5.1) Maak voor ieder element uit de array een nieuwe node aan (temp) in 'heap'.
        Temp = new Node;
        // 2.5.2) Dataveld van temp is elementwaarde, pointer next blijft naar nul;
        Temp->data = ArrayA[i];
        Temp->next = nullptr;
        // 2.5.3) De laatste node moet nu naar temp verwijzen
        Last->next=Temp;
        // 2.5.4) De laatste pointer moet nu naar temp verplaatst worden
        Last = Temp;

    }
}

// Probeer met 1 pointer na te gaan of de volgende waarde hoger is zonder pointer te verplaatsen,
// maar door te kijken of 
void InsertSorted(int value)
{
    // Eerst waarde aan temp toevoegen en temp in heap aanmaken
    Node* Temp = new Node;
    Temp->data = value;
    Temp->next = nullptr;
    
    // Maak nieuwe pointer aan: wat ook mag: Node* Current = First;
    struct Node*Current;
    // Wijs huidige pointer toe: Krijg het adres van First
    Current = First;
    
    // Ik zou zeggen gebruik een while loop
    while(Current!=nullptr)
    {
        // Waarde in te voegen = 5. Als de in te voegen waarde (5) groter is dan huidige waarde, maar lager
        // is dan huidig->next waarde. Dan moeten we hier in gaan voegen.
        // Ik had dit maar is onnodig: if(value>Current->data && value< Current->next->data)
        if(Current->next->data>=value)
        {
            // Temp koppelen aan volgende
            Temp->next= Current->next;
            // Huidige koppelen aan temp
            Current->next = Temp;
            return;
        }
        // Verplaats pointer
        Current = Current->next;
    }
}


int main()
{
    int ArrayA[{2,3,4,6,7,8}];
    // Zelf de waarde doorgeven
    Create(ArrayA,6);
    int insert = 5;
    InsertSorted(ArrayA,5);       
}