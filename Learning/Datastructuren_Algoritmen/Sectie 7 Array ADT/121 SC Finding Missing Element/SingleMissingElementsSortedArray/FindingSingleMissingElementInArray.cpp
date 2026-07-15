//15-4-2026: Finding Single Missing element in an (sorted) array
// Is eigenlijk al een bucket
// Foutje: Debuggen
// Ook niet iets met een heap?
// Dit is Sum of First and Natural Numbers: n(n+1)/2

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
        int SingleMissingMogelijkheid1(vector<int>&nums)
        {
            //Meerdere mogelijkheden. Als input:
            // index:   0 1 2 3 4  5 
            // elem:    5 6 7 8 10 11 
            // Dus waarde element minus index = afstand;
            // als afstand tussen huidige en vorige groter is, dan is er een waarde overgeslagen
            // dus tussen 8 en 3 = 5, vervolgens 10 en 4 = 6. Dus daartussen zit het missende
            // getal: dat is element op huidige index 10 + element op vorige index 8 delen door 2

            int i=0;
            int afstand = nums[0] - i;
            for(i=1; i<=nums.size(); i++);
            {
                //als huidige waarde groter is dan de afstand dan 
                if(nums[i]>nums[i-1])
                {
                    //Bereken en retourneer
                    return (nums[i]-nums[i-1])/2;
                }
            }
            return -1;

        }

        int SingleMissingMogelijkheid2(vector<int>&nums)
        {
        // Andere oplossing: gewoon beginnen bij het begin en denken: vorig element is huidig getal min 1?
        // Waarom niet volgend element = huidig getal +1? omdat we out of bound kunnen zijn?
        // Denk wel aan als de reeks gewoon is 0-2-4-8-10. Dan gaat minus 1 en plus 1 niet op. 
            {
                // Ook checken: ik maak een nieuwe functie waar hier afstand gewoon weer belangrijk is
                // Dan kan ik beter een globale variabele maken?
                int i = 0;
                int afstand = nums[i]-i;
                for(i=1; i<nums.size();i++)
                    if(nums[i+1]-nums[i]>afstand)
                    {
                        // Dan kan je het element van nums[i-1] nemen en daar + 1 bij doen (dat is het getal dat ontbreekt)
                        return nums[i-1]+1;
                }
                return -1;
            }

        }

        int SingleMissingMogelijkheid3(vector<int>&nums)
        {
            // Kan ook met whileloop? ga door zolang elementen niet verschillen in afstand. Return als verschil optreedt?
            // Aftand moet gelijk blijven? Kan je dan doen: while nums[i]-nums[i-1] gelijk is aan afstand doorgaan
            // Moet je dan if doen?
            int i = 0;
            int afstand = nums[i]-i;
            while(nums[i]-i==afstand)
            {
                i++;
            }
            return -1;
        }

        


        //hashset: voeg toe aan set en sorteer maargoed dat heeft geen zin hier


        //Bucketsort? (2 varianten): Dat is voor duplicaten handig? Hier niet echt

        // Blijkbaar ook nog met een Binary Search: zoek break point
};

int main()
{
    Solution sol;
    vector<int>nums = {1,2,3,4,5,6,8,9,10,11,12};
    int answer = sol.SingleMissingMogelijkheid1(nums);
    cout<<answer<<endl;

}