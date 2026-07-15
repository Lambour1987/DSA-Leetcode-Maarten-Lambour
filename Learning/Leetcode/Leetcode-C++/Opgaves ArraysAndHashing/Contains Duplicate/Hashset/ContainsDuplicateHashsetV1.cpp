// Contains Duplicate. Uitwerking met hashset

#include <vector>
#include <stdlib.h>
#include <unordered_set> 
#include <iostream>

using namespace std;

class Solution
{
public:
    bool ContainsDuplicate(vector<int>&nums)
    {
        unordered_set<int> seen;
        for(int i=0;i<nums.size();i++)
        {
            // if en forloops geen ';'
            // gebruik 'count'. Niet find. Find geeft iterator terug
            if(seen.count(nums[i]))
            {
                return true;
            }
            else
            {
            // bij array is het append, hier insert
                seen.insert(nums[i]);
            }
        }
        // Hier hele array doorgegaan, maar niks gevonden
        return false;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {3,1,4,6,5,2,4};
    bool answer = s.ContainsDuplicate(nums);
    cout<<boolalpha<<answer<<endl; 
}
