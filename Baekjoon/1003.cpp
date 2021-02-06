#include <stdio.h>
using namespace std;

int cnt0, cnt1;

int fib(int n) {
	if (n == 0) {
		cnt0++;
		return 0;
	}
	else if (n == 1) {
		cnt1++;
		return 1;
	}
	else {
		return fib(n - 1) + fib(n - 2);
	}
}

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		cnt0 = 0;
		cnt1 = 0;
		int x;
		scanf("%d", &x);
		int result = fib(x);
		printf("%d %d\n", cnt0, cnt1);
	}

	return 0;
}