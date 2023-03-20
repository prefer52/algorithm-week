#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void setEratosSieve(bool* arr, int size) {
	arr[1] = true;

	int max = sqrt(size);
	for (int i = 2; i <= max; i++) {
		if (!arr[i]) {
			for (int j = i * i; j <= size; j += i)
				arr[j] = true;
		}
	}
}

int main() {
	int t, n;
	vector<int> testCase;

	cin >> t;
	if (t == 0)
		return 0;

	cin >> n;
	int max = n;
	testCase.push_back(n);

	for (int i = 1; i < t; i++) {
		cin >> n;
		testCase.push_back(n);
		if (n > max)
			max = n;
	}

	bool *isCompNum = new bool[max + 1]{ false };
	setEratosSieve(isCompNum, max);

	for (int i = 0; i < testCase.size(); i++) {
		for (int j = testCase[i]/2; j >= 0; j--) {
			if (!isCompNum[j] && !isCompNum[testCase[i] - j]) {
				cout << j << ' ' << testCase[i] - j << '\n';
				break;
			}
		}
	}
}