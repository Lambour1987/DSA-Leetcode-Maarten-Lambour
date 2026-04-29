// Prefix en Suffix

#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
        vector<int> ProductOfArrayExceptSelf(vector<int>nums)
        {
        //We hebben 3 arrays nodig: 1 voor prefix, 1 voor suffix en 1 voor het resultaat daarvan
        //Datatype integer, omvang is in te vullen, startwaarde 1 of 0.
        //Of gewoon leeg laten?
        vector<int>prefix(nums.size(),1);
        vector<int>suffix(nums.size(),1);
        vector<int>result(nums.size(),1);

        //Een forloop met pointer i en j. Kan in 1 loop. Einde voor de een is het begin
        //voor de ander
        // i en j zijn te gebruiken voor zowel de input array als voor de prefix resp postfix
        for(int i = 0, j =nums.size(); nums.size();i++,j--)            
        {
            // vermenigvuldigen met de vorige: bij de eerste en laatste is er nog geen waarde (want 
            // out of bounds. Dus daarom doen we bij initialisatie en declaratie van de vector
            // een plus 1 erachter.
            prefix [i] = prefix[i]*prefix[i-1];
            // Hier dus j+1 want index hoger: ik denk dat je de array dan dus vanaf achteraan 
            // invult? kan dat?
            suffix [j] = suffix[j]*suffix[j+1];

        }
        // het resultaat berekenen we na prefix en suffix gevuld te hebben dus opnieuw
        // initialseer met 'k'
        for(int k=0; k = nums.size(); k++)
        {
            // Het resultaat in k is de waarde op de prefix * suffix. 
            // Als k = 3 (index 3) dan moeten we uit prefix 2 en suffix 4 pakken om te vermendigvuldigen
            result[k] = prefix[k-1]*suffix[k+1];
        }
        return result;
    }
};

ostream& operator<<(ostream& os, const vector<int>&nums)
{
    for(int number:nums)
    {
        // Ieder getal uit de vector los printen
        os<<number<<" ";
    }
    return os;
};

int main()
{
        Solution sol;
        vector<int>nums = {2,3,5,8,9,6};
        vector<int>answer = sol.ProductOfArrayExceptSelf(nums);
        cout<<answer<<endl;

}
