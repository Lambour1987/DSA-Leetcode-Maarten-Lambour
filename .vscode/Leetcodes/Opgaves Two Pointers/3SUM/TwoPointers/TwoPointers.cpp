// Sorteren en dan 2 pointers gebruiken
// Duplicaten uit input weghalen

//7-4-2026: NOg een keer doen: Let op er moet dus een for loop, met daarin een while loop, met daarin 2 while loops komen
// t.b.v. overslaan duplicates.
// Want ik heb/ had. Binnen de while loop een if statement: dat checkt steeds maar 1x tijdens
// uitvoering van de whileloop of er sprake is van een duplicate, terwijl er meerdere duplicates achter elkaar kunnen komen.
// dit is wel belangrijk ja.
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm> // t.b.v. sort

using namespace std;

class Solution
{
    public:
        vector<vector<int>> ThreeSum(vector<int>&nums)
        {

            // Eerst Vector van vectoren maken om straks combinaties toe te voegen
            // Let op d us maar 1x int.
            vector<vector<int>> Combinaties;

            // Daarna sorteren
            sort(nums.begin(),nums.end());

            //Met een buitenste forloop over de elementen gaan
            //We gaan tot size minus 2, want de een na laatste en laatste zijn linker en rechter pointer
            for(int i=0; i<nums.size()-2; i++)
            //Controleer of huidig element gelijk is aan vorig element. Zo ja: skip element.
            //Check of huidig element van iterator gelijk is aan vorige (begin bij 1)
                if(i>0 && nums[i]==nums[i-1])
                    continue;

                //Target wordt verminderd met dat getal = NewTarget
                int NewTarget = 0 - nums[i];

                //Binnen de forloop gebruiken we 2 pointers: een left op i+1 en een right aan het einde
                //van de array.
                int links = i+1;
                int rechts = nums.size()-1;

                while(links<rechts)
                //Controleer voor left of deze niet gelijk is aan vorig element. WEl gelijk, schuif
                //links een positie naar rechts.
                    if(nums[links]==nums[links-1])
                    {
                        links++;
                    }
                //Controleer voor right of deze niet gelijk is aan vorig (eigenlijk volgende elemnt in array)
                //Indien gelijk, moet right nog een stukje naar links.
                    if(nums[rechts]==nums[rechts-1])
                    {
                        rechts--;
                    }
                //Als links + rechts > newTarget, verschuif rechterpointer naar links r--;
                    if(nums[links]+nums[rechts]>NewTarget)
                    {
                        rechts--;
                    }
                //Als links + recht < target, verschuif linkerpointer naar rechts l++;
                    else if (nums[links]+nums[rechts]<NewTarget)
                    {
                        links++;
                    }
                    else if(nums[links]+nums[rechts]==NewTarget)
                        Combinaties.push_back({nums[i], nums[links], nums[rechts]});

                // Geen oplossing gevonden    
                    else
                    {
                        return {};
                    }
                
        }
};

ostream& operator<<(ostream& os, const vector<vector<int>> answer)
{
    // Zoiets als je ostream wilt gebruiken
    for(auto& combinaties:answer)
        for(auto& getallen: combinaties)
            os<<getallen<<" ";
    return false;
}

int main()
{
    Solution sol;
    vector <int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> answer = sol.ThreeSum(nums);
    cout<<answer<<endl;


};