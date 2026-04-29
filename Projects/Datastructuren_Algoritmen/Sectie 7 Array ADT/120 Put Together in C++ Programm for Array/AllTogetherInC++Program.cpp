// Doel: De class array schrijven met alle mogelijke operations die Abdul Bari gegeven heeft.
// Zonder classes moeten we voor iedere methode iedere keer de parameters meegeven. Dat is
// nu niet nodig want die zijn nu in private al gegeven.
// Je stopt data + functies in een class zodat je meerdere objecten kunt maken, 
// en elk object beschikt over dezelfde methoden om zijn eigen data te beheren.

// 21-4-2026: sommige functies nog bouwen

#include <stdlib.h>
#include <iostream>
#include <unordered_set> // t.b.v. eigen uitwerkingen

using namespace std;


// Doen:
// Class array schrijven met pointer naar Array, size en length en maak deze aan in de heap.
// In deze private een forward declartion swap
// Maak 2 constructors: Default (10 elementen) & Parameterized (kies zelf)
// Maak een destructor
// Member Function Declarations: Display, Append, Insert, Delete, LineairSearch, BinarySearch, Get, Set
// Max, Min, SUM, Avg, Reverse, Reverse2, InsertSort,
// isSorted, Rearrange, Merge (2 arrays),
// Union (2 arrays), Difference(2 arrays),
// Intersection (2arrays)


class Array
{
    // Private: dus niet benaderbaar van buiten de class: dus we kunnen
    // De arrays niet oproepen. Wel kunnen we de constructor oproepen
    private:
        // Pointer A verwijst naar een integer op de heap
        int *A;
        int size;
        int length;
        void swap(int *x, int *y);
    public:
    // Constructor: op te roepen
    // Bij listnode: LijstKnoopPunt(): waarde(), volgende(nullptr) {};
    // Hier: aanmaken array met size 10 en lenght 0. Let op 'A = new int[size]' 
    // moet achteraan staan.
        Array()
        { size=10; length=0; A = new int[size];}

    // Constructor aanmaken met zelf in te voeren size
        Array(int size)
        { size=size; length=0; A= new int[size];}

    // Destructor
        ~ Array()
        {
            delete []A;
        }
    // Binnen public geven we aan welke functies we gaan maken die vallen onder de
    // class array. Dit zijn dus geen Forward Declarations (hoewel we wel van te voren aangeven
    // dat het gaat om functies die we moeten beschrijven). Verschil: Deze vallen binnen de class
    // dus zijn Member Function Declarations. Het gaat om Display, Append, Insert, Delete, LineairSearch, BinarySearch, Get, Set
    // Max, Min, SUM, Avg, Reverse, Reverse2, InsertSort,
    // isSorted, Rearrange, Merge (2 arrays),
    // Union (2 arrays), Difference(2 arrays),
    // Intersection (2arrays)
    void Display();

    // Voor append: Geen vector teruggeven maar gewoon void
    void Append(int waarde);
    // Bij Insert willen we op een index een waarde invoeren
    void Insert(int index, int waarde);
    // Bij Delete willen we op een index een waarde verwijderen (dus niet eerst zoeken naar de waarde)
    int Delete(int index);
    int LineairSearchV1(int waarde);
    int LineairSearchV2(int waarde);    
    int BinarySearch(int waarde);
    int RBinarySearch(int waarde);
    int Get(int index);
    void Set(int index, int waarde);//geen waarde teruggeven, zoals bij Get
    int Max();
    int Min();
    int Sum();
    // Geen aparte telfunctie zoals bij LL: want dat is al lengte
    float Average(); // Geen parameters meegeven
    void ReverseV1(); // uit oefeningen: Auxiliry Array
    void ReverseV2(); // uit oefeningen: In-Place
    void ReverseV3(); // uit oefeningen: In-Place maar ik gebruik een while loop
    void ReverseV5(); // zelf gemaakt: is omgekeerd printen, geen reverse
    void ReverseV6(); // zelf gemaakt: is recursief omgekeerd printen, geen reverse
    void LeftShift(); // zie college 110 van Abdul Bari: deze nog uitwerken! geen pdf 
    void RightShift(); // idem
    void RotateLeft(); // idem
    void RotateRight(); // idem
    void InsertSort(int waarde); // zie college 112
    int isSortedV1(); // Dus met int en geen bool
    int isSortedV2 (); // Mijn uitwerking, check met vorige ipv check met volgende
    void ReArrange();

