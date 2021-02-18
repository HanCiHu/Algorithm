#include<iostream>
using namespace std;

int step[4] = {0, };
int dp[4][10001] = {0, };
int dis = 0;

int func(int x, int ans){
	if (x >= dis)
		return 0;
	for (int i = 0; i < 3; i++){
		func(x + step[i], ans + 1);
	}
	return ans;
}

int main(){
	for (int i = 0; i < 3; i++){
		cin>>step[i];
	}
	cin>>dis;

	cout << func(0,0) << endl;
}
