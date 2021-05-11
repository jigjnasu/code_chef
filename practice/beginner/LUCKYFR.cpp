/*
  Problem : Lucky Four
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/05/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        std::string s;
        std::cin >> s;
        int count = 0;
        for (char c : s)
            if (c == '4')
                ++count;
        std::cout << count << std::endl;
    }

    return 0;
}
