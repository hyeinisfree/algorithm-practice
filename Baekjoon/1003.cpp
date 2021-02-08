#include <iostream>
using namespace std;

int fibo[40];

int main() {
	fibo[0] = 0;
	fibo[1] = 1;

	for (int i = 2; i < 41; i++) fibo[i] = fibo[i - 1] + fibo[i - 2];

	int t; 
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		if (n == 0) cout << "1 0" << endl;
		else if (n == 1) cout << "0 1" << endl;
		else cout << fibo[n - 1] << " " << fibo[n] << endl;
	}
}