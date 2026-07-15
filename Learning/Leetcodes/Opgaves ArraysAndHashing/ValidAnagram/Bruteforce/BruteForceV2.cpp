// Bruteforce: ga met buitenste loop over s en binnenste loop over t
// In t moeten we een visited array bijhouden. Dit kan een set zijn
// maar hoeft niet?

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
    public:
        bool ValidAnagram(string s, string t)
        {
            //Eerst kijken of beide strings even lang zijn
            if(s.size()!=t.size())
            {
                return false;
            }

            //een visited array bijhouden voor string t, die even lang is als string t (of s want even lang)
            //Vul met nullen
            vector<int>visited(t.size(),0);


            // 
            for(const auto& chars:s)
                for(int j=0; j<t.size();j++)
                {
                    // Als overeenkomst is gevonden. Zoek of chart in array staat.
                    // Als die
                    if(chars==t[j] && visited[j]==0)
                    {
                        visited[j]=1;
                        // nu kan je ook stoppen want, je hebt de letter gevonden dus meteen door naar volgende
                        // letter
                        break;
                        
                    }
                   
                  
                    //Als je binnen de loop retourneert return je direct bij eerste mismatch (kan wel bij
                    //bijv. contains duplicate opgave)
            
                }
        }
};

int main()
{
    Solution sol;
    string s = "carrace";
    string t = "racecar";
    bool answer = sol.
}
