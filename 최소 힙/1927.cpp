#include<queue>
#include<iostream>

using namespace std;

int main(){
	priority_queue<int, vector<int>, greater<int> > q;
	int n,m;
	cin >> n;
	while (n--){
		cin >> m;
		if (m > 0) q.push(m);
		else{
			if (q.empty()) cout << "0" << "\n";
			else{
				cout << q.top() << "\n";
				q.pop();
			}
		}
	}
}