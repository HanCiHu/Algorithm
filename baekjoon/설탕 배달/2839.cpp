#include <iostream>

using namespace std;

int min(int a, int b){
	if (a == 0) return b;
	else if (b == 0) return a;
	return a > b ? b : a;
}

int main(){
	int n;
	int arr[5001] = {0, };
	cin >> n;

	arr[3] = arr[5] = 1;

	for (int i = 6; i <= n; i++) {
		int m = min(arr[i - 3], arr[i - 5]);
		if (m > 0) arr[i] = min(arr[i - 3], arr[i - 5]) + 1;
	}

	if (arr[n]) cout << arr[n];
	else cout << -1;
}