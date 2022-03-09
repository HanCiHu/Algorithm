#include <iostream>
#include <algorithm>

using namespace std;

int dist[801][801] = {0, };

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N, M, INF = 987654321;
	int start, end, weight;
	cin >> N >> M;

	for (int i = 1; i <= N; i++){
		for (int j = 1; j <= N; j++){
			if (i != j) dist[i][j] = INF;
		}
	}

	while (M--){
		cin >> start >> end >> weight;

		dist[start][end] = weight;
		dist[end][start] = weight;
	}

	int v1,v2;
	cin >> v1 >> v2;

	for (int k = 1; k <= N; k++){
		for (int i = 1; i <= N; i++){
			for (int j = 1; j <= N; j++){
				if (i != j && dist[i][j] > dist[i][k] + dist[k][j]) dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}

	int ans = min(dist[1][v1] + dist[v1][v2] + dist[v2][N], dist[1][v2] + dist[v2][v1] + dist[v1][N]);

	if (dist[1][v1] == INF || dist[v1][v2] == INF || dist[v1][N] == INF || dist[v2][N] == INF) cout << -1;
	else cout << ans;
}