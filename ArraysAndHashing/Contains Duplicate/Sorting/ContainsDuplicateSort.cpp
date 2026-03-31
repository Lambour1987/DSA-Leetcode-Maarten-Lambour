#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm> // hier voor sort gebruikt

using namespace std;

class Solution
{
public:
    vector<int> ContainsDuplicate(vector<int>&nums)
    {
        sort(nums.begin(),nums.end());
        return nums;
    }
};



int main()
{
    // Maak een object van de Class solution aan
    Solution s;
    // maak een vector met getallen aan
    vector <int> nums = {3,6,2,3};
    // Roep functie van de class aan voor object s met vector nums
    vector<int> nums2= s.ContainsDuplicate(nums);
    // test cout
    for(int num:nums2)
        cout<<num<<endl;
}