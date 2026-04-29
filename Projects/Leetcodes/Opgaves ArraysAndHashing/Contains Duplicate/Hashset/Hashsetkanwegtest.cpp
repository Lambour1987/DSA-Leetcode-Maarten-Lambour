#include <iostream>
#include <stdlib.h>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
    public:
        bool ContainsDuplicate(vector<int>&nums)
        {
            unordered_set<int> seen;

            for(int i = 0; i<nums.size();i++)
            {
                //Zoek voor ieder element of die in de set staat
                //Als die in de set staat, return true, anders toevoegen aan set
                //Return true kan zodra duplicate gevonden is dus binnen de loop

                if(seen.count(nums[i]))
                {
                    return true;
                }
                else
                {
                    seen.insert(nums[i]);
                }

            }
            return false;
        }
};

int main()
{
    Solution sol;
    vector<int>nums = {3,1,4,6,5,2,4};
    bool answer = sol.ContainsDuplicate(nums);
    cout << answer << endl; 

}