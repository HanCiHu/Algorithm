#include <stdio.h>

int n,m;
int size[1001] = {0, };
int value[1001] = {0, };
int count[1001] = {0, };
int dp[1001][1001][100000] = {0, };

int func(int i, int s, int v){
	if (i >= m) return 0;
	if (dp[i][s][v]) return dp[i][s][v];
	int a = func(i+1, s,v);
	int b = 0;
	if (count[i] > 0 && s + size[i] <= n){
		count[i]--;
		b = value[i]+func(i,s+size[i], v+value[i]);
	}
	dp[i][s][v] = a > b ? a : b;
	return dp[i][s][v];
}

int main(){
	scanf("%d",&n);
	scanf("%d",&m);
	for (int i = 0; i < m; i++)
		scanf("%d",&size[i]);
	for (int i = 0; i < m; i++)
		scanf("%d",&value[i]);
	for (int i = 0; i < m; i++)
		scanf("%d",&count[i]);
	printf("%d\n",func(0,0,0));
}