// Bruteforce, nog geen set gebruikt (dus is nog
// geen volledige uitwerking want er zijn wel duplicates)

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
    vector<vector<int>> ThreeSum(vector<int>&nums)
    {
        vector<vector<int>> Combinatie;
        for(int i=0; i<nums.size();i++)
        {
            for(int j=i+1; j<nums.size();j++)
            {
                for(int k=j+1; k<nums.size();k++)
                {
                    if(nums[i]+nums[j]+nums[k] == 0)
                    {
                        // Let op dus ook weer binnen brackets zetten
                        Combinatie.push_back({nums[i], nums[j], nums[k]});
                    }
                }
            }
        }
        return Combinatie;
    }
};

ostream& operator<<(ostream& os, const vector<vector<int>>&answer)
{
    for(const auto& triplet:answer)
    {
        os<<"[";
        for(int number:triplet)
        {
            os<<number<<" ";
        }
        os << "] ";
    }
    return os;
}

int main()
{
    Solution sol;
    vector<int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> answer = sol.ThreeSum(nums);
    cout<<answer<<endl;

}