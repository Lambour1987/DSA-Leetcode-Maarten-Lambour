// 5-5-2026: Search engine

#include <iostream>
// stdlib overbodig
// onderdeel waarmee je door je bestanden en mappen kunt werken
// gebruik als bouwsteen. Werkt pas goed vanaf C++17
#include <filesystem>
// voor ifstream straks handig:
#include <fstream>
#include <string>
#include <vector>

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
// == MAIN ==
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

        string content = readFile(file);

        cout << content << endl;
        cout << "------------------------" << endl;
    }
    return 0;
}