#include<cstdio>

using namespace std;


int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};

char board[21][21]={0, };
bool en[30] = {false};
int N,M,ans = 1;


void func(int x,int y,int dis){
	if (dis > ans) ans = dis;
	for (int i = 0; i < 4; i++){
		int nx = dx[i] + x;
		int ny = dy[i] + y;
		if (nx >= 0 && nx < M && ny >= 0 && ny < N && !en[board[ny][nx]-'A']){
			en[board[ny][nx]-'A'] = true;
			func(nx,ny,dis+1);
			en[board[ny][nx]-'A']= false;
		}
	}
}

int main(){
	scanf("%d %d",&N,&M);
	for (int i = 0; i < N; i++){
		for (int j = 0; j < M; j++){
			scanf(" %c",&board[i][j]);
		}
	}
	en[board[0][0]-'A'] = true;
	func(0,0,1);
	printf("%d\n",ans);
	return 0;
}