// 6-4-2026 Nog een keer doen en afmaken
// Concept juist implementatie nog niet

#include <vector>
#include <iostream>
#include <stdlib.h>

using namespace std;

class Solution
{
    public:
    
    vector<int> TwoSumII(vector<int>&numbers, int target)
    {
        //loop door de array heen
        for(int i=0; i<numbers.size();i++)
        {
            // het nieuwe target is het opgegeven target minus A[i]
            int newTarget = target-numbers[i];
            // Helperfunctie gebruiken
            BinarySearch(vector<int>&nums, newTarget)

        }
    }
};

//Helperfunctie Binary Search (iteratief of recursief?)
// Left en right binnen de functie bouwen
{
    int BinarySearch(const vector<int>&numbers, int left, int right, int newTarget)
    {
        // linker pointer op index i+1 (rechts van element waar je mee bezig bent)
        int left = numbers[i+1]
        // rechter pointer start aan het einde van de array
        int right = numbers.size-1;
        // midden berekenen (left+(left-right)/2 (van de indices toch? niet van de elementen)
        mid = left+(left+right)/2;

        // Eigenlijk hier: check eerst of huidige links, midden rechts toevallig al het te zoeken element is 
        // maar volgens mij kan je dat gewoon overslaan omdat het qua tijd weinig uitmaakt

        while(l<r);
        // Als target hoger ligt dan het midden, dan moet de linker pointer naar het midden +1
        {
            // Als target lager ligt dan het midden, dan moet de rechter pointer naar het midden -1
            if (mid==newTarget)
            {
                return numbers[mid];
            }
            else if (newTarget>mid)
            {
                left = mid + 1;
            }
            // Als target lager ligt dan het midden, dan moet de rechter pointer naar het midden -1
            else (newTarget<mid)
            {
                right = mid -1;
            }
            // Als niet gevonden, return false
            return false;
        }
     
        
    }
}


ostream& operator<<(ostream& os, const vector<int> numbers)
{
    for(auto& n: numbers)
    {
        os<<n<<" ";
        return os;
    }
}



int main()
{
    Solution sol;
    vector<int> numbers = {1,3,4,5,7,10,11};
    int target = 9;
    vector<int> answer = TwoSumII(numbers, target)
    cout<<answer<<endl;

}