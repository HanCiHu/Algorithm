#include<iostream>
#include<queue>

using namespace std;

int main(){
	queue<int> q;
	int cnt,a;
	cin >> cnt;
	string cmd;
	while (cnt--){
		cin >> cmd;
		if (cmd == "push"){
			cin >> a;
			q.push(a);
		}
		else if (cmd == "pop"){
			if (q.size() == 0){
				cout << "-1" << "\n";
				continue;
			}
			a = q.front();
			q.pop();
			cout << a << '\n';
		}
		else if (cmd == "size"){
			cout << q.size() << "\n";
		}
		else if (cmd == "empty"){
			cout << q.empty() << "\n";
		}
		else if (cmd == "front"){
			if (q.size() == 0){
				cout << "-1" << "\n";
				continue;
			}
			cout << q.front() << "\n";
		}
		else if (cmd == "back"){
			if (q.size() == 0){
				cout << "-1" << "\n";
				continue;
			}
			cout << q.back() << "\n";
		}
	}
}