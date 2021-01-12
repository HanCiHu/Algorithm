#include<iostream>
#include<utility>
#include<queue>

using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int main(){
	int N,M;
	cin >> N >> M;
	queue<pair<int, int> > q;
	int **map = new int*[M];
	for (int i = 0; i < M; i++){
		map[i] = new int[N];
		for (int j = 0; j < N; j++){
			int a;
			cin >> a;
			map[i][j] = a;
			if (a == 1) q.push(make_pair(j,i));
		}
	}
	while(!q.empty()){
		pair<int, int> position = q.front();
		q.pop();
		for(int i = 0; i < 4; i++){
			int nx = position.first + dx[i];
			int ny = position.second + dy[i];
			if (nx >= 0 && ny >= 0 && nx < N && ny < M && map[ny][nx] == 0){
				q.push(make_pair(nx,ny));
				map[ny][nx] = map[position.second][position.first] + 1;
			}
		}
	}
	int max = -1;
	bool flag = true;
	for (int i = 0; i < M; i++){
		for (int j = 0; j < N; j++){
			if (map[i][j] > max) max = map[i][j];
			if (map[i][j] == 0){
				flag = false;
				max = 0;
				break;
			}
		}
		if (!flag){
			break;
		}
	}
	cout << max - 1;
}