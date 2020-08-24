/*
  Problem Code : SNCKYEAR
  Problem : Chef and SnackDown
  Author : Rakesh Kumar
  Date: 25/08/2020
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    std::string s = "1000011101";
    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        if (s[n - 2010] == '1')
            std::cout << "HOSTED" << std::endl;
        else
            std::cout << "NOT HOSTED" << std::endl;
    }

    return 0;
}
