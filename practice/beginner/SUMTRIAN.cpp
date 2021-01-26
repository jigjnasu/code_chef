/*
  Problem : Helping Chef
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
        int rows = 0;
        std::cin >> rows;
        std::vector<std::vector<int>> triangle;
        for (int i = 1; i <= rows; ++i) {
            std::vector<int> v;
            for (int j = 0; j < i; ++j) {
                int e = 0;
                std::cin >> e;
                v.emplace_back(e);
            }
            triangle.emplace_back(v);
        }

        for (int row = triangle.size() - 2; row >= 0; --row)
            for (std::size_t col = 0; col < triangle[row].size(); ++col)
                triangle[row][col] += std::max(triangle[row + 1][col], triangle[row + 1][col + 1]);
        std::cout << triangle[0][0] << std::endl;
    }

    return 0;
}


