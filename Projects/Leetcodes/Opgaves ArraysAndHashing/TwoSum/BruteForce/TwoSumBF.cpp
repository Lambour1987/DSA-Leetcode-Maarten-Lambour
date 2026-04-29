#include<iostream>
#include<vector>

using namespace std;

class Solution
{
    public:
        vector<int> TwoSum(vector<int>&nums, int target)
        {
            for(int i = 0; i<nums.size();i++)
            {
                // Ook hier weer j+1 net als bij contains duplicate (en niet bij Valid Anagram BF)
                for(int j=i+1;j<nums.size();j++)
                {
                    if(nums[i] + nums[j] == target)
                        return {i,j};
                }
            }
            return {};
        }
};

// Helperfunctie om een vector te printen
// We hebben een referentie
// v is de vector
ostream& operator<<(ostream& os, const vector<int>& v)
{
    for(int x:v)
        os << x <<" ";
    return os;
}

int main()
{
    Solution sol;
    vector<int>nums = {1,4,2,7};
    int target = 8;
    vector<int> answer = sol.TwoSum(nums,target);
    //Dus: 'answer' is niet te printen als vector. Dus we moeten zodra we cout<< hebben een
    // functie oproepen die answer vertaald naar een vector. Dan wordt << overload (operator overloading)
    cout<<answer<<endl;
}