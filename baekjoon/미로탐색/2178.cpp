#include<iostream>
#include<queue>
#include<utility>
#include<stdio.h>

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int main(){
	int map[100][100];
	int N,M;
	cin >> N >> M;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			scanf("%1d", &map[i][j]);
		}
	}
	queue<pair<int, int> >q;
	q.push(make_pair(0,0));
	pair <int, int> position;
	while (!q.empty()){
		position = q.front();
		q.pop();
		if(position.first == M-1 && position.second == N-1){
			cout << map[N-1][M-1] << endl;
			break;
		}
		for (int i = 0; i < 4; i++){
			int nx = position.first + dx[i];
			int ny = position.second + dy[i];
			if (nx >=0 && ny >= 0 && nx < M && ny < N && map[ny][nx] == 1){
				map[ny][nx] = map[position.second][position.first] + 1;
				q.push(make_pair(nx,ny));
			}
		}
	}
}