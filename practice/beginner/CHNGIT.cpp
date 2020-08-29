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
        int n = 0, m = 0;
        std::cin >> n;
        m = n;
        std::unordered_map<int, int> dict;
        while (n--) {
            int e = 0;
            std::cin >> e;
            ++dict[e];
        }

        int max = 0;
        for (auto m : dict)
            max = std::max(m.second, max);
        std::cout << m - max << std::endl;
    }

    return 0;
}
