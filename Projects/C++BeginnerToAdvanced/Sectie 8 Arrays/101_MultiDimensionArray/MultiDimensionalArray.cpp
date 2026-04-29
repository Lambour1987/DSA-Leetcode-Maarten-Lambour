// 28-4-2026: 2d array is eigenlijk een lange single dimension array
// Vergelijk ook met heap en rowmajor en column major etc


#include <iostream>
#include <stdlib.h>

using namespace std;


// BELANGRIJK: Een 2d array wordt eigenlijk 1d opgeslagen in het geheugen. Mentaal denken
// wij gewoon aan een 2d array en gaan we er ook doorheen met een geneste loop!
// Maar dit zou in theorie ook kunnen met 1 enkele loop.

// BELANGRIJK II: Je kan dus in theorie ook een 3D of nD array hebben. Het gewoon doorzoeken (ieder
// element 1x doorzoeken) is gewoon O(n). Want je doet verder geen onderlinge vergelijkingen.
int main()
{
    // Initialiseren van een 2d array

    // Doorzoeken van een 2d array
}