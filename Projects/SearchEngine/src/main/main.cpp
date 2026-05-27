// 5-5-2026: Search engine
// 5-6-2026: Nog wel een keer de code checken of die helemaal duidelijk is
// 7-5-2026: Delen gekopieerd naar losse bestanden

//7-5-2026: erbij gezet: parser.h. Dus main weet dan dat hij de parser moet gebruiken.
#include "../fileLoader/fileLoader.h"
#include "../indexer/indexer.h"
#include "../search/search.h"
#include "../queryEvaluator/queryEvaluator.h"

//t.b.v testen
#include "../tokenizer/tokenizer.h"
#include "../queryParser/queryParser.h"

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


// ============================
//         == MAIN ==
// ============================

int main()
{
    // Toegevoegd: extra check
    // 19-5-2026: Geef aan in welke map mijn programma draait.
    cout << fs::current_path() << endl;  

    // maak een variabele folder aan: '..': ga 1 map omhoog.
    string folder = "test_data";

    // 1) Check folder eerst
    // Bekijk of er in het huidige pad een bestand genaamd 'test_data" bestaat.
    if(!fs::exists(folder))
    {
        cout <<"Folder does not exist! "<<endl;
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
    vector<Token> tokens = tokenizeQuery("hello AND amsterdam");

    vector<Token> postfix = toPostfix(tokens);

    for(const auto& token : postfix)
    {
        cout << token.value <<" ";
    }
    
    auto result = evaluatePostfix(postfix, index);

    cout << "RESULT SIZE: " << result.size() << endl;

    for (const auto& file : result)
    {
        cout << file << endl;
    }
}