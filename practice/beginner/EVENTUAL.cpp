/*
  Problem : Even-tual Reduction
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
    std::cin.ignore();
    while (t--) {
        int n = 0;
        std::cin >> n;
        std::cin.ignore();
        std::string s;
        std::getline(std::cin, s);

        std::vector<int> d(26, 0);
        for (char c : s)
            ++d[c - 'a'];

        std::string r = "YES";
        for (int e : d) {
            if (e & 1) {
                r = "NO";
                break;
            }
        }
        std::cout << r << std::endl;
    }

    return 0;
}
