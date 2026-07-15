// 8-4-2026 Klopt nog niet, opnieuw doen
// Soort Bruteforce maar ik denk even snel als sliding window


#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;


class Solution
{
    public:
        int BestTime(vector<int>&prices)
        {
            int koopmin = INT32_MAX; // Minimum moet heel hoog beginnen
            int verkoopmax = INT32_MIN; // Maximum moet heel laag beginnen
            int result = 0;

            // Resultaat is: Verkopen op hoogste punt en kopen op laagste punt EN verkoop hoogste punt moet
            // na kopen op laagste punt zijn. Dus (we hebben maar 1 i).
            // Dus....We berekenen per transactie ook het resultaat (en niet achteraf?)
            // Dat is dus: Resultaat

            for(int i = 0; i<prices.size();i++)
            {
                if(prices[i]>verkoopmax)
                {
                    verkoopmax = prices[i];
                }
                if(prices[i]<koopmin)
                {
                    koopmin = prices [i];
                }
                result = verkoopmax-koopmin;

            }
    
            return result;
        }     

};


int main()
{
    Solution sol;
    vector<int> prices = {10,1,5,6,7,1};
    int answer = sol.BestTime(prices);
    cout<<answer<<endl;

}