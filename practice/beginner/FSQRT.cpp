/*
  Problem : Finding Square Roots
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 16/01/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int n = 0;
    std::cin >> n;
    while (n--) {
        int m = 0;
        std::cin >> m;
        std::cout << static_cast<int>(std::sqrt(m)) << std::endl;
    }

    return 0;
}
