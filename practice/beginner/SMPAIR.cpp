/*
  Problem : The Smallest Pair
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
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

        int a = 0, b = 0;
        std::cin >> a >> b;
        if (a > b) {
            a ^= b;
            b ^= a;
            a ^= b;
        }

        for (int i = 2; i < n; ++i) {
            int e = 0;
            std::cin >> e;
            if (e < a) {
                b = a;
                a = e;
            } else if (e < b) {
                b = e;
            }
        }
        std::cout << a + b << std::endl;
    }

    return 0;
}
