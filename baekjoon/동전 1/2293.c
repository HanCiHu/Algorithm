#include <stdio.h>

int n,k;
int coin[101] = {0, };
int dp[10001] = {0, };
int ans = 0;

int func(int v, int i){
    if (v >= k || i == n){
        if (v == k)
            ans++;
        return 0;
    }
    if (v + coin[i] <= k){
        dp[v] = func(v + coin[i], i);
        v = v + dp[v];
    }
    dp[v] = func(v,i + 1);
    v = dp[v];
    return 0;
}

int main(){
    scanf("%d %d",&n,&k);
    int i = 0;
    for (i = 0; i < n; i++)scanf("%d",&coin[i]);
    func(0,0);
    printf("%d\n",ans);
}