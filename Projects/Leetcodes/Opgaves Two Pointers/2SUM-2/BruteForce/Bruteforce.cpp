// Array is al gesorteerd. Bruteforce met pruning

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
    public:
        vector<int> TwoSumII(vector<int>&numbers, int target)
        {
            // edge case hier niet nodig denk ik.
            // start loop i op 0 en loop tot einde;

            for(int i=0;i<numbers.size(); i++)
            {
                // start loop j op i+1 en loop tot einde;
                for(int j=i+1; j<numbers.size();j++)
                {
                    // als i+j gelijk is aan target, retourneer indices
                    if(numbers[i]+numbers[j]==target)
                    {
                        return {i,j};
                    }
                    // als i+j groter is dan target, stop. Anders doorgaan.
                    else if (numbers[i]+numbers[j]>target)
                    {
                        break; //pruning
                    }
                    // i+j kleiner dan target, gewoon doorgaan. Dus niks neerzetten
                    else
                    {
                    // of je zet gewoon niks neer, want hij gaat sowieso door hier.
                        continue;
                    }
                }
            }
            return {};
        }
};

ostream& operator<<(ostream& os, const vector<int>numbers)
{
    for(auto& n:numbers)
    {
        os<<n<<" ";
        
    }
    return os;
}


int main()
{
    Solution sol;
    int target = 9;
    vector<int> numbers = {1,3,4,5,7,10,11};
    vector<int> answer = sol.TwoSumII(numbers, target);
    cout<< answer <<endl;

    return 0;
}   