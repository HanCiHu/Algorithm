#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include<cstring>

#define Max 20

using namespace std;

struct shark{
	int x;
	int y;
	int exp;
	int size;
};

struct food{
	int x;
	int y;
	int distance;
};

int map_size;
int map[Max][Max] = {0, };
bool visit[Max][Max] = {false};
int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};

struct shark s;
vector<struct food> v;

bool comp(struct food a, struct food  b){
	if (a.distance <= b.distance){
		if (a.distance == b.distance){
			if (a.x <= b.x){
				if (a.x == b.x){
					if (a.y < b.y)
						return true;
					return false;
				}
				return true;
			}
			return false;
		}
		return true;
	}
	return false;
}

void bfs(int a, int b)
{
	queue<pair<pair<int, int>, int> > q;

	q.push(make_pair(make_pair(a,b),0));
	visit[a][b] = true;
	while (q.empty() == 0)
	{
		int x = q.front().first.first;
		int y = q.front().first.second;
		int dis = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && ny >= 0 && nx < map_size && ny < map_size){
				if (visit[nx][ny] == false){
					visit[nx][ny] = true;
					if (map[nx][ny] == 0 || map[nx][ny] == s.size)
						q.push(make_pair(make_pair(nx,ny),dis + 1));
					else if (map[nx][ny] < s.size){
						struct food f;
						f.x = nx;
						f.y = ny;
						f.distance = dis + 1;
						v.push_back(f);
						q.push(make_pair(make_pair(nx,ny), dis + 1));
					}
				}
			}
		}
	}
}

int main(){
	cin >> map_size;
	for (int i = 0; i < map_size; i++){
		for(int j = 0; j < map_size; j++){
			cin >> map[i][j];
			if (map[i][j] == 9){
				s.size = 2;
				s.x = i;
				s.y = j;
				s.exp = 0;
			}
		}
	}
	int ans  = 0;
	while(1){
		v.clear();
		memset(visit, false, sizeof(visit));
		bfs(s.x, s.y);
		if (v.size() == 0){
			cout<<ans<<endl;
			break;
		}
		else if (v.size() >= 1){
			if (v.size() >= 2)
				sort(v.begin(), v.end(), comp);
			s.exp++;
			ans += v[0].distance;
			map[v[0].x][v[0].y] = 9;
			map[s.x][s.y] = 0;
			s.x = v[0].x;
			s.y = v[0].y;
		}
		if (s.exp == s.size){
			s.exp = 0;
			s.size++;
		}
	}
}
