#include<algorithm>
#include<iostream>
#include<deque>

using namespace std;

int main(){
	int cnt,len;
	string cmd,arr;
	cin >> cnt;
	for (int i = 0;i < cnt; i++){
		cin >> cmd >> len >> arr;
		deque<int> a;
		int j = 0;
		while (arr[j] != '\0'){
			if (arr[j] < '0' || arr[j] > '9') j++;
			else{
				int num = 0;
				while (arr[j] >= '0' && arr[j] <= '9'){
					num = num * 10 + (arr[j] - '0');
					j++;
				}
				a.push_back(num);
			}
		}
		j = 0;
		int flag = true;
		int pFlag = true;
		while (cmd[j] != '\0'){
			if (cmd[j] == 'R') flag = !flag;
			else if (cmd[j] == 'D'){
				if (a.empty()){
					pFlag = false;
					break;
				}
				if (flag) a.pop_front();
				else a.pop_back();
			}
			j++;
		}

		if (pFlag){
			cout << '[';
			int num = 0;
			while (!a.empty()){
				if (flag){
					num = a.front();
					a.pop_front();
					cout << num;
				}
				else{
					num = a.back();
					a.pop_back();
					cout << num;
				}
				if (!a.empty()) cout << ",";
			}
			cout << "]\n";
		}
		else{
			cout << "error" << '\n';
		}
	}
}