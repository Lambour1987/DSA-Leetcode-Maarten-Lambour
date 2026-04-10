// Eigen idee met 2 maps

#include <stdlib.h>
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution
{
public:
    // Check nog of const string&s en t goed is: ja is geen kopie en read only
    bool isValid(const string&s, const string&t)
    {
        // Eerste check of strings wel gelijk zijn (edgecase)
        if(s.length() != t.length())
            return false;

        // Map want key (letter) en value (aantal)
        unordered_map<char,int> unorderedS;
        unordered_map<char,int> unorderedT;
        
        for(const auto& charS:s)
        // toevoegen karakter aan char en verhoog count van s
            unorderedS[charS]++;
            
        for(const auto& charT:t)
        // toevoegen karakter aan char en verhoog count van t
            unorderedT[charT]++;
        
        // vergelijk beide maps (dus eigenlijk O(n))
        // Kan simpeler: return unorderedS == unorderedT
        if(unorderedS == unorderedT)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    Solution sol;
    string s = "carrace";
    string t = "racecar";

    bool answer = sol.isValid(s,t);

    cout<<answer<<endl;
}
