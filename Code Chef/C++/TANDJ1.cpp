#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, b, c, d, K;
        cin >> a >> b >> c >> d >> K;
        int x = abs(c - a);
        int y = abs(d - b);
        int z = x + y;
        if (K >= z && (K - z) % 2 == 0)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

/* Explanation:-
https://www.youtube.com/watch?v=uynP0kgbqHA

if tom covers extra x1 distance horizontally, then he would have to x1 distance horizontally to come back, also if he covers y1 extra distance vertically then he will have to come back by covering the same distance so extra distance covered = 2(x1+y1)
and z is the minimum distance between tom and jerry, so K has to be >= z,
Now, K = z + 2(x1+y1)
let, x1+y1 = w
then, K = z+2w
=> w = (K-z)/2
now if w is an integer only then K will be valid so, K-z must be divisible by 2.

to find z, just find the distance between tom and jerry horizontally and vertically and then add them up, that is absolute(c-a)+ absolute(d-b)*/