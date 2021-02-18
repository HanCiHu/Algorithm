#include<iostream>
#include<algorithm>
#include<vector>

#define endl "\n"

using namespace std;
int N,M;
int visit[10001]={false};
vector<int> v;
vector<int> ans;

void print(){
	for (int i = 0; i < M; i++) cout << ans[i] << " ";
	cout << endl;
}

void func(int cnt){
	if (cnt == M){
		print();
		return;
	}

	for (int i = 0; i < N; i++){
		if (visit[v[i]]) continue;
		visit[v[i]] = true;
		ans.push_back(v[i]);
		func(cnt+1);
		ans.pop_back();
		visit[v[i]] = false;
	}
}

int main(){
	cin >> N >> M;
	int a;
	for (int i = 0; i < N; i++){
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(),v.end());
	func(0);
}