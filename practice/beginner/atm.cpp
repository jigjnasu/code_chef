/*
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
 */

#include <cstdio>

int main() {
	int needs = 0;
	float total = 0.0f;

	scanf("%d %f", &needs, &total);

	if (needs % 5 || static_cast<float>(needs) + 0.5f > total)
		printf("%.2f\n", total);
	else
		printf("%.2f\n", total - needs - 0.5f);

	return 0;
}
