#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	int a,b,n;
	int left,right;
	while (T--){

		cin >> a;
		vector<int> note1,note2;
		for (int i =0 ;i < a; i++){
			cin >> n;
			note1.push_back(n);
		}
		cin >> b;
		for (int i = 0;i < b; i++){
			cin >> n;
			note2.push_back(n);
		}
		sort(note1.begin(), note1.end());

		for (int j = 0; j < note2.size(); j++){
			int flag = 0;
			left = 0; right = note1.size() - 1;
			while (left <= right){
				int mid = (left+right)/2;
				if (note2[j] == note1[mid]){
					flag = 1;
					break;
				}
				if (note2[j] > note1[mid]) left = mid + 1;
				if (note2[j] < note1[mid]) right = mid - 1;
			}
			cout << flag << '\n';
		}
	}

}