    // Met Merge, Union, Difference en Intersection geven terug een pointer naar een array in Heap
    // Dit is de klassieke methoden. In Modern C++ zouden we ook een vector<int> kunnen gebruiken.
    Array* Merge(Array arr2);
    Array* SetUnionV1(Array arr2); // Uitwerking c.f. bord: gaat om ongesorteerde arrays
    Array* SetUnionV2(Array arr2); // Eigen uitwerking met hashset op ongesorteerde arrays
    Array* SetUnionV3(Array arr2); // Uitwerking c.f. pdf: gaat om gesorteerde arrays: Merge
    Array* SetDiff(Array arr2);
    Array* SetInter(Array arr2);

};


// BELANGRIJK: Itt tot C zetten we binnen Display niets tussen haakjes (daar: struct Array arr).
// Dit is omdat de functie werkt op het huidige object. Intern is dit void Display(Array* this).
// Dit betekent:
// Display(&arr);
//this->A
// this->length
// this->size

void Array::Display()
{
    // Volledige array doorgaan om de elementen te printen
    cout<<"De elementen in de array zijn"<<endl;
    for(int i=0; i<length;i++)
    {
        cout<<A[i]<<" ";
    }

}

void Array::Append(int waarde)
{
// we voegen de waarde (waarde) toe aan het einde van de array (array.length+1)
// Als de lengte de waarde niet overstijgt
    {
        // we hoeven niet array.length of array->length te doen omdat we al in het
        // object zitten zoals in C. Dus gewoon length<size.
        if(length<size)
        {
            // Dan de waarde invoeren op de eerstvolgende lege index van de array
            // Dus als array[0]=11, array[1]=12,array[2]=13, array[3]=14. Dan is de
            // lengte 4 en bevinden we ons op index 3. We willen invoegen op index 4.
            // De index is gelijk aan de lengte dus we voegen gewoon toe op 'lengte'.
            A[length] = waarde;
            // Daarna verhogen we de lengte want die wordt niet automatisch meegerekend.
            length = length+1; //of length++ of ++length of length =+1;
        }
    }
};

void Array::Insert(int index, int waarde)
{
    // Als we een waarde willen invoegen op een index, dan moeten alle elementen rechts
    // van de index naar rechts geschoven worden zolang de array nog ruimte heeft.

    // Eventueel naar links schuiven en naar rechts schuiven als aparte helper functies doen

    // Eerst controleren of de array nog ruimte beschikbaar heeft
    // En controle of de door de gebruiker ingevoerde index niet onder 0 lig of niet boven de lengte
    // We werken weer met member van een class dus A->lengt of A.length niet nodig
    if(index>=0 && index<=length && length<size)
    {
        // Net als met vergelijken doen we hier ook: Huidige min vorige A[i]-A[i-1]
        // A[0]=5, A[1]=3, A[2]=4, A[3]=leeg. Lengte is dus 3. We moeten dus alle
        // elementen van links naar rechts halen totdat we bij de op gegeven index zijn.
        // Stel we willen 7 invoegen op index 1. Dan moeten we dus op de 4e positie, dat is
        // lengte +1, dat is dus op index 3. Dat is lengte.
        
        for(int i = length; i > index; i--)
        {
            A[i]=A[i-1];
        }
        // Als we bij de index komen stoppen we daar de waarde in
        A[index]=waarde;
        // En vergeet dus niet de lengte op te hogen
        length +=1;

    }

}

// Bij deleten willen we dus de waarde op een index verwijderen. Niet eerst
// zoeken en verwijderen.

int Array::Delete(int index)
{
    // Ook hier weer kijken of de index niet leeg is
    // Ook controle of index niet hoger is dan lengte.
    if(index < 0 || index >= length)
    {
        cout<<"verwijderen niet mogelijk"<<endl;
        return -1;
    }

    // We deleten 1x
    int deleted = A[index];
    // A[0]=5, A[1]=3, A[2]=4, A[3]=7 A[4]=leeg. Lengte is dus 3. We willen A[1]=3 verwijderen.
    // Dan moeten alle elementen vanaf A[3]=7 (is lengte 4) naar links geschoven worden.
    for(int i = index;i<length;i++)
    {
        A[i] = A[i+1];
    }
    
    // Hier uiteindelijk de lengte inkorten
    length--;

    return deleted;
}

