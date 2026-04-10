// BruteForce: 2 forloops + sorteren + hashset

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <set>

using namespace std;

class Solution
{
    public:
        vector<vector<int>> ThreeSum(vector<int>&nums)
        {
            //Eigenlijk 2 loops met een hashset
            //We itereren met een for loop door de reeks, bijv de reeks [-1,0,1,2,-1,-4]
            //De loop begint op nums[0]
            //We berekenen de target minus index
            //Voor het resterende deel gebruiken we een hashset (doorloop met for loop)
            //Eerst zoeken of getal bestaat: zo ja dan triplet gevonden, voeg toe aan uitkomst vector<vector<int,int>>
            //Bestaat die niet dan toevoegen aan hashset en doorgaan met iteratie
            //We moeten sorteren gebruiken van de input. anders schijnen we dubbele triplets te krijgen bijv [-1,0,1] en [0,-1,1] 
            // Dat zijn een soort Permutaties dus

            //Maak Hashset
            set<vector<int>> result;

            //Begin: Forloop
            for(int i = 0; i<nums.size(); ++i)
            {
                for(int j=i+1;j<nums.size();++j)
                {
                    //whileloop??
                    //Target verminderen met nums[i]
                    //Eerste loop dus: newTarget1 (4) = 0 - (-4)
                    int newTarget1 = 0 - nums[i];

                    //Verminder newTarget1 ook nog met nums[j], dat wordt dan newTarget2
                    int newTarget2 = newTarget1 - nums[j];

                    //newTarget2 moeten we dan zoeken in de hashset. als die bestaat, triplet
                    // gevonden. Als die niet bestaat: nums[j] toevoegen aan de hashset
                    result.find(newTarget2);






                }
            }
        }

};

ostream& operator<<(ostream& os, const vector<vector<int>> answer)
{
    for(const auto& reeks:answer)
    // hier iets
        for(int getal:reeks)
        {
            os<<getal<<" ";
        }
    }
}

int main()
{
    Solution sol;
    vector<int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> answer = sol.ThreeSum(nums);
    cout<<answer<<endl;
}