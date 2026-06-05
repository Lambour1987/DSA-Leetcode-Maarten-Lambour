//4-6-2026 ASTEvaluator

#include <iostream>

// Voeg ASTEvaluator.h toe 
#include "ASTEvaluator.h"
// begin weer met de functie evaluateAST
// (parameters node en index). Als output een set van strings.
// gebruik weer die alias Inverted index
std::unordered_set<std::string> evaluateAST(ASTNode* node, const InvertedIndex& index)

{
    // Als er geen node is return .
    // Alternatief: if(!node)
    if(node == nullptr)
    {
        return {};
    }

    // We werken hier met if statements: dat is hier logisch omdat je werkt met een node->type
    // Dat is puur branching logic. Kan wel met switch cases maar in AST evaluators if. Met commands
    // kan ook maar dat is overkill? Daar is AST te klein voor nu.
    
    //
    //  =====  TERM =====
    //
    // Als node type TERM is 
    // Vergelijk dit weer met type == NodeType::NOT en postfixToken.type == TokenType::WORD
    if(node->type==NodeType::TERM)
    {
        //4-6-2026: Test
        std::cout << "TERM VALUE: " << node->value << std::endl;

        // Zoek in de index de waarde op van de node en stop deze in een variabele it (auto)
        auto it = index.find(node->value);
        // Vervolgens: als it niet gevonden is: end is de iterator die 1 positie voorbij het laatste element
        // staat. 'End' kan je gebruiken omdat index een set is
        if(it!=index.end())
        {
            // retourneer het second deel val it (want it is een...)
            return it->second;
        }
        // Return leeg
        return {};
    }

    //
    // =====   AND =====
    //
    // Als node type AND is
    if(node->type==NodeType::AND)
    {
        //roep evaluateAST functie op met parameter linkernode en index en sla op in left
        auto left = evaluateAST(node->left, index);
        //roep evaluateAST functie op met parameter rechternode en index en sla op in right
        auto right = evaluateAST(node->right, index);
        //maak een set van strings genaamd resultaat
        std::unordered_set<std::string> result;
        //voor ieder document in left
        for(const auto&doc:left)
        {
            // Als document doc ook in de rechter verzameling zit, voeg het dan toe aan het resultaat.
            if(right.count(doc)) 
            {
                result.insert(doc);
            }
        }
        // retourneer resultaat
        return result;
    }
    //
    // ===== OR =====
    //
    // Als node type OR is
    if (node->type==NodeType::OR)
    {
        // roep evaluateAST functie op met parameter linkernode en index en sla op in left
        auto left = evaluateAST(node->left, index);
        // roep evaluateAST functie op met parameter rechternode en index en sla op in right
        auto right = evaluateAST(node->right, index);
        // alle elementen uit van de rechterset in de linkerset
        left.insert(right.begin(), right.end());
        // returneer links
        return left;
    }
    //
    // ===== NOT =====
    //
    // als Node type NOT is
    if (node->type==NodeType::NOT)
    {
        // roep evaluateAST functie op en parameter met parameter rechternode en index en sla op in child
        // 4-6-2026: auto child = evaluateAST(node->left, index); wordt right. Dit heeft te maken met dat
        // NOT altijd maar 1 branch heeft, namelijk zijn tegenovergestelde.
        auto child = evaluateAST(node->right, index);
        // maak een set van strings voor allDocs
        std::unordered_set<std::string> allDocs;
        // voor linker en rechterdoc in de index
        for(const auto& [word,docs]:index)
        {
            //Voeg alle documenten toe aan allDocs
            //4-6-2026: Was eerst: allDocs.insert(allDocs.begin(), allDocs.end()); gewijzigd naar:
            for(const auto&doc: docs)
            {
                allDocs.insert(doc);
            }
        }
        // voor alle documenten in child
        for(const auto& doc: child)
        {
            // Verwijder alle documenten uit allDocs
            allDocs.erase(doc);
        }
        // retourneer allDocs
        return allDocs;
    }
    // return {};
    return {};
}



        
    
