#include <iostream>

using namespace std;


// De vraag: nu roep ik functies op allemaal in main, maar ik kan binnen de functies ook functies oproepen.
// zo zien we dat vaak bij swap. maar dat is niet zo netjes denk ik?

int GebruikersVraag()
{
    cout<<"Geef het getal aan tot en met hoe ver u door wilt gaan: ";
    int aantal;
    cin>>aantal;
    return aantal;
}


void SumOfNNaturalNumber(int doorgaantotenmet)
{
    int resultaat = 0;
    for(int i=1; i<=doorgaantotenmet;i++)
    {
        resultaat = i + resultaat;
        cout<<resultaat<<endl;
    }
}

// Deze nog even uitwerken dan
//void Uitkomst

int main()
{
    // Maar ook dit: nu heb ik een aantal als variabele en doorgaantot als variabele maar
    // eigen zou dat er maar 1 hoeven zijn. Zal ik een statische of globale of lokale variabele
    // moeten maken?
    int doorgaantotenmet = GebruikersVraag();
    SumOfNNaturalNumber(doorgaantotenmet);

}