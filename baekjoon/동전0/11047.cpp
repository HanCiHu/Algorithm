#include<iostream>
#include <stack>

using namespace std;

int main(){
	int coins, target;
	stack <int> coin;
	cin >> coins >> target;
	for (int i = 0; i < coins; i++){
		int a;
		cin >> a;
		coin.push(a);
	}
	int ans = 0;
	while (!coin.empty()){
		int a = coin.top();
		while (target - a >= 0){
			target -= a;
			ans++;
		}
		coin.pop();
	}
	cout << ans;
}