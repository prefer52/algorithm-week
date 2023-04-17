#include <iostream>
using namespace std;

void eratosSieve(int size, bool *arr) {
	arr[1] = true;
	for (int i = 2; i <= size; i++) {
		for (int j = i*2; j <= size; j+=i) {
			arr[j] = true;
		}
	}
}

int main() {
	int n;
	cin >> n;

	bool *arr = new bool[1001]{ false };
	eratosSieve(1000, arr);

	int a, count = 0;
	for (int i = 0; i < n; i++) {
		cin >> a;
		if (arr[a] == false)
			count++;
	}

	cout << count;
}