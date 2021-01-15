/*
  Problem : Second Largest
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 16/01/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        std::vector<int> v(3, 0);
        std::cin >> v[0] >> v[1] >> v[2];
        std::sort(v.begin(), v.end());
        std::cout << v[1] << std::endl;
    }

    return 0;
}
