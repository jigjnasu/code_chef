/*
  Problem : Find Remainder
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
        int a = 0, b = 0;
        std::cin >> a >> b;
        std::cout << a % b << std::endl;
    }

    return 0;
}
