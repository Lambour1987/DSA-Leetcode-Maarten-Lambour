//7-5-2026: 

#include "indexer.h"
#include "../parser/parser.h"

//BELANGRIJK: hoewel deze libraries ook in indexer.h staan en zelfs meegenomen worden is het beter om
//deze alsnog apart hier neer te zetten. Want dan kan je bestanden altijd afzonderlijk compilen.

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <filesystem>

using namespace std;
namespace fs = std::filesystem;


// ============================
// == FREQUENCY MAP ==
// ============================

// We gaan tellen hoe vaak woorden voorkomen in de vectoren van strings 
// dus 'hello', 'world', 'hello', 'world', 'bye', 'world' 2x hello, 3x world, 1x bye.

// Functie buildFrequencyMap die als input vraagt een referentie naar vector van strings 'words' 
// en output een hashmap key: string, value: int
// 7-5-2026: veranderde parameter van 'const vector<string&>words' naar huidige: vanwege Single Responibility
//
unordered_map<string, int> buildFrequencyMap(const string& text)
{
    //Declareer een hashmap frequentie
    unordered_map<string,int>frequentie;

    // 7-5-2026: Nieuw: ipv functie woorden als parameter mee kreeg, krijgt hij nu text mee.
    // en met die text laat hij zelf woorden maken door tokenize op te roepen.
    vector<string>words = tokenize(text);

    //For each word in words tel hoeveelheid woorden (?)
    for(const auto& word:words)
    {
        // Vergelijk met frequentie =+1;
        // Hier: verhoog in de map frequentie bij kolom word de het aantal als deze al bestaat of
        // voeg toe als het woord nog niet in de map is opgenomen.
        frequentie[word]++;
    }
    // Retourneer het resultaat
    return frequentie;
}

// ============================
// == builtInvertedIndex ==
// ============================
// We gaan aangeven in welke files een woord voorkomt: Vergelijk met google search
// We gebruiken een set

// Functie buildInvertedIndex die als input heeft een vector van bestandspaden (van fs) genaamd files
// en teruggeeft een hashmap met key: string en value een set van strings. Dus tellen hoe vaak die voorkomt? Nee!
// We slaan op in welke files een woord voorkomt
// Een hashset heeft net als een map ook een key en value maar key is index? maar hier dus string (eerste deel van unordered_map?)
unordered_map<string, unordered_set<string>> buildInvertedIndex(const vector<fs::path>&files)
{
    //maak dus een map met key(string) en value (set van strings) genaamd index
    //Het is dus een map met key: string en een verzameling van strings (bestandsnamen): 
    // hello → {"a.txt", "b.txt"}
    // world → {"a.txt"} 

    unordered_map<string,unordered_set<string>> index;
    //loop door iedere file heen
    for(const auto& file:files)
    {
        //Roep de functie readfile op (arg file) en sla de inhoud op in een string content
        string content = readFile(file);
        //Roep de functie tokenize op (arg content) en sla het resultaat op in words
        auto words = tokenize(content);
        //Loop door vector van woorden heen heen
        for(const auto& word:words)
        //voeg in de map-set index de filename toe en a aan de set van het woord 'word'
        {
            index[word].insert(file.filename().string());
            // Werd eerst als correctie aangeboden. Blijkt toch weer een bug: index.at(word).insert(file.filename().string());
        }

    }
    // Return index
        return index;
}