// Swap is een private functie (helperfunctie hier). Die gebruiken we binnen andere functies.
// We swappen hier de waarden van de geheugenadressen, niet van de elementen of indices van de array.
void Array::swap(int *x, int *y)
{
    // Dus let even op in vergelijking met Linked List: Maak temp aan. x is waarschijnlijk eerste,
    // y tweede variabele. Eerste variabele x naar temp. Tweede variabele y naar x. 
    // temp naar y. Cirkel rond. temp<-eerste<-tweede<-temp;
    int temp = *x;
    *x=*y;
    *y=temp;

}

// Hier dus: Zoek waarde, geef index terug. 
// Bij deleten: Zoek index, geef waarde terug (en delete)
// For each loop kan ook en is handiger?

int Array::LineairSearchV1(int waarde)
{
    for(int i=0; i<length;i++)
    {
        if(waarde==A[i])
        {
            // waarde gevonden
            return A[i];
        }
        else
        {
            // waarde niet gevonden
            return -1;
        }
    }
}


// 20-4-2026: Nog even checken met dat Swap> Chat eruit
// Nu array met swap schrijven (indien je herhalend gaat zoeken)
// Hier heb je niks aan met met binary search
int Array::LineairSearchV2(int waarde)
{
    for(int i=0; i<length;i++)
    {
        if(waarde==A[i])
        {
            // waarde gevonden: We swappen nu. Let op het gaat
            // om referenties. Dit kan ook swap[&A[0], &A[i]];
            swap[&A[i], &A[0]];
            return 0;
        }
    }
    // waarde niet gevonden
    return -1;
}

// 20-4-2026 Probeer ter oefening eens een Recursive Lineair Search te schrijven.


// Binary Search.
int Array::BinarySearch(int waarde)
{
    int links,midden,rechts;
    
    links=0;
    //Dus: hier geen arr.length of arr->length?
    rechts=length-1;
    
    

    // Zolang links niet groter is dan rechts
    while(links<=rechts)
    {
        //Bereken mid: voorkom integer overflow d.m.v.
        // Midden = Links   + ((Rechts-Links)/2) of;
        // Midden = Rechts  - ((Links+Rechts)/2)
        midden = links + (rechts-links)/2;
        
        // Hier dus wel weer 'A' want het gaat om het object A? 
        if(waarde==A[midden])
        {
            // Geef terug de index
            return midden;
        }
        else if(waarde<A[midden])
        {
            links = midden + 1;
        }
        else // Als waarde hoger dan het midden ligt
        {
            rechts = midden - 1;
        }
        return -1;
    }

}

// 20-4-2026: Probeer eens een Binary Search op basis van de waarden te doen ipv indices

int Array::Get(int index)
{
    if(index >= 0 && index < length)
        return A[index];
}

void Array::Set(int index, int waarde)
{
    if(index >= 0 && index <length)
    {
        A[index]==waarde;
    }
}

int Array::Max()
{
    // Als startwaarde nemen we het eerste getal uit de array
    // BELANGRIJK: Vergelijk met INT32_MIN gebruiken
    
    int max = A[0];

    for(int i=1; i<length;i++)
    {
        if(max>A[i])
        {
            max = A[i];
        }
    }
    return max;
}


// Voor minimum nog doen en
// 20-4-2026: maar eens een min en max die start vanaf achteraan (denk aan LL recursief)

// Hier gebleven

// Som berekenen
int Array::Sum()
{
    int sum = 0;
    // Stel: getallen index 0 t/m 4 gevuld. Dan is lengte 5.
    // Dan doorloop je tot en met 4. Dat is kleiner of gelijk aan 5 - 1 of
    // kleiner dan 5.
    // Beter hier eigenlijk dus i<length

    for(int i=0; i<=length-1;i++)
    {   
        sum = sum + A[i];
    }
    return sum;
}


// BELANGRIJK: We hebben een class geschreven. De functies lengte en som behoren bij het object.
// WE hoeven ze dus niet als parameter mee te geven.
float Array::Average()
{
    // Wat als nul
    if(length==0)
    {
        return 0;       
    }
    // Let op, kan niet: want Sum is int, en lengte ook. Dus omzetten naar float heeft
    // geen zin: float average = Sum()/length;
    // Dus:
    {
        // Blijkbaar dus tussen haakjes
        return (float) Sum()/ length;
    }
}

// Reverse: Auxiliry Array: Dit lijkt veel op een deep copy. echter hier verwijderen we hier de kopie
// weer nadat we die data weer terug naar de oorspronkelijke array hebben gedaan.
// Is dit niet ook een leetcode? en het kan dan sneller geloof ik , zonder extra array

