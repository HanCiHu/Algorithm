#include<iostream>
#include<queue>

using namespace std;

#define endl "\n"

int N,startX,startY,dstX,dstY;
int dx[] = {1,2, 2, 1,-1,-2,-2,-1};
int dy[] = {2,1,-1,-2,-2,-1, 1, 2};
int visit[301][301] = {0, };

void func(){
	queue<pair<int, int> >q;
	q.push(make_pair(startX,startY));
	visit[startY][startX] = 1;
	while (!q.empty()){
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		if (x == dstX && y == dstY){
			cout << visit[y][x] - 1 << endl;
			return ;
		}
		for (int i = 0; i < 8; i++){
			int nx = x+dx[i];
			int ny = y+dy[i];
			if (nx >=0 && nx < N && ny >=0 && ny < N && !visit[ny][nx]){
				visit[ny][nx] = visit[y][x] + 1;
				q.push(make_pair(nx,ny));
			}
		}
	}

}

int main(){
	int testCase;
	cin >> testCase;
	while (testCase--){
		cin >> N;
		cin >> startX >> startY;
		cin >> dstX >> dstY;
		func();
		for (int i = 0 ;i < N; i++){
			for (int j = 0; j < N; j++){
				visit[j][i] = 0;
			}
		}
	}
}