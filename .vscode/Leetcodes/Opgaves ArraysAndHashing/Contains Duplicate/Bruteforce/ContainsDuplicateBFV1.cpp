#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
public:
    bool ContainsDuplicate(vector<int>&nums)
    {
        for(int i = 0; i< nums.size(); i++)
        {
            // Let op: j = i + 1, niet j = 1: dan wordt in de volgende loop met zichzelf vergeleken
            // for loop: of '< nums.size()' of '<=nums.size()-1'

            for(int j = i+1;j <nums.size(); j++)
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
    // Object aanmaken
    Solution s;
    // Door te geven vector
    vector<int> nums = {3,1,4,6,5,2,4}; //Testcase zie onder
    // Memberunctie oproepen op object (zonder 's.' kan niet want memberfunctie hoort bij een class)
    bool answer = s.ContainsDuplicate(nums);
    // Gebruik boolalpha om 'true' of 'false' te krijgen (anders krijg je 1)
    cout<<boolalpha<<answer<<endl;
};

//Als testcase:
// Lege vector nums = {};
// Een getal nums = {1};
// Zonder duplicaten = {1,2,3,4}