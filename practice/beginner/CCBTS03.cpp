/*
  Problem : Chef and Laddus For Children
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 31/08/2020
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
        std::vector<int> v;
        while (n--) {
            int s = 0;
            std::cin >> s;
            v.emplace_back(s);
        }
        std::sort(v.begin(), v.end());

        int r = v[v.size() - 1];
        for (int i = 0; i + k - 1 < v.size(); ++i)
            r = std::min(r, v[i + k - 1] - v[i]);
        std::cout << r << std::endl;
    }

    return 0;
}
