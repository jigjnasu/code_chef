/*
  Problem : Summer Heat
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/11/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int xa = 0, xb = 0, Xa = 0, Xb = 0;
        std::cin >> xa >> xb >> Xa >> Xb;
        std::cout << std::ceil(Xa / static_cast<float>(xa)) + std::ceil(Xb / static_cast<float>(xb)) << std::endl;
    }

    return 0;
}