// Container with most Water Two pointers
// Denk nog even aan: hoe je dan altijd het maximum weet te pakken

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
    public:
        int ContainerWithMostWater(vector<int>height)
        {
            // links op 0;
            int left=0;
            // rechts op lengte van height
            int right=height.size()-1; //Dus dezelfde als in de for loop?

            int MaxVolume = 0;

            while(left<right)
            {
                int volume = (right-left)*min(height[right], height[left]);
                if(volume > MaxVolume)
                    MaxVolume = volume;
                
                // Pointer met kleinere hoogte verplaatsen
            
                if(height[left]<height[right])
                    left++;
                else
                    right--;
            }
            return MaxVolume;
        }
};

int main()
{
    Solution sol;
    vector<int> height = {1,7,2,5,4,7,3,6};
    int answer = sol.ContainerWithMostWater(height);
    cout<<answer<<endl;
}