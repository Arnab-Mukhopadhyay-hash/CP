#include <iostream>
#include <string>
using namespace std;

int main()
{
    int k, n;

    cin >> k >> n;
    string arr[k];
    for (int i = 0; i < k; i++)
    {
        cin >> arr[i];
    }
    for (int j = 0; j < n; j++)
    {
        string str;
        cin >> str;
        bool flag = false;
        for (int i = 0; i < k; i++)
        {
            if (str.find(arr[i]) != string::npos)
            {
                flag = true;
                break;
            }
            else if (str.length() >= 47)
            {
                flag = true;
                break;
            }
        }
        if (flag)
            cout << "Good" << endl;
        else
            cout << "Bad" << endl;
    }
    return 0;
}