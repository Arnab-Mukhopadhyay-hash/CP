#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, q, sum = 0, count = 0;
        cin >> n >> q;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            sum += arr[i];
        }
        while (q--)
        {
            int l, r;
            cin >> l >> r;
            int z = l - r + 1;
            if (z % 2 != 0)
                count++;
        }
        cout << sum + count << endl;
    }
    return 0;
}