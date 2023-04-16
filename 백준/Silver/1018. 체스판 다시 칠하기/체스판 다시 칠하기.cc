#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int m, n;
string *board;
// 0행 0열이 start_color로 시작
void make_chess_board(vector<int*> board_count, char start_color, char reverse_color) {
	char sc = start_color, rc = reverse_color, tmp;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j += 2) {
			if (board[i][j] != sc)
				board_count[i][j] = 1;
		}

		for (int j = 1; j < n; j += 2) {
			if (board[i][j] != rc)
				board_count[i][j] = 1;
		}

		tmp = sc;
		sc = rc;
		rc = tmp;
	}
}

int count_min_change(vector<int*> board_count) {
	int r = 0, c = 0, sum = 0;
	vector<int> change;

	while (true) {
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				sum += board_count[r + i][c + j];
			}
		}
		change.push_back(sum);
		sum = 0;

		if (r + 8 == m && c + 8 == n)
			break;

		if (c + 8 != n) {
			c++;
		}
		else {
			r++;
			c = 0;
		}
	}
	sort(change.begin(), change.end());

	return change[0];
}

int main() {
	cin >> m >> n;
	
	board = new string[m];
	vector<int*> b1Count;
	vector<int*> b2Count;
	for (int i = 0; i < m; i++) {
		cin >> board[i];
		b1Count.push_back(new int[n] {0});
		b2Count.push_back(new int[n] {0});
	}

	make_chess_board(b1Count, 'W', 'B');
	make_chess_board(b2Count, 'B', 'W');

	int a = count_min_change(b1Count);
	int b = count_min_change(b2Count);

	if (a < b)
		cout << a;
	else
		cout << b;
}