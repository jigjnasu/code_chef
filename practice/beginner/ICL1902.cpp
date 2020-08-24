/*
  Problem Code : ICL1902
  Problem : FlatLand
  Author : Rakesh Kumar
  Date: 25/08/2020
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        int chanda_mamas = 0;
        while (n) {
            const int t = static_cast<int>(std::sqrt(n));
            n -= t * t;
            ++chanda_mamas;
        }
        std::cout << chanda_mamas << std::endl;

    }

    return 0;
}
