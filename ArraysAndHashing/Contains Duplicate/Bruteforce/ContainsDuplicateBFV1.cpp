#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
bool ContainsDuplicate(vector<int>&nums)
    {
    // for loop: of '< nums.size()' of '<=nums.size()-1'
        for(int i=0;i<nums.size();i++)
        {
            cout<<nums[i]<<endl;
        }
        return false;
    }
};

int main()
{
    // Object s aanmaken
    Solution s;
    // Door te geven vector
    vector<int> nums = {1,2,3,3};
    // Memberunctie oproepen op object (zonder 's.' kan niet want memberfunctie hoort bij een class)
    s.ContainsDuplicate(nums);

    return 0;

};
