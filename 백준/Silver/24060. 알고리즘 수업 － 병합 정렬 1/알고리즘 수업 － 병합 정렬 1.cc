#include <iostream>
using namespace std;

int *tmp;
int save_count = 0, k;

void merge(int *a, int p, int q, int r) {
	int i = p, j = q + 1, t = 0;

	while (i <= q && j <= r) {
		if (a[i] <= a[j]) {
			tmp[t++] = a[i++];
		}
		else {
			tmp[t++] = a[j++];
		}
	} 

	while (i <= q)
		tmp[t++] = a[i++];
	while (j <= r)
		tmp[t++] = a[j++];

	i = p, t = 0;
	while (i <= r && ++save_count) {
		a[i++] = tmp[t++];
		if (save_count == k) {
			cout << tmp[t - 1];
		}
	}
}

void merge_sort(int *a, int p, int r) {
	if (p < r) {
		int q = (p + r) / 2;
		merge_sort(a, p, q);
		merge_sort(a, q + 1, r);
		merge(a, p, q, r);
	}
}

int main() {
	int n, *arr;

	cin >> n >> k;
	arr = new int[n];
	tmp = new int[n];
	
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	merge_sort(arr, 0, n - 1);
	if (save_count < k)
		cout << -1;
}