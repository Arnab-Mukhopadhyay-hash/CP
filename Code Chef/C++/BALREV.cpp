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
        string s;
        cin >> s;
        // int one = 0, zero = 0;
        // for (int i = 0; i < s.length(); i++)
        // {
        //     if (s[i] == '0')
        //         zero++;
        //     else if (s[i] == '1')
        //         one++;
        // }
        // while (zero--)
        //     cout << 0;
        // while (one--)
        //     cout << 1;
        // cout << endl;

        /* METHOD 2*/
        sort(s.begin(), s.end());
        cout << s << endl;
    }
    return 0;
}