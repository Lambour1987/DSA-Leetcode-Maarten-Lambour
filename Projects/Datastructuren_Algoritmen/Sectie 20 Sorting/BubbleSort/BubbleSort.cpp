//20-4-2026: BubbleSort: afmaken. Grootste deel al goed. Let op die minus i in de 
// tweede forloop. Is optimalisatie. Mag zonder. Snelheid O(n^2)


#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

void Display(vector<int>&nums)
{
    for(const auto& n:nums)
    {
        cout<<n<<" ";
    }
}

vector<int> BubbleSort(vector<int>&nums)
{
    // Bij BubbleSort moet de grootste achteraan komen
    // Vergelijk de huidige (begin op index 1) met de vorige (index 0)
    // Als de huidige kleiner is dan vorige, dan swappen (zo komt zwaarste achteraan)
    // Anders niks doen. Omdat we dit een aantal keren opnieuw doen denk ik aan 2 geneste forloops

    // Buitenste loop starten we op index 0, eerste getal.
    // Overigens nu is 'size' een memberfunctie van vector toch? Dus geen length. 
    for(int i=0; i < nums.size(); i++)
    {
        // voor de onderlinge vergelijkingen starten we op index 1
        // BELANGRIJK: Niet verplicht maar optimalisatie: dat is -i. 
        for(int j=1; j<nums.size()-i;j++)
        {
            if(nums[j]<nums[j-1])
            {
                // Gewoon swap uit de standaard library gehaald
                swap(nums[j],nums[j-1]);
            }
        }
    }
    return nums;
};







int main()
{
    //Vector nums
    vector<int>nums = {8,5,7,3,2};
    //Roep de display functie aan, voorafgaand sorteren
    Display(nums)
    // Per ronde willen we aangeven hoe de passes zijn.

};