/*
  Problem : Change It
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/08/2020
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0, k = 0;
        std::cin >> n >> k;
        int total = 0;
        while (n--) {
            int m = 0, p = 0;
            std::cin >> m >> p;
            if (k) {
                if (k <= m) {
                    m -= k;
                    k = 0;
                    total += m * p;
                } else {
                    k -= m;
                }
            } else {
                total += m * p;
            }
        }
        std::cout << total << std::endl;
    }

    return 0;
}
