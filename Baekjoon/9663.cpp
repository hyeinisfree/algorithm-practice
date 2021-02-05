#include <iostream>
#include <cmath>
using namespace std;

const int MAX = 15;
int N, cnt;
int col[MAX];

bool promising(int i) {
	for (int j = 0; j < i; j++) {
		if (col[j] == col[i] || abs(col[i] - col[j]) == (i - j)) return false;
	}
	return true;
}

void queen(int i) {
	if (i == N) {
		cnt++;
		return;
	}
	for (int j = 0; j < N; j++) {
		col[i] = j;
		if (promising(i)) queen(i + 1);
	}
}

int main() {
	cin >> N;
	queen(0);
	cout << cnt << endl;
	return 0;
}