#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

map<int, vector<int> > graph;
map<int, bool> visit;

void dfs(int root){
	stack<int> s;

	s.push(root);

	while (!s.empty()){
		int node = s.top();
		s.pop();

		if (!visit[node]) cout << node << ' ';

		visit[node] = true;

		for (int i = 0 ; i < graph[node].size(); i++){
			if (!visit[graph[node][i]]) s.push(graph[node][i]);
		}

	}
}

void bfs(int root){
	queue<int> q;

	q.push(root);
	visit[root] = true;
	
	while (!q.empty()){
		int node = q.front();
		q.pop();

		cout << node << ' ';

		for (int i = graph[node].size() - 1; i >= 0; i--){
			if (!visit[graph[node][i]]) {
				q.push(graph[node][i]);
				visit[graph[node][i]] = true;
			}
		}
	}
}

int main(){
	int N,M,root;
	cin >> N >> M >> root;

	for (int i = 0 ; i < M; i++){
		int start, end;
		cin >> start >> end;

		graph[start].push_back(end);
		graph[end].push_back(start);
	}

	for (int i = 1; i <= N; i++) {
		sort(graph[i].rbegin(), graph[i].rend());
		visit[i] = false;
	}

	dfs(root);
	cout << '\n';
	for (int i = 1 ; i <= N; i++) visit[i] = false;
	bfs(root);
	cout << '\n';
}
