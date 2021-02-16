#include<queue>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int N,M,K;
bool visit[101][101] = {false};

int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};

vector<int> ans;

bool flagCheck(int& x, int& y){
	for (int i = 0; i < M; i++){
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

void func(){
	int a,b;
	queue<pair<int,int> >q;

	while (flagCheck(a,b)){
		q.push(make_pair(a,b));
		visit[b][a] = true;
		int size = 1;
		while (!q.empty()){
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx >= 0 && nx < N && ny >=0 && ny < M && !visit[ny][nx]){
					q.push(make_pair(nx,ny));
					visit[ny][nx] = true;
					size++;
				}
			}
		}
		ans.push_back(size);
	}
}

int main(){
	int x1,y1,x2,y2;
	scanf("%d %d %d",&M,&N,&K);
	while(K--){
		scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
		for (int i = M-y2; i < M-y1; i++){
			for (int j = x1; j < x2; j++){
				visit[i][j] = true;
			}
		}
	}
	func();
	sort(ans.begin(),ans.end());
	printf("%ld\n",ans.size());
	for (auto a = ans.begin(); a != ans.end(); a++){
		printf("%d ",*a);
	}
}