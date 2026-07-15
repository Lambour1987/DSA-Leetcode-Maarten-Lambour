// 29-4-2026: 
#include <iostream>
#include <stdlib.h>

using namespace std;

// Ik zou zeggen. Net als bij een gewone integer gebruiken we of '/' of '%' om
// stukken af te hakken en dan zouden we moeten tellen hoe vaak we dat doen.
// Je zou zeggen dat kan misschien omdat letters ook ASCII code zijn.
// BELANGRIJK: Dit kan dus niet!

//Zelf gemaakt
void LettersTellen1(string Word)
{

    int count = 0;
    for(int i=0; i<Word.length();i++)
    {
        count = count + 1;
    }
    cout<<"Het aantal letters volgens eerste methode is "<<count;
}

void LettersTellen2(string Word)
{
    int count = 0;
    for(int i=0; Word[i]!='\0';i++)
    {
        count += 1;
    }
    cout<<"Het aantal letters volgens eerste methode is "<<count;
};



int main()
{
    string Word;
    cout<<"Geef een woord op: ";
    cin>>Word;
    LettersTellen1(Word);


};