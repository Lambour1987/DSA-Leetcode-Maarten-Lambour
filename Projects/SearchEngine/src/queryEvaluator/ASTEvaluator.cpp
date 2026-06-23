//4-6-2026 ASTEvaluator

#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <cmath>
#include <algorithm>

// Voeg ASTEvaluator.h toe 
#include "ASTEvaluator.h"

using namespace std;
// begin weer met de functie evaluateAST
// (parameters node en index). Als output een set van strings.
// gebruik weer die alias Inverted index

//17-6-2026: Schijnbaar hier de constructor voor de class ASTEvaluator neerzetten
ASTEvaluator::ASTEvaluator(int totalDocs, const unordered_map<string,int>& docLength): totalDocs(totalDocs),docLength(docLength)
{
    this->totalDocs = totalDocs;
    this->docLength = docLength;

    int totalLength = 0;
    
    for(const auto& [doc, len]:docLength)
    {
        totalLength += len;
    }
    if(totalDocs ==0)
    {
        avgDocLen = 1;
    }
    else
    {
        avgDocLen = (double)totalLength / totalDocs;
    }
}

//17-6-2026 En dit stuk dan ook: De BM25 helper
double ASTEvaluator::computeIDF(int N, int df)
{
    if(N==0)
    {
        return 0;
    }
    if(df == 0)
    {
        return 0;
    }
    double val = ((N-df + 0.5)/ (df+0.5))+1;
    
    if(val <=0) return 0;

    return log(val);
}


