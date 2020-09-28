#include <iostream>
#define MIN(a,b) a<b ? a:b
#define N 4
#define M 14
#define INF 987654321;
using namespace std;
int dp[M+1];
int coin[N] = { 1,4,5,6 };
int main() {
    int i, j;

    for (i = 1; i <= M; i++)
        dp[i] = INF;

    for (i = 0; i < N; i++) {
		cout << "동전 " << coin[i] << "사용시 "<< endl;
        for (j = coin[i]; j <= M; j++) {
            dp[j] = MIN(dp[j], dp[j - coin[i]] + 1);
            cout << j << ' ' << dp[j] << endl;
        }
        cout<<endl;
    }
    cout << dp[M];
}
