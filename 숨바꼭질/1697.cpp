#include<iostream>
#include<queue>

using namespace std;

int main(){
	queue<pair<int,int> > q;
	int dis,target;
	cin >> dis >> target;
	bool visit[100001] = {false};
	q.push(make_pair(dis,0));
	while (!q.empty()){
		int d = q.front().first;
		int cnt = q.front().second;
		if (d == target){
			cout << cnt;
			break;
		}
		q.pop();
		if (d + 1 < 100001 && !visit[d + 1]){
			q.push(make_pair(d+1,cnt+1));
			visit[d+1] = true;
		}
		if (d - 1 >= 0 && !visit[d - 1]){
			q.push(make_pair(d-1,cnt+1));
			visit[d-1] = true;
		}
		if (d*2 < 100001 && !visit[d*2]){
			q.push(make_pair(d*2,cnt+1));
			visit[d*2] = true;
		}
	}
}