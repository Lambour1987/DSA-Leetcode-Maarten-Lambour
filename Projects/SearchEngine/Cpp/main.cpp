// 5-5-2026: Search engine
// 5-6-2026: Nog wel een keer de code checken of die helemaal duidelijk is

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


using namespace std;
// ga std::filesystem voortaan korter schrijven als fs (alias)
namespace fs = std::filesystem;

// ============================
// == GET FILES ==
// ============================

// Functie om alle documenten uit een dataset op te halen
// Resultaat terug in een vector van bestandspaden (onderdeel van filesystem (fs)).
// Als input referentie naar folder (niet aan te passen)
vector<fs::path> getFiles(const string& folder)
{
    // Vector aanmaken om bestandspaden in op te slaan
    vector<fs::path> files;
    // Voor iedere bestandsfile in het filesystem (directory) maken we een referentie en wordt het datatype automatisch bepaald
    // Dit is dus gewoon door een directory lopen: 1 voor 1 bestanden geven.
    for(const auto&entry:fs::directory_iterator(folder))
    {
    // Als het bestand een gewone file is dan moeten we de bestandslocatie/ pad aan de vector toevoegen
    // is_regular_file is een functie die bepaalt of we met een echt bestand te maken hebben: dus geen
    // mappen, snelkoppelingen en systeembestanden
        if(entry.is_regular_file())
        {
            // voeg pad toe aan vector getFiles
            files.push_back(entry.path());
        }
    }
    // retourneer de vector met bestandspaden
    return files;
}

// ============================
// == READ FILES ==
// ============================

// Functie die het bestand leest en als input heeft een referentie naar path van het type path (van fs)
// en als output een string geeft
string readFile(const fs::path& path)
{
    // bestand openen o.b.v. bestandslocatie/pad
    ifstream file(path);
    // probeer het bestand te openen. Als dit niet lukt melding. 
    if(!file)
    {
        cout<<"Bestand niet geopend"<<endl;
    }
    // declareer string variabelen content (voor alle regels) en line (1 regel)
    string content;
    string line;
    // zolang er regels in de file zijn, stop die in line. Gebruikt functie getline.
    while (getline(file, line))
    {
    // voeg de lijnen toe aan de grote string: In deze fase nog handig 1 grote string te gebruiken,
    // en niet een vector. Scheidt deze met een 'enter'. Let op niet met endl; want het gaat hier
    // over 1 string en niet verschillende strings;
        content += line + "\n";
    }
    // return content
    return content;
};

// ============================
// == TEXT PROCESSING ==
// ============================

// Tekst splitsen in woorden "Hallo Wereld Hallo Wereld Bye Wereld" 
// wordt ("hallo", "wereld", "hallo", "wereld", "bye", "wereld")

//Functie tokenize met als input een snelkoppeling naar tekst die we niet willen wijzigen
//en als output een vector van strings
vector<string> tokenize(const string& text)
{
    // Maak een vector van woorden aan
    vector<string> words;
    // Maak een variabele 'woord' aan
    string word;
    // Doorloop ieder karakter van de tekst (voor een char is const en & niet nodig)
    for(char c:text)
        // Als de tekst een spatie bevat (' '), een tab bevat ('    ') of een endl;
        // gebruik (isspace). Dan controleer je alle 3.
        // Vergelijk: als we vragen of c leeg is: c==' '. maar nu met functie dus: isspace(c). (dan c als argument)
        if(isspace(c))
        {
        // check of het woord helemaal leeg is.
                if(!word.empty())
                {
                // niet leeg dan pushen we het woord op de vector
                    words.push_back(word);
                // wat is word.clear?
                    word.clear();
                }
        }
        else
        {
        // Geen spatie is. Dan de letter aan de woordstring toevoegen in kleinkapitaal:
            word +=static_cast<char>(tolower(c));
        }

    //Als het woord niet leeg is, voeg het woord toe aan de string woorden
    if(!word.empty())
    {
        words.push_back(word);
    }
    // Retourneer woorden
    return words;
}    

// ============================
// == FREQUENCY MAP ==
// ============================

// We gaan tellen hoe vaak woorden voorkomen in de vectoren van strings 
// dus 'hello', 'world', 'hello', 'world', 'bye', 'world' 2x hello, 3x world, 1x bye.

