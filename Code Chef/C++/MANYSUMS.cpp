#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int l, r;
        cin >> l >> r;
        cout << (2 * r) - (2 * l) + 1 << endl;
    }
    return 0;
}

/*EXPLANATION:-
l -> least number in the range
r -> greatest number in the range
now the least number that can be made = 2*l
and the greatest number that can be made = 2*r
and all the numbers in between 2*l and 2*r can be made using the given integers, hence we need to find number of integers between 2*l and 2*r, That's It.


Another way could be, lets say we have l and r and we choose any two numbers in between l and r to make an integer (nC2) and add the number of distinct integers lying between l and r
Therefore, number of distinct integers that can be formed = (nC2)+distinct integers between l and r
But, the problem here is if l == r, even then we will be choosing 2 integers even though all the integers are same.
*/