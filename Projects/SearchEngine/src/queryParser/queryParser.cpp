//13-5-2026 Query Parser. Nog geen AST 


#include "queryParser.h"
#include <stack>
#include <vector>

using namespace std;

// functie precedence met als input een referentie naar 'teken' die we niet wijzigen
// en een output int van static: Static: Alleen zichtbaar binnen dit bestand en niet in andere
// cpp files. Je kan er niet naar linken.
static int precedence(const Token&teken)
{
    // switch cases maken. case And return 2, or 1 anders 0. 
    // 'teken' komt uit het struct token (zie tokenizer.h)
    switch (teken.type)
    {
        case TokenType::AND: return 2;
        case TokenType::OR: return 1;
        default: return 0;
    }
}

// maak een statische functie isOperator met als input een referentie naar 'teken' die we niet wijzigen
static bool isOperator(const Token &teken)
{
    //retourneer teken.type als Tokentype AND of OR is
    return teken.type == TokenType::AND || teken.type == TokenType::OR;
}

// Functie toPostfix met als input een referentie naar de vector tokens die we niet aan wijzigen en als output
// een vector Token. Ik denk alas constructor? een vector van token output en een stack van token operatorStack
vector<Token> toPostfix(const vector<Token>&tokens)
{
    // maak een vector van token output
    vector<Token>output;
    // maak een stack van tokens operationStack
    stack<Token>operationStack;
    // voor iedere referentie die we niet veranderen naar teken in tokens
    for(const auto&teken:tokens)
    {
        //Als het teken geen Operator is
        //waarom geen teken.isOperator()? ofzo
        if(!isOperator(teken))
        {
            //voeg aan output vector het teken toe
            output.push_back(teken);
            //ga door;
            continue;
        }
        // Zolang de stack (operationStack) niet leeg is en de top gelijk is of groter aan 
        // aan de huidige operator. Dan van de stack af halen en in output zetten
        
        // Zolang de stack niet leeg is
        while (!operationStack.empty() 
        // En bovenste element van de operationStack een operator is (roep functie op)
        && isOperator(operationStack.top())
        // En de top van de operationStack groter of gelijk is aan het huidige teken
        // "De waarde" van AND is hoger dan OR. Vandaar.
        && precedence(operationStack.top())>= precedence(teken))
        {
            //Voeg de top operationStack toe aan aan output
            output.push_back(operationStack.top());
            // Haal top eraf
            operationStack.pop();
        }
        // Push op de operationstack het teken
        // Push je huidige teken er weer op
        operationStack.push(teken);
    }
    // Zolang operationStack niet leeg is
    while(!operationStack.empty())
    {
        // Voeg aan de output de top van operation stack toe
        output.push_back(operationStack.top());
        // Haal top eraf
        operationStack.pop();
    }
    //Retourneer output
    return output;
}