// Functie buildFrequencyMap die als input vraagt een referentie naar vector van strings 'words' 
// en output een hashmap key: string, value: int
unordered_map<string, int> buildFrequencyMap(const vector<string>&words)
{
    //Declareer een hashmap frequentie
    unordered_map<string,int>frequentie;

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

// ============================
// == SEARCH ==
// ============================

// Zoekfunctie search met als input(map-set genaamd index en een query). Output void.
// Denk bij void: soms een printfunctie maar met referenties werken we gewoon direct in de variabele
// de we hebben opgeroepen. Dit is dus geen lineair search of binary search
void search(const unordered_map<string,unordered_set<string>>&index, const string& query)
{
    //Zet query naar lowercase (consistent met tokenize)
    //Voor iedere letter in de query moeten we deze naar lowercase zetten
    //Tussendoor: technisch gezien gaat omzetten van 'hello' naar 'hello' itt'HELLO' naar 'hello' net iets sneller.
    //Dus conversie kost minimale tijd

    //BELANGRIJK: Nu maken we bij de parameters een referentie naar een query, en hier kopieren we de query (we kopieren niet de referentie)
    // toch is dit sneller dan direct in de parameteroproep een kopie te maken (const string& query wordt dan 'string query'). Mag wel maar
    // is iets langzamer. Nu: we maken pas een kopie als hem nodig hebben. Blijkbaar.
    string q = query;
    // char dus geen const en & nodig
    for(char& c:q)
    {
        c=tolower(c);
    }

    // We zoeken de query in de map-set index. Als niet gevonden, geef melding.
    // Dus we zoeken dan in de map-set index de query. Dat is gelijk aan index.end());
    // Wat is index.end()); ook alweer?
    if(index.find(q) == index.end())
    {
        cout<<"Woord niet gevonden"<<endl;
        return;
    }
    
    // Als deze wel gevonden is zoek in de index naar de query (nog niet eerder zo gezien)
    // en retourneer de filename.
    // Dit zou ook binnen de if statement kunnen? In dit geval betekent het precies hetzelfde?
    // Verschil: eerst if statement. Als gevonden dan returnen. Of. Hij is niet- niet gevonden.
    // Dus wel gevonden. Dus door met volgende regel
    for(const auto& file:index.at(q))
    {
        cout<<file<<endl;
    }
}

// ============================
// == MULTISEARCH ==
// ============================
// Als we zoeken (query): "hello bye"
// hello staat in a.txt en b.txt en bye staat in b.txt
// Maar we willen alleen waar Beide in voorkomen: Intersection (denk aan set, union, intersection, difference)

// Functie searchMulti heeft als input de map-set index en de query. Als output niks
void MultiSearch(const unordered_map<string, unordered_set<string>>& index, const string& query)
{
    
    // Roep de functie tokenize met argurment query en sla op in een woordvector
    vector<string> words = tokenize(query);
    // Als woord is leeg dan retourneer
    if(words.empty())
    {
        return;
    }
    // start met eerste woord (dat is a[0]) en sla het resultaat op in result: geef de waarde die hoort bij key hello
    auto result = index.at(words[0]);
    // intersect met de rest: begin bij 1 en ga door tot einde (let op dit lijkt wel een beetje op LL maken)
    // BELANGRIJK: waarom niet int i =1 maar size_t=1? int werkt ook. maar size_t is correcter: is een unsigned
    // integer type speciaal voor groottes en indices. size_t komt komt uit de words vector.
    // als je int i zou doen vergelijk je int(signed) met size_t(unsigned). compiler moet dan converteren.
    // Dus size_t is het datatype
    for(size_t i=1; i<words.size(); i++)
    {
        //volgende woord in index opslaan in variabele nextSet
        const auto& nextSet = index.at(words[i]);
        //maak een string set 'temp' aan.
        unordered_set<string> temp;
        //Loop door iedere file heen uit resultaat
        for(const auto& file:result)
        {
            // Als de file in nextset zit? (gebruik Count)
            if(nextSet.count(file))
            {
                //voeg de file toe aan tijdelijke set
                temp.insert(file);
            }
        // sla tijdelijk resultaat op in result
        }
        result = temp;
    }
    
    // Doorloop iedere file in het resultaat en print resultaat.
    for(const auto& file: result)
    {
        cout<<file<<endl;
    }
};

// ============================
//      == RANKING ==
// ============================

// Per file geven we een score. Woord komt 1x voor +1, 

// Functie RankedSearch(map-set: index en query) en void output
void RankedSearch(const unordered_map<string,unordered_set<string>>&index, const string& query)
{
    // Roep tokenize functie aan(input is query) en sla resultaat op in words
    // We hebben bijv als query: 'hello bye'. We roepen tokenize functie op en die geeft 
    // dan terug: ["hello", "bye"]
    const auto& words = tokenize(query);
    
    //Score map: maak een hashmap (string, int) voor de score
    unordered_map<string,int> score;
    //Per woord files ophalen
    for(const auto& word:words)
    {
        //zoek woord op in index. Als gevonden ga door. zoek in volledige index (na einde)
        if(index.find(word)==index.end())
        {
            continue;
        }
        // voor iedere file op de positie word van de index
        // dus niet: for(const auto&file:word[index])
        for(const auto&file:index.at(word))
        {
            //Verhoog de score van die file
            score[file]++;
        }
    }
    //maak een vector van paren (string, int) aan 'ranked'
    vector<pair<string, int>> ranked;
    //voor ieder paar in de score
    for(const auto&[file,s]: score)
        // Voeg paar (file, s) toe aan de vector van paren ranked
        ranked.push_back({file, s});

    // Sorteer rankden van begin tot eind, gebruik een lambda (inline) functie
    // lambda [capture](parameters) -> return type { body }. Hier geen capture
    // BELANGRIJK: lambda is hier dus onderdeel van sort. Je zet het achter sort neer. Normaal
    // niet verplicht. Nu wel: Ik bepaal hier nu de volgorde: we zetten a voor b als a.second 
    // groter is dan b.second. Return een boolean: want je doet eigenlijk een if statement: is a>b.

    sort(ranked.begin(), ranked.end(),
    //capture en daarna tussen haakjes de parameters
    [](const auto& a, const auto&b)
    {
        return a.second>b.second;
    });

    // We gaan nu weer ieder paar uit ranked printen
    for(const auto&[file,s]:ranked)
    {
        cout<<file <<" -> "<<s<<endl;
    }
}



// ============================
//         == MAIN ==
// ============================

int main()
{
    // Toegevoegd: extra check
    cout << fs::current_path() << endl;  

    //maak een variabele folder aan: '..': ga 1 map omhoog.
    string folder = "../test_data";

    // 1) Check folder eerst
    // Als folder niet bestaat, geef melding
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
        auto frequentie = buildFrequencyMap(words);

        //6) Print ieder paar in de Hashmap (woord, aantal): first en second.
        for(const auto& pair:frequentie)
        {
        cout<<pair.first <<" --> "<< pair.second<<endl;
        }

        
    }
    auto index = buildInvertedIndex(files);

    MultiSearch(index, "hello bye");

    return 0;
}