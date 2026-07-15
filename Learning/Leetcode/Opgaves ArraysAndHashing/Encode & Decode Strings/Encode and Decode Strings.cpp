// 3-4-2026
#include <vector>
#include <stdlib.h>
#include <iostream>

using namespace std;

class Solution
{
public:

    string encode(vector<string> strs)
    {
    // Vector van pairs maken voor het bijhouden van het aantal letters per woord
        vector<pair<string, int>> karaktermap;
        // Houd een teller bij die start bij 1 (altijd 1 karakter)
        

    // Loop door het aantal woorden in strs
        for(auto& woord:strs)
        {
            int count =1
            // Loop door iedere letter van het woord en houdt bij hoeveel letters het zijn
            for(auto&letter:woord)
                count[letter]++;
            //Sla het resultaat op in de vector van pairs
            
            karaktermap.push_back(woord, count);

        }

    // Oplossing zelf bedacht. Kan maar omslachtig:
    // Tel aantal woorden, tel aantal letters per woord. Houdt lengte per woord bij. Houdt totale positie bij.
    // Dat in een vector<pair<pair<string,int>int>>. array van woord, aantal letters en positie in totaal. Bijv
    // Stel woord 1)  "A,B,C,D". 1,2,3,4: lengte 4. woord 2) "E,F,G,H,I". 1,2,3,4,5 maar ook 5,6,7,8,9: lengte 5 3) woord 3 "J,K,L".
    // 1,2,3 maar ook: 10,11,12. Lengte 3. woord 4) M,N lengte 1,2. Lengte 2. Maar ook 13,14.
    // Vervolgens kunnen we starten bij woord 1 en kopieren naar een nieuwe string, Nu moet woord 2 gekopieerd worden naar woord 1 (lengte is 5) en moet op positie 5 komen te staan (dat is 4+1). Woord 3
    // moet gekopieerd worden achter woord 2. Dat is nu dus positie 10 in totaal (lengte woord 1 + lengte woord 2 + 1)
    // woord 4 moet achter woord 1 en 2 en 3 komen te staan. Dat is dus positie 13 en 14.
    // Dit kan dus in een vector<pair<pairs<string, int, int>>> maar dan moet je dus positie bijhouden en dat is onnodig complex
    // Daarna kan je op basis van de relatieve positie ook weer decoderen.
    // Ik geloof dat mijn oplossing niet mag want we houden dan iets bij (state variable)

    return encoded_string;
    }
};

vector<string> decode(string s)
{





}
int main()
{

    return strs;
}

int main()
{
    Solution sol;
    string strs = {"Hel   lo", "#%#World"};

}