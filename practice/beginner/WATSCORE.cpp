/*
  Problem : That Is My Score!
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 29/08/2020
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
        std::vector<int> ank(13, 0);
        while (n--) {
            int p = 0, s = 0;
            std::cin >> p >> s;
            ank[p] = std::max(ank[p], s);
        }
        int total = 0;
        for (int i = 0; i <= 8; ++i)
            total += ank[i];
        std::cout << total << std::endl;
    }

    return 0;
}
