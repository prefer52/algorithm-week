#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main() {
	int m, n;

	cin >> m >> n;

	int max = sqrt(n);

	bool *isCompNum = new bool[n + 1]{ false };

	if (n != 1) {
		isCompNum[1] = true;

		for (int i = 2; i <= max; i++) {
			if (!isCompNum[i]) {
				for (int j = i * i; j <= n; j += i) {
					isCompNum[j] = true;
				}
			}
		}

		string primeStr = "";
		int index = 0;
		for (int i = m; i <= n; i++) {
			if (!isCompNum[i]) {
				primeStr += to_string(i) + '\n';
			}
		}

		cout << primeStr;
	}
}