#include<iostream>
#include<stack>

using namespace std;

int map[101][101] = {0, };
bool visit[101][101];
int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};
int ans = 0;
int N;

bool flagCheck(int& x, int& y){
	for (int i = 0; i < N; i++){
		for (int j = 0; j< N; j++){
			if (!visit[i][j]){
				x = j;
				y = i;
				return true;
			}
		}
	}
	return false;
}

void func(int depth){
	stack<pair<int,int> > s;
	bool flag = true;
	int d = 0;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			if (map[i][j] <= depth) visit[i][j] = true;
		}
	}
	int a,b;
	while (flagCheck(a,b)){
		flag = false;
		s.push(make_pair(a,b));
		visit[b][a] = true;
		while (!s.empty()){
			int x = s.top().first;
			int y = s.top().second;
			s.pop();
			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx >= 0 && nx < N && ny >=0 && ny < N && !visit[ny][nx]){
					s.push(make_pair(nx,ny));
					visit[ny][nx] = true;
				}
			}
		}
		d++;
	}
	if (flag) d++;
	if (ans < d) ans = d;
	return ;
}

int main(){
	int a,mx;
	mx = 0;
	cin >> N;
	for (int i = 0;i < N; i++){
		for (int j = 0; j<N; j++){
			cin >> a;
			map[i][j] = a;
			if (mx < a) mx = a;
		}
	}
	for (int i = 1; i <= mx; i++){
		for (int j = 0; j < N; j++){
			for (int k = 0; k < N; k++){
				visit[j][k] = false;
			}
		}
		func(i);
	}
	cout << ans << endl;
}