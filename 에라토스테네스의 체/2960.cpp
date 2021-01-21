#include<iostream>

using namespace std;

int main(){
	int N,K;
	cin >> N >> K;
	int cnt = 0;
	int arr[1005] = {0, };
	for (int i = 2; i <= N; i++)
		arr[i] = i;
	for (int i = 2; i <=N; i++){
		for (int j = 1; j*i <= N; j++){
			if (arr[i*j] == 0) continue;
			arr[i*j] = 0;
			cnt++;
			if (cnt == K){
				cout << i*j;
				return 0;
			}
		}
	}
}