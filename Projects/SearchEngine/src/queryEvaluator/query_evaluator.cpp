// 13-5-2026
// 15-5-2026: Waarom is nou bijv index niet geimporteerd maar herkent C++ het wel?
// Importeren Token library?


#include <stack>
#include <vector>
#include <unordered_map>
#include <algorithm>

#include "queryParser.h"

using namespace std;

// Functie evaluatePostfix die als input een vector met referenties die niet te wijzigen zijn naar postfix
// een hashmap van strings en vector van integers referentie naar index die we niet mogen wijzigen. Als
// output een vector van integers.
vector<int> evaluatePostfix(const vector<Token>& postfix, const unordered_map<string, vector<int>>&index)
{
    // maak een stack van vectoren van integers (noem hem stack)
    stack<vector<int>> St;
    
    // voor elk postfixToken in in postfix (noem even anders want we hebben al een 'token')
    // deze variabele heeft daar niets mee te maken
    for(const auto& postfixToken:postfix)
    {
        //Als het tokentype gelijk is aan WORD (uit de struct)
        if(postfixToken.type == TokenType::WORD)
        {
            // push de documenten op de stack waarin we het token value vinden: dus bijv index["apple"] = [1,3,5]
            // Dus apple komt voor in document 1,3,5 en die zetten we op de stack
            // token.value is dus gewoon de tekst.
            St.push(index.at(postfixToken.value));
        }
        // Anders als tokentype gelijk is aan 'AND'
        else if(postfixToken.type == TokenType::AND)
        {
            // Haal de twee laatste indices van waarden van de stack om daar AND of OR op toe te passen:
            // haal waarde van stack uit de top en stop deze in een variabele right (auto datatype)
            auto right = St.top(); St.pop();
            // haal waarde van stack uit de top en stop deze in een variabele left (autodatatype)
            auto left = St.top(); St.pop();

            // maak een vector van integers resultaat
            vector<int> result;

            // voor ieder document in links
            for (const auto& doc:left)
            {
                // Zoek of doc voorkomt in de vector right. Niet gevonden. Is iterator einde.
                if(find(right.begin(),right.end(),doc) != right.end())
                {
                // Voeg doc toe aan het resultaat
                    result.push_back(doc);
                }
            }
            // Voeg toe aan stack
            St.push(result);
        }
        // Anders. Dan is het tokentype OR
        else if (postfixToken.type == TokenType::OR)
        {
            // maak een variable right en stop daarin de stack top. Haal daarna het bovenste element van de stack
            auto right = St.top(); St.pop();
            // maak daarna een variabele left en stop daarin de stack top. Haal daarna het bovenste element van de stack
            auto left = St.top(); St.pop();
            // maak een vector van integers genaamd left
            vector<int> result = left;
        // Voor ieder document in right
            for(int doc:right)
            {
                // Als doc niet in resultaat staat, voeg toe aan het resultaat?
                if(find(result.begin(), result.end(),doc)==result.end())
                // Dus == result.end() is hetzelfde als. Dus als het niet in het
                // resultaat staat. Voeg toe aan resultaat. Hashset is misschien makkelijker hier
                // 15-5-2026: Als optimalisatie later hashset toevoegen
                    result.push_back(doc);
            }
            // resultaat toevoegen aan stack
            St.push(result);
        }
    }
    // Return de stacktop
    return St.top();
}