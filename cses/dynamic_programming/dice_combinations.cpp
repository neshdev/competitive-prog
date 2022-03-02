#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
#include <array>
#include <math.h>


int main()
{
    int n;
    cin >> n;
    auto dp = new ll[n];
    dp[0] = 1LL;
    ll mod = (ll)(pow(10, 9) + 7LL);
    for (ll i = 1; i <= n; i++)
    {
        dp[i] = 0LL;
    }
    
    for (ll x = 0; x < n + 1; x++)
    {
        for (ll dice = 1; dice <= 6; dice++)
        {
            if (x-dice >= 0)
            {
                dp[x] += dp[x-dice];
                dp[x] %= mod;
                // auto t = dp[x]
                // cout << dp[x]  << endl;
                
            }
        }
    }
    cout << dp[n] % mod << endl;
    // for (int i = 0; i < n+1; i++)
    // {
    //     cout << dp[i] << " ";
    // }
    // cout << "ended" << n << endl;
}