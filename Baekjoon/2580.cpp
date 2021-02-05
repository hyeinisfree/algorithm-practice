#include <iostream>
using namespace std;

const int MAX = 9;
int N, cnt;
int arr[MAX][MAX];
bool row[MAX][MAX + 1], col[MAX][MAX + 1], square[MAX][MAX + 1];

int squareId(int row, int col) {
	return (row / 3) * 3 + (col / 3);
}

void sudoku(int cnt) {
	if (cnt == 81) {
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}
		exit(0);
	}

	int r = cnt / 9;
	int c = cnt % 9;

	if (arr[r][c]) sudoku(cnt + 1);
	else {
		for (int i = 1; i <= MAX; i++) {
			if (!row[r][i] && !col[c][i] && !square[squareId(r, c)][i]) {
				arr[r][c] = i;
				row[r][i] = true;
				col[c][i] = true;
				square[squareId(r, c)][i] = true;
				sudoku(cnt + 1);
				arr[r][c] = 0;
				row[r][i] = false;
				col[c][i] = false;
				square[squareId(r, c)][i] = false;
			}
		}
	}
}

int main() {
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			cin >> arr[i][j];
			if (arr[i][j]) {
				row[i][arr[i][j]] = true;
				col[j][arr[i][j]] = true;
				square[squareId(i, j)][arr[i][j]] = true;
			}
		}
	}
	sudoku(0);
	return 0;
}