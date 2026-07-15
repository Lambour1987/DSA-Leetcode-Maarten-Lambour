// 15-4-2026 Binary Search met 2 functies in public en private
// Het is ook mogelijk deze op te lossen in 1 functie. Dit nog doen
// Daarnaast natuurlijk met een while loop

#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution
{
    public:
    // Een public class voor 'search'. De gebruiker weet niet dat het om een binary search gaat
        int Search(vector<int>&nums, int target)
        {
            //Hier geven we door als argument: links, rechts, vector en target
            // kan in 1 regel, voor het overzicht doe ik er 2
            int links = 0;
            int rechts = nums.size()-1;
            // Check: is dit logisch dat het &nums is? Nee dat moet niet.
            return BinarySearch(links, rechts, nums,target);

        }
    
    private:
    // Een private class voor de recursive binary search
    // Deze heeft als parameters left en right. Dat is voldoende, het midden
    // berekenen we binnen de BS functie
        int BinarySearch(int links, int rechts, vector<int>&nums, int target)
        {
            // Stopconditie bepalen
            if(links> rechts)
            {
                return -1;
            }

            // Bereken midden dmv gemiddelde formule (voorkom int overflow dus l+(r-l)/2)
            int midden = links+(rechts-links)/2;

            // Als target lager ligt dan middelste element, dan verplaats rechts naar midden -1
            // Roep opnieuw de functie op
            if(target<nums[midden])
            {
                rechts =  midden - 1;
                // roep functie opnieuw op met nieuwe rechts
                // Denk hier ook weer aan: moet het met &nums?
                // En... Dus: eigenlijk haal je midden steeds weg en bereken je opnieuw, terwijl je
                // links en rechts behoudt en de functie in stopt?
                BinarySearch(links, rechts, nums, target);
            }
            else if (target>nums[midden])
            {
                links = midden + 1;
                BinarySearch(links, rechts, nums, target);
            }
            else //target == midden
            {
                return midden;
            }
        }
};


// Waar zouden we eventuele ostream print neerzetten: private/ public of erbuiten: buiten



int main()
{
    Solution sol;
    vector<int>nums = {-1,0,2,4,6,8};
    int target = 4;
    int answer = sol.Search(nums, target);
    cout<<answer<<endl;

}