/*
  Problem Code : JOHNY
  Problem : Uncle Johny
  Author : Rakesh Kumar
  Date: 02/02/2021
*/

#include <bits/stdc++.h>

inline int find(const std::vector<int>& v, int k) {
    int s = 0;
    int e = v.size() - 1;
    int r = 0;
    while (s <= e) {
        if (s == e) {
            r = s + 1;
            break;
        }

        const int m = (s + e) >> 1;
        if (v[m] == k) {
            r = m + 1;
            break;
        } else if (k < v[m]) {
            e = m - 1;
        } else {
            s = m + 1;
        }
    }

    return r;
}

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

        int k = 0;
        std::cin >> k;
        k = v[k - 1];
        std::sort(v.begin(), v.end());
        std::cout << find(v, k) << std::endl;
    }

    return 0;
}
