// Sorteer eerst alle letters van de woorden
// Sorteer daarna alle woorden
// O(m*nlogn)
// Maar let op! Orginele woorden moeten worden gegeven

#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>


using namespace std;

class Solution
{
public:
    vector<vector<string>> GroupAnagram(vector<string>&strs)
    {
        //Hashmap en sorting gebruiken: We maken een Hashmap met key (inputstring) en value is
        //de lijst met woorden die dezelfde letters hebben:
        // bijv key: res["opst"] → Value: ["stop", "tops", "pots"]
        unordered_map<string, vector<string>> hashmap;

        //We lopen eerst door de woorden van de input heen
        for(const auto& s:strs)
        {
            // Van ieder woord maken we een kopie:
            string sortedS = s;
            // Van ieder woord gaan we de letters sorteren:
            sort(sortedS.begin(),sortedS.end());
            // Ieder gesorteerd woord gaan we toevoegen als key en ieder inputwoord
            // gaan we toevoegen als value (pushback)
            hashmap[sortedS].push_back(s);

        }

        // Maak een vector van vectoren om het resultaat op te slaan (geen echte matrix)
        vector<vector<string>>result;

        // We gaan nu door de Hashmap lopen en we voegen de pairs (1 key, meerdere values) toe
        // aan het resultaat
        for(auto&pair:hashmap)
        {
            result.push_back(pair.second);
        }

        return result;
        
    }
};

// Iets uitgebreidere helperfunctie
ostream& operator<<(ostream& os, const vector<vector<string>>& vv)
{
    for (const auto& v : vv)
    {
        os << "[ ";
        for (const auto& s : v)
        {
            os << s << " ";
        }
        os << "] ";
    }
    return os;
}


int main()
{
    Solution sol;
    vector<string> strs = {"act","pots","tops","cat","stop","hat"};
    vector<vector<string>> answer = sol.GroupAnagram(strs);
    cout<<answer<<endl;
}