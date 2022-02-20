#include <stack>
#include <iostream>

using namespace std;

int graph[101][101] = {0, };
int visit[101] = {0, };

int dfs(int count){
	int ans = 0;
	stack<int> s;

	s.push(1);

	while (!s.empty()){
		int computer = s.top();
		s.pop();

		visit[computer] = 1;

		for (int i = 1; i < count + 1; i++){
			if (visit[i] == 0 && graph[computer][i] == 1){
				visit[i] = 1;
				s.push(i);
				ans++;
			}
		}
	}
	return ans;
}

int main(){
	int n,m;

	cin >> n >> m;

	while (m--){
		int computer1, computer2;

		cin >> computer1 >> computer2;
		graph[computer1][computer2] = 1;
		graph[computer2][computer1] = 1;
	}
	cout << dfs(n) << '\n';
}