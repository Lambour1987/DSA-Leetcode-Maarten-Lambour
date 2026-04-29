#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;

class Solution
{
public:
// check of kan met const auto &: voorkomt kopieren
    bool isValid(string s, string t)
    {
        // Eerst lengte controleren van s en t
        if(s.size() != t.size())
        {
            return false;
        }

        // Zet strings eerst naar lowercase zodat hoofdletters geen invloed hebben op sortering

        transform(s.begin(), s.end(), s.begin(), ::tolower);
        transform(t.begin(), t.end(), t.begin(), ::tolower);

        //Daarna gaan we sorteren
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());

        //Gebruik cout om te checken hoe het sorteren eruit ziet
        cout<<"de string s is nu gesorteerd: "<<s<<endl;
        cout<<"de string t is nu gesorteerd: "<<t<<endl;

        //Verwerk: we gaan dus eerst to lower case en dan sorteren en nite andersom
        // want ASCII zorgt ervoor dat hoofdletters dan eerst komen? dit nog checken


        // Kan simpeler: return
        if(s==t)
        {
            return true;
        }
        else
        {
            return false;
        }

    }
};



int main()
{
    Solution sol;
    string s = "Racecar";
    string t = "Carrace";

    bool answer = sol.isValid(s,t);

    //Gebruik boolalpha om een true or false te krijgen
    cout<<boolalpha<<answer<<endl;

}