//17-6-2026: De Evaluator zelf
unordered_map<string, double> ASTEvaluator::evaluateAST(ASTNode* node, const InvertedIndex& index)
{
    // Als er geen node is return .
    // Alternatief: if(!node)
    if(node == nullptr)
    {
        //17-6-2026: van return {}; naar
        return unordered_map<string,double>{};
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
        cout << "TERM VALUE: " << node->value << endl;

        //9-6-2026: Toegevoegd:
        cout << "LOOKUP KEY: [" << node->value << "]" << endl;

        //9-6-2026: Toegevoegd:
        cout << "NODE VALUE RAW: [" << node->value << "] size=" << node->value.size() << endl;

        //16-6-2026: omdat we de index hebben gewijzigd moeten we e.e.a. aanpassen
        //17-6-2026: dus dit wordt ook een map
        //17-6-2026: En nu t.b.v ranking ipv // std::unordered_map<std::string, int>result; 
        // en dit is naar boven veprlaatst
        unordered_map<string, double>result;

        // Zoek in de index de waarde op van de node en stop deze in een variabele it (auto)
        auto it = index.find(node->value);
        // Vervolgens: als it niet gevonden is: end is de iterator die 1 positie voorbij het laatste element
        // staat. 'End' kan je gebruiken omdat index een set is
        //9-6-2026: Ook weer toegevoegd.
        if(it == index.end())
        {
            return {};
        }

        int df = it->second.size();
        double idf = computeIDF(totalDocs, df);

            // weggehaald:
            // std::cout << "DOCS FOR " << node->value << ": ";
        //17-6-2026: gewijzigd van for(const auto& pair : it->second) naar
        for(const auto& [ doc, positions]: it->second)
        {
            //17-6-2026: weggehaald
            // const std::string& doc = pair.first;
            // const std::vector<int>& positions = pair.second;
            
            //17-6-2026: weggehaald
            //std::cout << "DOC" << doc << " POSITIONS: ";
            //nieuw

            double tf = positions.size();
            //17-6-2026 gewijzigd van: double docLen = max(1.0, (double)docLength[doc]);
            //17-6-2026 van double docLen = docLength[doc]; naar
            double docLen = docLength.count(doc)? docLength.at(doc):1;
            
            if(docLen ==0)
            {
                docLen =1;
            }
            
            cout << "DEBUG docLen=" << docLen << " avg=" << avgDocLen << endl;

            double score = 
            idf *
            ((tf*(k1+1)) /
            (tf+k1*(1- b + b*(docLen/avgDocLen))));

             //17-6-2026: toegevoegde test:
            cout << "DOC KEY CHECK: " << doc << endl;

            //17-6-2026: toegevoegde test
            cout <<" docLength exists? " << docLength.count(doc) << endl;

            //17-6-2026: toegevoegde test
            cout << "docLen " << docLength[doc] << endl;


            // for(int p: positions)
            // {
            //     std::cout << p << " ";
            // }
            // // std::cout << std::endl;
            // // return it->second;
            // std::cout<<std::endl;

            //17-6-2026: van result.insert(doc); naar: (omdat we map ipv set gebruiken)
            //17-6-2026 nu gewijzigd naar result[doc] += positions.size();
            //17-6-2026 en weer terug naar result[doc] = 1;
            result[doc] = score;
        }   
        // Return leeg
        // 16-6-2026: moet zijn return resultaat
        return result;
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
        //17-6-2026: wordt een map: std::unordered_set<std::string> result;
        unordered_map<string,double> result;
        //voor ieder document in left
        //17-6-2026: logica aangepast t.b.v. map. was: for(const auto&doc:left)
        for(const auto&[doc, lscore]:left)
        {
            // Als document doc ook in de rechter verzameling zit, voeg het dan toe aan het resultaat.
            // 17-6-2026: ook aangepast if(right.count(doc)) 
            if(right.count(doc)) 
            {
                //17-6-2026: gewijzigd van result[doc] = left[doc]+right[doc]; naar
                //17-6-2026: en weer gewijzigd van result[doc] = 1; naar
                //17-6-2026: Weer gewijzigd int rscore = right.at(doc);
                //en dit ook result[doc] = lscore + rscore + 1; naar
                //17-6-2026 en weer gewijzigd naar result[doc]=lscore + right.at(doc) * 2;
                //17-6-2026: weer veranderd naar BM25styleresult[doc] = left[doc]+right[doc];
                result[doc] = min(left[doc],right[doc]);
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

        //17-6
        unordered_map<string,double> result = left;

        //17-6-2026: Dit is aangepast naar een forloop: left.insert(right.begin(), right.end());
        for(const auto& [doc, score]:right)
        {
            //17-6-2026: gewzijgid van left[doc] += score; naar
            //17-6-2026 left[doc] = 1; weer naar
           //17-6-2026 weer gewijzigd left[doc] += score; naar
           auto it = left.find(doc);
           
           if(it == left.end())
            {
                left[doc] = score;
            }
            else
            {
                it->second = max(it->second, score);
            }
  
        }
        // returneer links
        return left;
    }
    //
    // ===== NOT =====
    //
    // als Node type NOT is
    if (node->type==NodeType::NOT)
    {

        //17-6-2026 Nieuw
        unordered_map<string, double>result;

        // roep evaluateAST functie op en parameter met parameter rechternode en index en sla op in child
        // 4-6-2026: auto child = evaluateAST(node->left, index); wordt right. Dit heeft te maken met dat
        // NOT altijd maar 1 branch heeft, namelijk zijn tegenovergestelde.
        auto child = evaluateAST(node->right, index);
        // maak een set van strings voor allDocs
        //17-6-2026: van std::unordered_set<std::string> allDocs; aangepast naar:
        //17-6-2026: en van std::unordered_map<string, double> allDocs; weer naar
        unordered_set<string> allDocs;
        // voor linker en rechterdoc in de index
        for(const auto& [word,docs]:index)
        {
            //Voeg alle documenten toe aan allDocs
            //4-6-2026: Was eerst: allDocs.insert(allDocs.begin(), allDocs.end()); gewijzigd naar:
            //17-6-2026 for(const auto&doc: docs)
            for(const auto&[doc, positions]:docs)
            {
                //17-6-2026: van allDocs.insert(doc.first);
                //17-6-2026: van allDocs[doc.first] = 0;
                //17-6-2026: weer terug naar allDocs[doc.first] = 1;
                //17-6-2026: weer terug van allDocs[doc] = 1; naar
                allDocs.insert(doc);
            }
        }
        // voor alle documenten in child
        //17-6-2026 van for(const auto& doc: child) naar
        for(const auto& [doc, score]:child)
        {
            // Verwijder alle documenten uit allDocs
            //17-6-2026: gewzijgd van allDocs.erase(doc);
            {
                allDocs.erase(doc);
            }
        }
        //17-6-2026: Geef defaultscore 1
        for(const auto& doc:allDocs)
        {
            result[doc] = 1.0;
        }


        // retourneer allDocs
        return result;
    }
    // return {};
    return {};
}



        
    
