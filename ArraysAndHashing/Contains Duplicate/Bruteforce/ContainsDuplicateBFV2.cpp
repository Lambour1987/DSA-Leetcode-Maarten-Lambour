#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
public:
    bool ContainsDuplicate(vector<int>&nums)
    {
        int i,j;
        for(i = 0; i< nums.size(); i++)
        {
            // Let op: j = i + 1, niet j = 1: dan wordt in de volgende loop met zichzelf vergeleken
            for(j = i+1;j <nums.size(); j++)
            {
                if(nums[i]==nums[j])
                {
                    return true;
                }
                // Dus niet hier 'false' zetten: want dan krijg je direct false als een getal niet overeenkomt
            }
        
        }
        // Hier pas false want je hebt dan de hele array doorlopen
        return false;
    }
};


int main()
{
    Solution s;
    vector<int> nums = {1,2,3,3};
    bool answer = s.ContainsDuplicate(nums);
    // Gebruik boolalpha om 'true' of 'false' te krijgen (anders krijg je 1)
    cout<<boolalpha<<answer<<endl;
};