// 5-5-2026: Search engine
// 5-6-2026: Nog wel een keer de code checken of die helemaal duidelijk is
// 7-5-2026: Delen gekopieerd naar losse bestanden

//7-5-2026: erbij gezet: parser.h. Dus main weet dan dat hij de parser moet gebruiken.
#include "../fileLoader/fileLoader.h"
#include "../indexer/indexer.h"
#include "../search/search.h"
#include "../queryEvaluator/queryEvaluator.h"
#include "../queryParser/ASTBuilder.h"
#include "../types/AST.h"

//t.b.v testen
#include "../tokenizer/tokenizer.h"
#include "../queryParser/queryParser.h"
#include "../queryEvaluator/ASTEvaluator.h"

#include <iostream>
// stdlib overbodig
// onderdeel waarmee je door je bestanden en mappen kunt werken
// gebruik als bouwsteen. Werkt pas goed vanaf C++17
#include <filesystem>
// voor ifstream straks handig:
#include <fstream>
#include <string>
#include <vector>
// gebruikt voor o.a. Freq map en InvertedIndex
#include <unordered_map>
// Gebruikt voor o.a. InvertedIndex
#include <unordered_set>
// wat is cctype?
#include <cctype>
#include <algorithm>

using namespace std;
// ga std::filesystem voortaan korter schrijven als fs (alias)
namespace fs = std::filesystem;

// 4-6-2026: Hier toegevoegd: main.cpp
// functie printAST met als parameter een pointer naar een ASTNode en default parameter diepte van 0.
void printAST(ASTNode* node, int depth = 0)
{
    // Als er geen node is retourneer 
    if(!node) return;

    // Voor integer 0 tot integer kleiner dan diepte, verhoog i.
    for(int i=0; i<depth;i++)
    {
        cout<<" ";
    }
    // Zet de waarde van het node type (ik denk enum) om naar een integer en print de waarde.
    // Dat wordt dan TERM = 0, AND =1, OR =2, NOT=3
    // (dit is dus omzetten en niet zoals 'auto' afleiden van het datatype)
    cout << static_cast<int>(node->type) << endl;
    // Recursief printAST oproepen op linkernode
    printAST(node->left, depth + 1);
    // Recursief printAST oproepen op rechternode
    printAST(node->right, depth + 1);
}


// ============================
//         == MAIN ==
// ============================

int main()
{
    // Toegevoegd: extra check
    // 19-5-2026: Geef aan in welke map mijn programma draait.
    cout << fs::current_path() << endl;  

    // maak een variabele folder aan: '..': ga 1 map omhoog.
    // 28-5-2026: gewijzigd van string folder = "test_data"; naar:
    // 4-6-2026: gewijzigd van string folder = "src/test_data"; naar:
    // fs::path folder = fs::current_path()/ "test_data";
    // 4-6-2026: weer gewijzigd naar
    string folder = "./src/test_data/";
    
    // 1) Check folder eerst
    // Bekijk of er in het huidige pad een bestand genaamd 'test_data" bestaat.
    if(!fs::exists(folder))
    {
        cout <<"ML: Eigen bericht. Dus app start maar Folder does not exist! "<<endl;
        return 1;
    }

    // 2) Files ophalen
    vector<fs::path> files = getFiles(folder);

    // 3) Loop door de files
    for (const auto& file : files)
    {
        cout << "\nFILE: " << file.filename().string() << endl;

        //3.1 File lezen
        string content = readFile(file);

        cout << content << endl;
        cout << "------------------------" << endl;

        //3.2) Roep de tokenize functie aan en geef als argument de text mee. Sla resultaat op in words.
        auto words = tokenize(content);

        //3.3) Roep de buildFrequencyMap aan en geef als argument words mee en sla het resultaat op in freq.
        //7-5-2026: deze weggehaald vanwege: 
        //19-5-2026: Nu weer aangepast. Was auto frequentie = buildFrequencyMap(content);
        auto frequentie = buildFrequencyMap(words);

        //6) Print ieder paar in de Hashmap (woord, aantal): first en second.
        for(const auto& pair:frequentie)
        {
        cout<<pair.first <<" --> "<< pair.second<<endl;
        }
        
    }
    auto index = buildInvertedIndex(files);

    // 7-5-2026: Deze weggehaald: multiSearch(index, "hello bye");
    // In plaats daarvan:
    // We gaan onder andere zoeken of de woorden 'search', 'multi' en 'rank' aan het begin voorkomen
    // van een zoekveld
    
    //13-5-2026: Test voor queryparser: 
    // Kan volgens mij weg
    //4-6-2026: we vervangen onze query van vector<Token> tokens = tokenizeQuery("hello AND amsterdam"); naar;
    vector<Token> tokens = tokenizeQuery("hello OR random AND project");

    //4-6-2026: direct nog een test na tokenizeQuery("NOT hello");
    for(const auto& token : tokens)
{
    cout << "TYPE=" << static_cast<int>(token.type)
         << " VALUE=" << token.value << endl;
}

    //4-6-2026: Test voor AST Builder oproepen: deze komt dus in plaats van toPostfix
    ASTBuilder builder;
    ASTNode* root = builder.build(tokens);

    //4-6-2026: Dit er later nog bijgezet
    //Roep functie evaluateAST op met parameters root en index en sla op in resultaat (auto)
    auto ASTResult = evaluateAST(root,index);

    // 4-6-2026: test toevoegen

    cout << "AST RESULT SIZE: " << ASTResult.size() << endl;

    for(const auto& file : ASTResult)
    {
        cout << file << endl;
    }

    printAST(root);
};
// 4-6-2026: toPostfix etc weghalen. want AST komt hiervoor in de plaats. Mogelijk om dit later
// nog erbij te voegen:

    // vector<Token> postfix = toPostfix(tokens);

    // for(const auto& token : postfix)
    // {
    //     cout << token.value <<" ";
    // }
    
//     auto PostFixResult = evaluatePostfix(postfix, index);

//     cout << "RESULT SIZE: " << PostFixResult.size() << endl;

//     for(const auto& file : PostFixResult)
//     {
//         cout << file << endl;
//     }
// }