#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;



void pre()
{
    fastio;

    
}

void solve(int tc)
{
    //input an array then bubble sort it and hold some extra space of 10000KB
    int n;
    cin >> n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin >> a[i];
    }
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                swap(a[j],a[j+1]);
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        cout << a[i] << " ";
    }
    cout << '\n';
    //use 10000KB of space random information
    int b[10000];
    for(int i=0;i<10000;i++)
    {
        b[i] = rand();
    }
    for(int i=0;i<10000;i++)
    {
        cout << b[i] << " ";
    }
    cout << '\n';
}

signed main()
{
    pre();

    int tc, tt = 1;
    // cin >> tt;
    
    for(tc = 1; tc <= tt; tc++)
    {
        // cout << "Case " << tc << ": ";
        solve(tc);
        // cout << '\n';
    }

    return 0;
}