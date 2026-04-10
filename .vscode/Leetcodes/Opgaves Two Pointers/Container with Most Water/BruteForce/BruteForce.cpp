#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
        int MostWater(vector<int>&height)
        {
            //BF door de indices heengaan

            int maxVolume = 0;
            
            // In de uitwerking doen ze de height size in een losse variabele omdat die vaker voorkomt
            for(int i=0; i<height.size();i++)
            {
                for(int j=i+1; j<height.size();j++)
                {
                    // Oppervlakte is minimum van de twee waarden waar i en j op staan
                    // vermenigvuldigd met de afstand van i en j.
                    int volume = min(height[i],height[j])*(j-i);
                    if(volume>maxVolume)
                    {
                        maxVolume = volume;
                    }
                    
                }
            }
            return maxVolume;   
        }
        
};


int main()
{
    Solution sol;
    vector<int>height = {1,7,2,5,4,7,3,6};
    int answer = sol.MostWater(height);
    cout<<answer<<endl;
}