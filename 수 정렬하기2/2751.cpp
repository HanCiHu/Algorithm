#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

int main(){
	int N;
	cin >> N;
	vector<int> a;
	int b;
	for (int i = 0; i < N; i++){
		cin >> b;
		a.push_back(b);
	}
	sort(a.begin(),a.end());
	for (int i = 0; i < N; i++) cout << a[i] << '\n';
}