// Weer geen parameters nodig, want data zit al in het object
void Array::ReverseV1()
{
    //We moeten een nieuwe array maken in heap. We gebruiken C++ dus doen we dit met 'new'
    // Eerst rechts: We maken een nieuwe array van integers aan op de heap ter grootte van de lengte van de array
    // Links: we wijzen met een pointer B naar de de eerste integer van die array.
    // Alternatief: vector<int> B;
    int *B = new int[length];      

    //We lopen vervolgens van achteren naar voren in de oorspronkelijke array en kopieren
    //de elementen naar de nieuwe array. Volgens mij kan dit in 1 for loop
    int links = 0;
    int rechts = length-1;
    // Na de eerste ';'hieronder hoeven we niet aan te geven hoever B gaat. Die stopt vanzelf
    // omdat A stopt.
    for(int links = 0, rechts = length - 1; rechts >= 0; links++, rechts--)
    {
        B[links]=A[rechts];
    }

    //Vervolgens lopen we door de nieuwe array en kopieren weer naar oorspronkelijke array.
    for(int links = 0; links<= length-1; links++)
    {
        A[links]=B[links];
    }
    delete [] B;

}
// Swap met for loop
void Array::ReverseV2()
{
    // Let op, na eerste ';' doen we eigenlijk wat we normaal in een while loop doen
    for(int links=0, rechts=length-1; links<rechts;links++,rechts--)
    {
        swap(&A[links],&A[rechts]);
    }
}


// Swap met while loop
void Array::ReverseV3()
{
    int links = 0;
    int rechts = length-1;
    while(links<rechts)
    {
        swap(&A[links],&A[rechts]);
        links ++;
        rechts --;
    }
        

}

// Geen Reverse maar omgekeerd printen kan natuurlijk door gewoon van achteren naar voren te lopen, maar zou ook
// recursief kunnen door steeds de functie opnieuw op te roepen
void Array::ReverseV4()
{
    for(int i = length-1; i>= 0; i--)
    {
        cout<<A[i]<<" ";
    }

}


// Left Shift: Mijn idee dus i buiten de for loop declareren, zodat die ook na de loop geldig is.
// i Is dan aan het einde. Dat is op A[i]. Dus die zetten we op nul.
void Array::LeftShift()
{
    int i;
    for(i=0; i<length-1;i++)
    {
        A[i]=A[i+1];
    }
    A[i]=0;
}

// Right Shift: volgens de methode officieel. lijkt op mijn methode.
void Array::RightShift()
{
    for(int i=length-1;i>0;i--)
    {
        A[i]=A[i-1];
    }
    A[0]=0;
}




// Nog uitwerken
// void Array::ReverseV5()
// {

// 21-4-2026 Reverse met for each loop kan ook. Nog doen

// Nog uitwerken: Left Shift, Rotate Left, Right Shift, Rotate right. Zie 110 Abdul Bari

// evt Insertion Sort (zie pdf, maar legt nite uit in college)

//Orginele uitwerking
int Array::isSortedV1()
{
    // Hier: nu weer i<length-1; Ik denk omdat we met de volgende element vergelijken
    // Straks: i<length. Mag ook: i<=length-1.
    for(int i=0; i<length-1;i++)
    {
        if(A[i]>A[i+1])
        {
            return 0;
        }
    }
    return 1;
}

// BELANGRIJK: Lees even: want dit dacht ik eerst maar klopt dus niet.
// In tegenstelling tot Insert waar we op een Index een Waarde invullen (gewone Insert)
// Doen we hier binnen een sorted array een waarde invullen.
// Omdat de array gesorteerd is kunnen we het volgende element vergelijken met het huidig
// Als de waarde van het volgende element groter is en de waarde van het vorige element
// kleiner is dan de waarde die we willen invoegen: dan moeten
// we vanaf de volgende locatie ieder element opschuiven, door te beginnen
// aan het einde van de array (er moet wel ruimte zijn) en het vorige
// element daar naar toe kopieren tot we bij de waarde 

// Dus: We starten rechts. We gaan naar links (i--). We verschuiven naar rechts A[i+1].
void Array::InsertSort(int waarde)
{
    int i = length - 1;

    while(i > 0 && waarde < A[i])
    {
        A[i + 1] = A[i];
        i--;
    }

    A[i + 1] = waarde;
    length++;
}


