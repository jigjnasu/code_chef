/*
  Problem : Lapindromes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
*/

#include <bits/stdc++.h>

inline void print(const std::vector<int>& v) {
    std::cout << "--------------------------------------------" << std::endl;
    for (int e : v)
        std::cout << e << " ";
    std::cout << std::endl;
    std::cout << "--------------------------------------------" << std::endl;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        std::string s;
        std::cin >> s;

        const int h = s.size () >> 1;
        std::vector<int> l(26, 0);
        std::vector<int> r(26, 0);
        for (int i = 0; i < h; ++i) {
            ++l[s[i] - 'a'];
            ++r[s[s.size() - i - 1] - 'a'];
        }

        std::string res = "YES";
        for (std::size_t i = 0; i < l.size(); ++i) {
            if (l[i] != r[i]) {
                res = "NO";
                break;
            }
        }
        std::cout << res << std::endl;
    }

    return 0;
}
