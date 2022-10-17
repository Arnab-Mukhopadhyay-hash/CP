#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int rn = 0;
        while (n != 0)
        {
            int d = n % 10;
            rn = (rn * 10) + d;
            n /= 10;
        }
        cout << rn << endl;
    }
    return 0;
}