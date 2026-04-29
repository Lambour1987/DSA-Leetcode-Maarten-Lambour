// 20-4-2026: Dus Beslisboom mogelijk: zowel wel/ niet opnamen als 

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
    public:
        vector<vector<int>> CombinationSum(vector<int>&nums, int target)
        {   
            // Recursief, dus Basecase zoeken. Dat wanneer we boven het target uitkomen,
            // of als we geen nodes hebben. We roepen steeds opnieuw de formule op met
            // dezelfde nums en we gaan dan tot target is 0?

            
            
            return CombinationSum(&nums, target);
        }

}

