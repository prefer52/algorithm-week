#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

class Number {
public:
	int num, count;
	Number() {
		count = 0;
	}

	bool operator<(Number b) {
		return num < b.num;
	}
};

bool compareNum(Number a, Number b) {
	return a.num > b.num;
}

bool compareCount(Number a, Number b) {
	if (a.count == b.count)
		return a.num < b.num;
	else
		return a.count > b.count;
}

int main() {
	int sum = 0, n, x;
	Number *num = new Number[8001];
	for (int i = 0; i < 8001; i++)
		num[i].num = i - 4000;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		num[x + 4000].count++;
		sum += x;
	}

	// 평균
	cout << (int)round((double)sum / n) << '\n';

	// 중앙값
	int mid = round((double)n / 2);
	int i = 0;
	for (int count = 0; count < mid; count += num[i++].count) {
		if (count + num[i].count >= mid) {
			cout << num[i].num << '\n';
			break;
		}
	}
	// 최빈값
	sort(num, num + 8001, compareCount);
	if (num[0].count == num[1].count)
		cout << num[1].num << '\n';
	else
		cout << num[0].num << '\n';

	// 범위
	int min, max;
	sort(num, num + 8001);
	for (int i = 0; i < 8001; i++) {
		if (num[i].count > 0) {
			min = num[i].num;
			break;
		}
	}
	for (int i = 8000; i >= 0; i--) {
		if (num[i].count > 0) {
			max = num[i].num;
			break;
		}
	}
	cout << max - min << '\n';
}