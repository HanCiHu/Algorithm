#include<cstdio>
#include<queue>

using namespace std;

int main(){
	int n,m;
	scanf("%d",&n);
	priority_queue<int> q;
	while (n--){
		scanf("%d",&m);
		if (m == 0){
			if (q.empty()) printf("0\n");
			else {
				printf("%d\n",q.top());
				q.pop();
			}
		}
		else q.push(m);
	}
}