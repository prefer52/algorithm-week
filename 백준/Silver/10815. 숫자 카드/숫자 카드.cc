#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(0);

	int n, m, v;

	cin >> n;
	cin.ignore();
	vector<int> card_list;
	string list, num;
	getline(cin, list);

	stringstream sstream1(list);
	while (getline(sstream1, num, ' ')) {
		card_list.push_back(stoi(num));
	}
	sort(card_list.begin(), card_list.end());

	cin >> m;
	cin.ignore();
	vector<int> result;
	getline(cin, list);
	stringstream sstream2(list);
	while (getline(sstream2, num, ' ')) {
		v = stoi(num);
		int min = 0, max = n - 1, mid, find = 0;

		while (min <= max) {
			mid = (min + max) / 2;
			if (card_list[mid] == v) {
				result.push_back(1);
				find = 1;
				break;
			}
			else {
				if (v < card_list[mid])
					max = mid - 1;
				else
					min = mid + 1;
			}
		}
		
		if(find == 0)
			result.push_back(0);
	}

	string re;
	for (int i = 0; i < m; i++) {
		re += to_string(result[i]) + ' ';
	}

	cout << re;
}