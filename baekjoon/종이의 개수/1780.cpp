#include<cstdio>

using namespace std;

int map[3000][3000] = {0, };
int a = 0,b = 0, c = 0;

void func(int x, int y, int l){
	bool flag = true;
	int color = map[y][x];
	if (l == 1){
		if (color == -1) a++;
		else if (color == 0) b++;
		else if (color == 1) c++;
		return ;
	}
	for (int i = 0; i < l; i++){
		for (int j = 0; j < l; j++){
			if (map[i + y][j + x] != color){
				flag = false;
				break;
			}
		}
		if (!flag) break;
	}
	if (!flag){
		func(x,y,l/3);
		func(x+(l/3),y,l/3);
		func(x+(l/3)+(l/3),y,l/3);
		func(x,y+(l/3),l/3);
		func(x+(l/3),y+(l/3),l/3);
		func(x+(l/3)+(l/3),y+(l/3),l/3);
		func(x,y+(l/3)+(l/3),l/3);
		func(x+(l/3),y+(l/3)+(l/3),l/3);
		func(x+(l/3)+(l/3),y+(l/3)+(l/3),l/3);
	}
	else{
		if (color == -1) a++;
		else if (color == 0) b++;
		else if (color == 1) c++;
	}
}

int main(){
	int N;
	scanf("%d",&N);
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			scanf("%d",&map[i][j]);
		}
	}
	func(0,0,N);
	printf("%d\n%d\n%d\n",a,b,c);
}