# include<iostream>
# include<vector>
using namespace std;

int N,M;
vector<int> map[1001];
bool visit[1001] = { false };   //basic value = true

void loop(int x){
    visit[x] = true;
    for (int i = 0; i < map[x].size(); i++){
        int next = map[x][i];
        if (!visit[next])
            loop(next);
    }
}

int main(){
    int x,y;
    int ans = 0;
    cin >> N >> M;
    for (int i = 0; i < M; i++){
        cin >> x >> y;
        map[x].push_back(y);
        map[y].push_back(x);
    }
    for (int i = 1; i <= N; i++){
        if (!visit[i]){
            loop(i);
            ans++;
        }
    }
    cout << ans << endl;
}