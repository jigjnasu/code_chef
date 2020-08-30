/*
  Problem : Lucky Four
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 31/08/2020
 */

#include <bits/stdc++.h>

inline int four(const std::string& n) {
    int count = 0;
    for (char c : n)
        if (c == '4')
            ++count;
    return count;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        std::cout << four(std::to_string(n)) << std::endl;
    }

    return 0;
}
