#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm> // hier voor sort gebruikt
#include <unordered_set>

using namespace std;

class Solution
{
public:
    vector<int> SortedVector(vector<int>&nums)
    {
        // Vector gesorteerd
        sort(nums.begin(),nums.end());

        for(int num:nums)
        {
            cout<<num<<endl;
        }
        return nums;
    }

    // Gebruik const omdat we vector niet meer willen veranderen
    bool ContainsDuplicate(const vector<int>&sortednums)
    {
        // We kunnen nu Bruteforce of met hashset door vector gaan. Maar 
        // nu is gesorteerd dus gewoon vergelijken

        for(int i=1;i<sortednums.size();i++)
        {
            // Dus i vergelijken met i-1: begin loop dus op 1 (niet op 0)
            if(sortednums[i]==sortednums[i-1])
            {
                return true;
            }
        }
        return false;
    }
};



int main()
{
    // 1) Maak een object van de Class solution aan
    Solution sol;
    // 2) Maak een vector nums met getallen aan
    vector <int> nums = {3,1,4,6,5,2,4};
    // Roep functie van de class aan voor object s (1) met vector nums (2) en sla op in sortednums
    vector<int> sortednums = sol.SortedVector(nums);
    // Roep setfunctie aan
    bool answer = sol.ContainsDuplicate(sortednums);
    // Print resultaat
    cout<<answer<<endl;
}