// Dus int teruggeven: Let op ik doe dus if(A[i]>A[i-1])
// Checken of array gesorteert is: doe je dus eigenlijk met 'vergelijk volgende'
// Als die niet gesorteerd is, dan doe je vergelijk huidig met vorige.
// Nog even checken of deze logica klopt...
int Array::isSortedV2()
{
    // Hier weer: i<length. Mag ook: i<=length-1.
    for(int i=1; i<length;i++)
    {
        if(A[i]>A[i-1])
        {
            return 0;
        }
    }
    return 1;
}



//Rearrange: Op basis van conditie: 
// het idee is dat de positieve elementen rechts
// komen te staan en negatieve elementen links.
// Gebruik 2 pointers en swap
// array[]={-6,-8,3,10,5,-7,-9,12,-4,2}
// Wordt uiteindelijk {-6,-4,-8,-9,-7,5,10,12,3,2}
// Ik denk dat dit wel interessant is als je gewoon alle positieve 
// eruit wil halen om dat deel vervolgens te sorteren (het positieve deel)
// Je hoeft ook maar tot de helft te gaan net als bij reverse geloof ik
void Array::ReArrange()
{
    int links = 0;
    int rechts = length-1;
    {
        // We willen tot de helft lopen
        while(links<rechts)
        {
            //Zolang links kleiner is dan nul kunnen we deze overslaan
            while(A[links]<0)
            {
                links++;
            }
            // Zolang rechts groter is dan nul kunnen we deze overslaan
            while(A[rechts]>0)
            {
                rechts--;
            }
            // Omdat we nu al een match hebben gevonden hoeven we niet te doen:
            // A[links]<0 && A[rechts]>0; maar kunnen we doen if(links<rechts)
            if(links<rechts)
            {
                swap(&A[links],&A[rechts]);
            }

        }
    }
// eventueel doen ReArrange met buitenste For Loop

//NOG EEN KEER DOEN
// Merge van reeds gesorteerde arrays
// We hebben als parameter 1 array, namelijk de tweede array. Want de eerste zit al in 'Array::'.
// De tweede array noemen we dan 'B'
// We geven terug een pointer naar een Heap
// Met LL doen we ook nog recursief

    // Met gebruik nieuwe kopie: houd rekening met overgebleven lengte
    // Ik zou zeggen: gebruik 2 while loops: je weet hoe lang de array is, maar de stappen
    // verschillen. We gaan wel de hele array door.
    
    // Als het element in array A kleiner is dan het element in array B.
    // Verplaats element in array A naar array C. Verschuif pointer in A.
    // Anders verplaats element van array B naar array C.
    // Verschuif pointer in B.
    
    // Start met aanmaken nieuwe Array in heap
    // Als lengte A langer is dan lengte B, verplaats de rest van array A
    // Naar array C. Als B langer is dan A, verplaats de rest van array B naar array C.

    // Check of dit klopt; 
    // We moeten beginnen met 

Array* Array::Merge(Array arr2)
{
    int i=0;
    int j=0;
    int k=0;
    // Let op: omdat we de lengte van Array A al in de class hebben staan, hoeven we niet A.length te doen
    // maar gewoon 'length'. arr2 is een object van Array en als parameter meegegeven. Niet in de class.
    // Dus hier wel 'B.length'
    
    // Zelf: arr2 hernoemd naar B;
    Array B = arr2;
    
    // Start met aanmaken in heap: verwijs een pointer C naar een
    // Array. Maak een nieuwe array aan van integers op de heap ter grootte van de lengte
    // van A + de grootte van de lengte van B. 

    // Dit mag ook (boven ook zo gedaan): int* C = new int[length + B.length];
    Array *C = new Array(length+B.length);
    
    //Ga door zolang er nog elementen in beide arrays over zijn
    //Let op: Ik denk dus dat we altijd in de buitenste loop echt over
    //de lengte gaan en de binnenste loop (hier if) over de elementen zelf
    while(i<length && j<B.length)
    {
        if(A[i]<B[j])
            {
                C[k]=A[i];
                i++;
            }
            else
            {
                C[k]=B[j];
                j++;
            }
            k++;
    }


// 23-4-2026: OPNIEUW DOEN    
// Performing Union of 2 sets
// Array A: {3,5,10,4,6}    
// Array B: {12,4,7,2,5}
// Array C: {3,5,10,4,6,12,7,2}
// Dus sorteren niet belangrijk. In de output mogen geen dubbele staan
// BF uitwerking: Kopier Array A naar array C, Bekijk vervolgens in Array B bij ieder element
// of deze bestaat in array C. Als die bestaat, sla over. Bestaat die nog niet. Voeg achteraan 
// C toe. 


// Op ongesorteerde array (bord uitwerking, niet in pdf): Hier is een forloop logischer
// BELANGRIJK: Uitwerking pdf geeft kopie array als parameter. Logischer en netter is het om
// geen kopies te maken dus een referentie te maken '&'. In BEIDE situaties gaat het gewoon
// om een object en verwijzen we ernaar via '.' Dus arr2.lengte en niet arr2->lengte.
// Dat laatste doen we als het gaat om een element op de heap en dan verwijzen we met '*'.

// BELANGRIJK II: In mijn uitwerking is &arr2 dus een referentie naar een object. We kunnen
// niet afleiden of dit object op de heap of op de stack staat.
// Arr3 staat bij mij wel duidelijk op de heap. Want New en *.
Array* Array::SetUnionV1(Array &arr2)
{
    int i = 0;
    int j = 0;
    int k = 0;

    // We maken een nieuwe array aan met de lengte van arr1 en arr2 (rechterdeel)
    // En we verwijzen met een pointer arr3 naar deze array

    Array *arr3 = new Array(length+arr2.lengte);

    // Kopieren van de elementen van array A naar array C
    // We hebben hiervoor gewoon 1 iterator a nodig
    for(i= 0; i<length;i++)
    {
        // arr3 staat in Heap dus verwijs via array pointer. A is onderdeel van de class dus
        // geen verwijzing nodig
        arr3->A[i]=A[i];
    }

    // Nu hebben we een derde array gevuld met elementen A. Vervolgens gebruiken we
    // een iterator k die start vanaf het lege punt in array arr3 (na de elementen van A)
    k = length; // geen +1 nodig en geen verwijzing nodig want length is onderdeel van class

    // Nu hebben we iterator j. Die gaat door array arr2 heen. Start bij het begin.
    // per element moeten we beoordelen of dit element in arr3 staat.
    for(j=0; j<arr2.length;j++)
    {
        //als het element uit arr2 al bestaat in arr3, sla over. Anders
        //voeg toe aan array:
        // Dus roep Search op met parameter j van arr2. Als -1 dan niet gevonden en voeg toe
        if(arr3->LineairSearchV1(arr2.A[j])==-1)
        {
            // Voeg toe aan array 3
            {
                arr3->A[k]=arr2.A[j];
                k++;
            }
            // En anders slaan we over

        }
    }
    arr3->length = k;

    return arr3;

}


// Optimaler: Geen Extra array. Verleng array 1 met lengte arr2: DIT KAN NIET.
// Dus we maken gewoon een nieuwe array.
// Loop door array 1 heen en voeg ieder element toe aan de hashset en aan array 3.
// Als we bij het laatste element van array 1 zijn beginnen we bij array2
// We lopen vervolgens door ieder element van array 2 heen. Als deze al in de hashset
// zit dan voegen we deze niet toe. Als deze nog niet in de hashset zit, voegen we
// deze wel toe aan array 3.

// We beginnen hier weer met een referentie (dus geen kopie maken) van array2.
Array* Array::SetUnionV2(Array &arr2)
{
    // Nieuwe array maken ter grootte van arr1 en arr2
    Array *arr3= new Array(length+arr2.length);

    int i = 0;
    int j = 0;
    int k = 0;
    unordered_set<int>seen;

    // Kopieer ieder element van arr1 naar arr3 en voeg tegelijkertijd toe aan de hashset
    for(i = 0; i<length;i++)
    {
        arr3->A[i]=A[i];
        seen.insert(A[i]); // bij een vector push_back, bij een set insert.
    }

    // start nu in array 2 aan het begin en in array 3 op de lengte (nieuwe index)
    {
        k = length; // de length is van array 1 en daar starten we ook op in array 3

        for(j=0; j<length;j++)
        {
            // als element op positie j van array B niet in de hashset is,
            // voeg deze dan toe aan arr3. 
            // keuze tussen seen.find()==seen.end() en seen.count()
            // seen.count is hier handiger want 0 of 1 als resultaat
            // keuze tussen seen.count()==1 of !seen.count(). Laatste iets overzichtelijker
            if(!seen.count(arr2.A[j])
            {
                arr3->A[k]=arr2.A[j];
            }
        }
    }
    return arr3
};
