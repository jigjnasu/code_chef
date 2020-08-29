/*
  Problem : Puppy and Sum
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/08/2020
 */

#include <bits/stdc++.h>

inline int sum(int n) {
    return (n * (n + 1)) >> 1;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int d = 0, n = 0;
        std::cin >> d >> n;
        while (d--)
            n = sum(n);
        std::cout << n << std::endl;
    }

    return 0;
}
