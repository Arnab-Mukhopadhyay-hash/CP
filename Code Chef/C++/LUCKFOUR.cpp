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
        int count = 0;
        while (n > 0)
        {
            int d = n % 10;
            if (d == 4)
                count++;
            n /= 10;
        }
        cout << count << endl;
    }
    return 0;
}