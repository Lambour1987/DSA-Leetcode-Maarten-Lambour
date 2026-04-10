//Two Pointers begin links en rechts (niet vanuit midden)
// Oplossing lastiger dan ik dacht

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <cctype> // Om letters hoofdletter -> kleine letter te maken


using namespace std;

class Solution
{
    public: 
        bool ValidPalinDrome(string& s)
        {
            // Controle op lege string
            if(s.empty()) return false;


            //Begin met pointers rechts en links
            // Dus niet l = s[0]
            int l = 0; 
            int r = s.size()-1;

            // Ik had r>l. Is exact hetzelfde als l<r. Maar wel doen l<r
            // Verderop wel r>l
            while(l<r)
            {   // for loop kan ook? Kan wel
                // Als links en rechts gelijk en beide alfanumeriek, ga dan door
                // Dus: als l/ r of beide niet alfanumeriek zijn dan moet 1 van de twee doorschuiven
                // Geen sliding window want pointers bewegen naar elkaar toe (alhoewel onder voorwaarden)
                // Check eerst of s[l] alfanumeriek is

                // While loop in een while loop: Gewoon O(n): want l gaat nooit naar links en r nooit naar rechts: 
                // theoretisch kan je oneindig geneste loops hebben en toch O(n) zolang de richting maar gelijk blijft
                // (de loops bewegen niet onafhankelijk, maar afhankelijk van elkaar)
                while(l<r && !alphanum(s[l]))
                {
                    l++;
                }
                // Hier r>l. Is hetzelfde: maar consistent is l<r volgens Chat.
                while(r>l && !alphanum(s[r]))
                {
                    r--;
                }
                if(tolower(s[l]) != tolower(s[r]))
                {
                    return false;
                }
                l++,r--;
            }

            return true;

        }
        // Hulpfunctie om te bepalen of een karakter alfanumeriek is
        bool alphanum(char c)
        {
            // alfanumeriek als: Hoofdletters A-Z, a-z, 0-9
            // Dit doe je met operator precedence: hiermee pak je dus alle letters: groter of gelijk aan a 
            // en kleiner of gelijk aan z.
            // tussen 'a' en 'z'
            return
                (c>='a' && c<='z') || 
                (c>='A' && c<='Z') ||
                (c>='0' && c<='9');
        }
};

int main()
{
    Solution sol;
    string s = {"Was it a car or a cat I saw?"};
    bool answer = sol.ValidPalinDrome(s);
    cout << "Is this a Palindrome? " << (answer ? "true" : "false");

    return 0;
}