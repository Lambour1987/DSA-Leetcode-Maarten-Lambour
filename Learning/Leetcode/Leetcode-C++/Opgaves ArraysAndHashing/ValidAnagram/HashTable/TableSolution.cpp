// In plaats van unordered map gebruikt leetcode een tabel
// 

#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
    public:
        bool isValid(string& s, string&t)
        {
            // Eerst controleren of een van de strings leeg is. Beide leeg of in van beide leeg. Return false.
            if(s.length() != t.length())
            {
                return false;
            }

            //Maak tabel aan met 26 karakters gevuld met 0
            // Of hashmap? je moet alle letters toevoegen aan hashmap? 
            // Of je moet de input letters aan een hashmap hangen zodat de inputstrings getallen worden ipv letters
            vector<int>count(26,0);
            {
                //Forloop: mag ook t.length zijn
                for(int i=0;i<s.length();i++)
                {
                    //Tel in de count tabel 1 op op de juiste index: dat is de huidige letter (bijv c) minus 1 (a). Want index.
                    count[s[i] - 'a']++;
                    //Tel in de count tabel 1 op op de juiste index: dat is de huidige letter (bijv c) minus 1 (a). Want index.
                    count[t[i] - 'a']--;

                }
                //Nu bekijken of alle indices weer op 0 staan. Zo niet, dan geen anagram. Zo wel, wel een anagram
                for(int c:count)
                {
                    if(c!=0)
                    {
                        return false;
                    }
            }

            return true;
        }
};


int main()
{
    Solution sol;
    string s = {"carrace"};
    string t = {"racecar"};
    bool answer = sol.isValid(s,t);
};
