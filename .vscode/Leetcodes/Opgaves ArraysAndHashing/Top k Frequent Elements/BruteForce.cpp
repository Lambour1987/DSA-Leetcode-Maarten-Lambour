// Bruteforce: 

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
    public:
        vector<int> TopKFrequent(vector<int>&nums, int k)
        {
            sort(nums.begin(), nums.end(), greater<int>());
            
            // We maken een lijst waarin zowel het getal als het aantal in voorkomt.
            vector<pair<int,int>> freq; 

            // We starten met 1
            int count = 1;

            //Ga met een forloop door de lijst heen. Binnen de forloop maken we een
            //counter die telt hoevaak eenzelfde getal steeds voorkomt.
            // Als volgende getal niet zelfde is als vorige dan opnieuw

            for(int i=1;i<nums.size();i++)
            {
                if(nums[i]==nums[i-1])
                {
                    // Als zelfde getal dan counter verhogen
                    count++;
                }
                else
                {
                    // Als getal anders dan zowel het (vorige) 
                    // getal als de frequentie (counter) opnemen
                    freq.push_back({nums[i-1], count});
                    count = 1;
                }
            }
            // Met huidige functie zal het laatste element nog niet meegenomen worden dus
            // we moeten dit nog bijvoegen:
            freq.push_back({nums.back(), count});

            // Nu moeten we de frequentiemap sorteren waarbij het 2e getal (count) wordt 
            // gesorteerd van hoog naar laag. (sort(freq.begin(),freq.end() betreft het bereik, niet
            // van hoog naar laag sorteren)). Dat komt na de komma
            sort(freq.begin(), freq.end(),
            // We maken een lambda functie
            // pair<int,int> is een element
            // sort vergelijkt 2 elementen: a en b
            [](const pair<int,int>& a, 
                const pair<int,int>& b)
                {
                    return a.second > b.second;
            });

            // Top k elementen in result: de eerste elementen uit de freq. map
            vector<int> result;
            for(int i = 0; i < k; i++)
                result.push_back(freq[i].first);

            return result;
        }

};

//Helper functie om getallen los te printen
ostream& operator<<(ostream& os, const vector<int>& nums)
{
    for(int getal:nums)
        os<<getal<<" ";
    return os;

};

int main()
{
    Solution sol;
    vector<int> nums = {2,1,300,4,300,2,1,300};
    int k = 2;
    vector<int> answer = sol.TopKFrequent(nums,k);
    cout<<answer<<endl;

}