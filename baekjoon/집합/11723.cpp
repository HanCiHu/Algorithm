#include<iostream>
#include<cstring>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	int cnt;
	string cmd;
	int a;
	cin >> cnt;
	bool s[21] = {false};
	while (cnt--){
		cin >> cmd;
		if (cmd == "add"){
			cin >> a;
			s[a] = true;
		}
		else if (cmd == "check"){
			cin >> a;
			printf("%d\n",s[a]);
		}
		else if (cmd == "remove"){
			cin >> a;
			s[a] = false;
		}
		else if (cmd == "toggle"){
			cin >> a;
			if (s[a]) s[a]=false;
			else s[a]=true;
		}
		else if (cmd == "all"){
			memset(s,true,sizeof(s));
		}
		else {
			memset(s,false,sizeof(s));
		}
	}
}