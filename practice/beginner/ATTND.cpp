/*
  Problem : Attendance
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/08/2020
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    std::cin.ignore();
    while (t--) {
        int n = 0;
        std::cin >> n;
        std::cin.ignore();
        std::unordered_map<std::string, int> dict;
        std::vector<std::string> names;
        while (n--) {
            std::string s;
            std::getline(std::cin, s);
            names.emplace_back(s);
            std::string f;
            std::istringstream iss(s);
            iss >> f;
            ++dict[f];
        }

        for (const std::string& n : names) {
            std::string f;
            std::istringstream iss(n);
            iss >> f;
            if (dict[f] == 1)
                std::cout << f << std::endl;
            else
                std::cout << n << std::endl;
        }
    }

    return 0;
}
