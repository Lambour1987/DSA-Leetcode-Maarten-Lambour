// Eigen uitwerking: maar ik geef de waarden terug, niet de indices, maar hij kan wel

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
    public:
    // We zetten een forwarde Declaration neer voor de debugger
    // Ipv forward declaration hadden we de functie in geheel ook boven de functie TwoSum kunnen zetten
    void Debughelper(int i, int num, int complement, const unordered_set<int>& set);

    // TwoSum Functie
    vector<int> TwoSum(vector<int>&nums, int target)
    {
    // zoek target minus nums[i] in hashset. Als je die vindt gevonden zo niet voeg
    // nums[i] toe aan hashset

        unordered_set<int> set;

        for(int i=0;i<nums.size(); i++)
        {
            int zoekgetal = (target-nums[i]);
            
            // Oproepen van de debug Helper functie
            // Let op: Bij aanroepen datatype niet nodig, maar wel juiste naam
            Debughelper(i, nums[i],zoekgetal,set);

            // Gebruik count: we zoeken naar een element en niet naar een index (vergelijkbaar met for each loop)            
            if(set.count(zoekgetal))
            {
                return {zoekgetal, nums[i]};//of andersom kan ook
            }
            else
            {
                //Niet gevonden: toevoegen aan hashset met 'insert'. Niet met push_back(vector)
                set.insert(nums[i]);
            }
        }
        return {};

        

        


    }
        // Debug functie: Deze moet buiten de TwoSum functie staan, maar binnen de class
        // Let op dus bij parameters: datatype wel, maar naam mag anders zijn
        // Dit is dus handmatig debuggen
    void Debughelper(int i, int num, int complement, unordered_set<int>& set)
        {
            cout << "i=" << i << ", num=" << num 
                << ", complement=" << complement 
                << ", set bevat: ";
        for (int x : set) cout << x << " ";
        cout << endl;
        }
};



// Helperfunctie om een vector te printen
// We hebben een referentie
// v is de vector
ostream& operator<<(ostream& os, const vector<int>&v)
{
    for(int x:v)
        os << x << " ";
    return os;
};


int main()
{
    Solution sol;
    vector<int> nums = {2,1,5,3};
    int target = 4;
    vector<int> answer = sol.TwoSum(nums,target);
    cout<<answer<<endl;

    //Test case: ik denk dat er geen 2 getallen tot hetzelfde antwoord mogen leiden
}