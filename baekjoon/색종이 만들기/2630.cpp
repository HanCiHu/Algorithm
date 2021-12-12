#include<cstdio>

using namespace std;

int n,b=0,w=0;
int m[129][129]={0, };

void func(int x, int y, int l){
	int def = m[x][y];
	if (l == 1){
		if (def == 1) b++;
		else w++;
		return ;
	}
	int flag = false;
	for (int i = x; i < l + x; i++){
		for (int j = y; j < l + y; j++){
			if (m[i][j] != def){
				flag = true;
				break;
			}
		}
		if(flag) break;
	}
	if (!flag){
		if (def == 1) b++;
		else w++;
		return ;
	}
	func(x,y,l/2);
	func(x+l/2, y, l/2);
	func(x, y+l/2, l/2);
	func(x+l/2, y+l/2, l/2);
	return ;
}

int main(){
	scanf("%d",&n);
	int k;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			scanf("%d",&k);
			m[i][j] = k;
		}
	}
	func(0,0,n);
	printf("%d\n%d\n",w,b);
}