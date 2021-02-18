#include <iostream>
#include <cstring>
using namespace std;

char arr[100001][200] = {0, };
int n, m, x;
int idx = 0;

void print(){
	int i = 0;
	for (i = 0; i < (n + 1) / 2; i++){
		cout << arr[idx][i];
	}
	i = n % 2 == 0 ? i - 1: i - 2;

	while (i >= 0){
		cout << arr[idx][i];
		i--;
	}
	cout << endl;
	exit(0);
}

void func(int j){
	if (j == (n + 1) / 2){
		strcpy(arr[idx + 1], arr[idx]);
		if (idx == x - 1)
			print();
		idx++;
		return ;
	}

	for (int i = 0; i < m; i++){
		arr[idx][j] = 'a' + i;
		func(j + 1);
	}
}

int main(){
	cin >> n >> m;
	cin >> x;
	func(0);
}
