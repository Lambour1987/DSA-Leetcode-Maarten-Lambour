//1-4-2026: Nog eens doen: idee klopt (bruteforce met visited array maar) maar hte werkt nog niet.

#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    // Check: const string &s?
    bool isValid(const string &s, const string &t)
    {
        // Eerst checken of de lengtes van beide arrays even lang zijn
        if(s.length() != t.length())
        {
            return false;
        }
        
        // Dus een vector met booleans waarvan de lengte even groot is als onderste string t. vul met nullen.
        vector<bool>visited(t.length(), false);

        for(int i=0;i<s.length();i++)
        // itt contains duplicate hier dus wel steeds opnieuw starten vanaf 0? Maar reeds overeengekomen
        // letters wel overslaan. Of marken of flaggen ofzo. Dan nog een array bijhouden voor onderste array
        // met 1 (al gehad) of 0
        {
            // Dit is een edge case
            bool found = false;
            for(int j=0;j<t.length();j++)
            {
                //Als i en j gelijk zijn op de index en de flag staat op 0, dan de flag array op die index (ook j) op 1 zetten
                if(s[i]==t[j]&& !visited[j])
                {
                    visited[j]=true;
                    found = true;
                    // Stop inner loop zodra match is gevonden
                    break;
                }
                // uiteindelijk moeten alle flags op 1 staan. Dat zal sowieso zijn omdat het algoritme stopt zodra
                // er geen match is
                
            }
            if(!found)
                    return false;
        }
        return true;
    }
};

int main()
{
    Solution sol;
    string s = "racecar";
    string t = "carrace";

    bool answer = sol.isValid(s,t);
    cout<<answer<<endl;

}