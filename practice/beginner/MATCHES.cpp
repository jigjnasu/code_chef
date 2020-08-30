/*
  Problem : Playing with Matches
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 31/08/2020
 */

#include <bits/stdc++.h>

const std::vector<int> M = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

inline int matches(const std::string& n) {
    int total = 0;
    for (char c : n)
        total += M[c - '0'];
    return total;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int a = 0, b = 0;
        std::cin >> a >> b;
        std::cout << matches(std::to_string(a + b)) << std::endl;
    }

    return 0;
}
