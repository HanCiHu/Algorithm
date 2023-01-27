#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int N, W;
int region1[100001] = {0, };
int region2[100001] = {0, };
int dp[100001][2][2][2][2] = {0, };

int func(int i, int flag1, int flag2, int first1, int first2){
  if (i == N) return 0;
  if (dp[i][flag1][flag2][first1][first2] > 0) return dp[i][flag1][flag2][first1][first2];
  
  int ans = func(i + 1, false, false, first1, first2);
  
  if (N > 1){
    if (region1[i] + region1[i == 0 ? N - 1 : i - 1] <= W && !flag1 && region2[i] + region2[i == 0 ? N - 1 : i - 1] <= W && !flag2){
      if (i == N - 1 && !first1 && !first2) ans = max(ans, 2 + func(i + 1, true, true, true, true));
      else if (i == 0) ans = max(ans, 2 + func(i + 1, true, true, true, true));
      else if (i != N - 1) ans = max(ans, 2 + func(i + 1, true, true, first1, first2));
    }

    if (region1[i] + region1[i == 0 ? N - 1 : i - 1] <= W && !flag1){
      if (i == N - 1 && !first1) ans = max(ans, 1 + func(i + 1, true, false, true, first2));
      else if (i == 0) ans = max( ans, 1 + func(i + 1, true, false, true, first2));
      else if (i != N - 1) ans = max( ans, 1 + func(i + 1, true, false, first1, first2));
    }

    if (region2[i] + region2[i == 0 ? N - 1 : i - 1] <= W && !flag2){
      if (i == N - 1 && !first2) ans = max(ans, 1 + func(i + 1, false, true, first1, true));
      else if (i == 0) ans = max(ans, 1 + func(i + 1, false, true, first1, true));
      else if (i != N - 1) ans = max(ans, 1 + func(i + 1, false, true, first1, first2));
    }
  }

  if (region1[i] + region2[i] <= W){
    if (i == N - 1 && !first1 && !first2) ans = max(ans, 1 + func(i + 1, true, true, first1, first2));
    else if (i != N - 1) ans = max(ans, 1 + func(i + 1, true, true, first1, first2));
  }

  dp[i][flag1][flag2][first1][first2] = max(ans, dp[i][flag1][flag2][first1][first2]);
  return dp[i][flag1][flag2][first1][first2];
}

int main(){
  int T;
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> T;

  for (int i = 0; i < T; i++){
    cin >> N >> W;
    memset(region1, 0, 100001);
    memset(region2, 0, 100001);
    memset(dp, 0, 100001 * 2* 2* 2* 2);
    for (int j = 0; j < N; j++) cin >> region1[j];
    for (int j = 0; j < N; j++) cin >> region2[j];
    cout << (2 * N) - func(0, false, false, false, false) << '\n';
  }
}
