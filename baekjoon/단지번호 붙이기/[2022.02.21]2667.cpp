#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int map[26][26] = {0, };
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
vector<int> v;

void dfs(int i, int j, int n){
  vector<pair<int, int> > s;
  int town = 0;

  s.push_back(make_pair(i, j));
  map[i][j] = 0;

  while (!s.empty()) {
    int x = s.back().first;
    int y = s.back().second;

    s.pop_back();
    town++;

    for (int i = 0 ; i < 4; i++){
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (map[nx][ny] == 1 && nx >= 0 && ny >= 0 && nx < n && ny < n){
        map[nx][ny] = 0;
        s.push_back(make_pair(nx, ny));
      }
    }
  }
  v.push_back(town);
}

int main(){
  int n, town_count = 0; scanf("%d", &n);

  for (int i = 0; i < n; i++){
    for (int j = 0 ; j < n; j++) scanf("%1d", &map[i][j]);
  }

  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      if (map[i][j] == 1) {
        dfs(i, j, n);
        town_count++;
      }
    }
  }

  sort(v.begin(), v.end());

  printf("%d\n", town_count);

  for (int i = 0;i < v.size(); i++) printf("%d\n", v[i]);
}
