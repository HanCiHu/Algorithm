#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>

#define Max 20

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

bool visit[Max][Max] = {false};
char map[Max][Max];
int w,h;

struct location{
	int h;
	int w;
	int dis;
};

struct location robot;
vector<struct location> v;

void bfs(int a, int b){
	queue<pair<pair<int, int>, int> > q;
	q.push(make_pair(make_pair(a,b),0));
	while (q.empty() == 0){
		int x = q.front().first.first;
		int y = q.front().first.second;
		int dis = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && ny >= 0 && nx < h && ny < w && visit[nx][ny] == false){
				visit[nx][ny] = true;
				if (map[nx][ny] != 'x'){
					q.push(make_pair(make_pair(nx, ny), dis + 1));
					visit[nx][ny] = true;
					if(map[nx][ny] == '*'){
						struct location l;
						l.h = nx;
						l.w = ny;
						l.dis = dis + 1;
						v.push_back(l);
					}
				}
			}
		}
	}
}

bool comp(struct location a, struct location b){  //left >> under >> right >> up
	if (a.dis <= b.dis){
		if (a.dis == b.dis){
			if (a.w < b.w){
				return true;
			}
			else if (a.w == b.w){
				if (a.h < b.h){
					return false;
				}
				return true;
			}
			else
				return false;
		}
		return true;
	}
	return false;
}

int main(){
	cin >> w >> h;
	while (w != 0 || h != 0){
		int check = 0;
		for (int i = 0; i < h; i++){
			for (int j = 0; j < w; j++){
				cin >> map[i][j];
				if (map[i][j] == 'o')
				{
					robot.h = i;
					robot.w = j;
					robot.dis = 0;
				}
				else if (map[i][j] == '*')
					check++;
			}
		}
		if (check == 0){
			cout<<check<<endl;
			break;
		}
		while (1){
			v.clear();
			memset(visit, false, sizeof(visit));
			bfs(robot.h, robot.w);
			if (v.size() == 0){
				if (robot.dis == 0)
					cout << -1 << endl;
				else
					cout << robot.dis << endl;
				break;
			}
			else if (v.size() > 0){
				sort(v.begin(), v.end(), comp);
				map[robot.h][robot.w] = '.';
				map[v[0].h][v[0].w] = 'o';
				robot.h = v[0].h;
				robot.w = v[0].w;
				robot.dis += v[0].dis;
			}
		}
		cin >> w >> h;
		memset(map, 0, sizeof(map));
		memset(visit, false, sizeof(visit));
	}
}
