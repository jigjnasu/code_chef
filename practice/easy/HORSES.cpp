/*
  Problem Code : HORSES
  Problem : Racing Horses
  Author : Rakesh Kumar
  Date: 02/02/2021
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
        std::vector<int> v;
        while (n--) {
            int s = 0;
            std::cin >> s;
            v.emplace_back(s);
        }

        std::sort(v.begin(), v.end());

        int r = v[v.size() - 1];
        for (std::size_t i = 1; i < v.size(); ++i)
            r = std::min(r, v[i] - v[i - 1]);
        std::cout << r << std::endl;
    }

    return 0;
}
