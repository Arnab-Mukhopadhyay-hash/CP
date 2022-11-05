#include <bits/stdc++.h>
using namespace std;
int sumN(int n)
{
    int sum = (n * (n + 1)) / 2;
    return sum;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        if (n == 0)
            cout << n << endl;
        else
        {
            if (sumN(n) % 2 == 0)
                cout << n << endl;
            else
                cout << n - 1 << endl;
        }
    }
    return 0;
}