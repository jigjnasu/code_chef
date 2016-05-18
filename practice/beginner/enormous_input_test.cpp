/*
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
 */

#include <cstdio>

typedef unsigned long long int u_longi;

int main() {
	u_longi n = 0;
	u_longi k = 0;

	scanf("%llu %llu", &n, &k);

	u_longi counter = 0;
	while (n--) {
		u_longi t = 0;
		scanf("%llu", &t);
		
		if (t % k == 0)
			++counter;
	}

	printf("%llu\n", counter);

	return 0;
}
