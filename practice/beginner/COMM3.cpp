/*
  Problem : Three Way Communications
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
 */

#include <bits/stdc++.h>

inline double euclidean_distance(const std::vector<int>& x,
                                 const std::vector<int>& y) {
    return std::sqrt(((x[0] - y[0]) * (x[0] - y[0])) +
                     ((x[1] - y[1]) * (x[1] - y[1])));
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int r = 0;
        std::cin >> r;
        std::vector<std::vector<int>> points;
        for (int i = 0; i < 3; ++i) {
            std::vector<int> p(2, 0);
            std::cin >> p[0] >> p[1];
            points.emplace_back(p);
        }

        std::string res = "yes";
        const double d1 = euclidean_distance(points[0], points[1]);
        const double d2 = euclidean_distance(points[0], points[2]);
        const double d3 = euclidean_distance(points[1], points[2]);
        if ((d1 > r && d2 > r) || (d1 > r && d3 > r) || (d2 > r && d3 > r))
            res = "no";
        std::cout << res << std::endl;
    }

    return 0;
}
