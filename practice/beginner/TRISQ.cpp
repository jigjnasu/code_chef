/*
  Problem : Fit Squares in Triangle
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 31/08/2020
*/

#include <bits/stdc++.h>

using ll = long long int;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        ll r = 0;
        if (n >= 4) {
            if (n & 1)
                n -= 3;
            else
                n -= 2;
            const ll k = n >> 1;
            r = (k * (k + 1)) >> 1;
        }
        std::cout << r << std::endl;
    }

    return 0;
}
