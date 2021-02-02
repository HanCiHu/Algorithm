#include<queue>
#include<cstdio>

using namespace std;

int main(){
	priority_queue<int, vector<int>, greater<int> > q;
	int n,m;
	scanf("%d",&n);
	while (n--){
		scanf("%d",&m);
		if (m > 0) q.push(m);
		else{
			if (q.empty()) printf("0\n");
			else{
				printf("%d\n",q.top());
				q.pop();
			}
		}
	}
}