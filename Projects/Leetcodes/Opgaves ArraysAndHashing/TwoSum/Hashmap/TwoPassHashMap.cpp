//14-4-2026: The Two Pass: dan gaan we dus eerst de array door en voegen we toe
// aan de hashmap en daarna itereren we (nog een keer door de hashmap?)
// Dit kan sneller en dat legt hij uit in het filmpje: Hier: Two Pass


#include <iostream>
#include <stdlib.h>
#include <unordered_map>
#include <vector>

using namespace std;

//Mappen value -> index

class Solution
{
    public:
        vector<int> TwoSum(vector<int>&nums, int target)
        {
            unordered_map<int,int>seen;
            
            //Pass 1: Maps vullen
            for(int i=0; i<nums.size();i++)
            {

                //BELANGRIJK: Ik had hier: seen.insert({nums[i],i}); Maar nu zie ik ook weer 
                //dat het moet zijn seen[nums[i]] = i;

                // Insert bij map, set en bij vector push_back?
                // Denk eraar dat push_back achteraan invoeren is en een map/ set dat niet uitmaakt of in 
                // ieder geval geregeld wordt door een functie
                // Let op 2 integers toevoegen (waarde, index)
                // Dit itt tot een pair geloof ik?(met first, en second)
                seen[nums[i]]=i;

            }
            // Na het doorlopen van de array en de getallen toegevoegd te hebben aan de hashmap.
            // Dit nog checken: Ik denk: neem het target en haal nums[i] eraf
            // Zoek het resterende in de hashmap, retourneer de index

            // Dus nieuwe for loop

            // PASS 2: Zoeken
            for(int i=0; i<nums.size();i++)
            {
            // target = target - nums[i]; is niet goedd. Moet wel echt een nieuwe zijn.
                int NewTarget = target - nums[i];
                // Let op: We willen dus een if statement combinereen met seen. Dat lukt niet
                // zomaar (dus if(seen.find(newTarget)) kan niet zomaar).

                if(seen.find(NewTarget) !=seen.end()) && seen[NewTarget] !=i);
                {
                    return {seen[NewTarget], i};
                }
                seen[nums[i]]=i;
            }
            return {};
    
        }
};

// Let op we willen dus ieder karakter printen uit resultaat, niet uit
// De array
ostream& operator<<(ostream& os, const vector<int>result)
{
    for(const int num:result)
    {
        os<<num<<" ";
        return os;
    }
}


int main()
{
    Solution sol;
    vector<int>nums = {3,4,5,6}   ;
    int target = 7;
    vector<int> answer = sol.TwoSum(nums,target);
    cout<<answer<<endl;
    
}