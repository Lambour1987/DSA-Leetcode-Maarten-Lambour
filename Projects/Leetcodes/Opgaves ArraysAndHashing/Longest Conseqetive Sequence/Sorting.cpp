#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
    public:
        int LSC(vector<int>&nums)
        {
            // Als reeks leeg is, return false
            if(nums.empty())
            {
                return 0;
            }

            // Sorteer de inputvector
            sort(nums.begin(),nums.end());

            // Loop door gesorteerde array en check of ieder element 1 hoger is dan de vorige. A
            // Als gelijk. Skip. Als niet 1 hoger. Einde reeks. Nieuwe reeks starten
            
            int maxreeks = 1;
            
            //Dus let op: dit is een reeks van een subset, maar die zetten we dus boven de for loop
            int reeks = 1;

            // Doe maar size. Dus of <=size-1 of <size.
            // Begin bij 1, want we gaan sorteren-> vergelijken
            for(int i=1;i<nums.size();i++)
            {
                // Als huidig 1 groter is dan vorige dan kan reeks omhoog
                if(nums[i] == nums[i-1]+1)
                {    
                    reeks++;
                }
                // Als huidig nummer gelijk is (kan je hier dan continue doen?)
                else if(nums[i]==nums[i-1])
                {
                    continue;
                }
                else
                {
                // Anders reeks opslaan en een nieuwe reeks starten
                    reeks=1;
                }
                //Uiteindelijk moeten we van alle reeksen het maximum nemen.
                maxreeks = max(maxreeks, reeks);
            }
            return maxreeks;

        }
        
}

int main()
{
    Solution sol;
    vector<int> nums = {100,4,200,1,3,2};
    int answer = sol.LSC(nums);
    cout<<"Longest";
};