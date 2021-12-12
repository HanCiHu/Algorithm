#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int n,m,a,left,right;
	cin >> n;
	vector<int>v1,v2;
	for (int i = 0;i < n; i++){
		cin >> a;
		v1.push_back(a);
	}
	cin >> m;
	for (int i = 0; i<m;i++){
		cin >> a;
		v2.push_back(a);
	}
	sort(v1.begin(),v1.end());
	for (int i = 0; i < v2.size(); i++){
		bool flag = false;
		left = 0;
		right = v1.size() - 1;
		while (left <= right){
			int mid = (left + right) / 2;
			if (v1[mid] == v2[i]){
				flag = true;
				break;
			}
			if (v1[mid] > v2[i]) right = mid - 1;
			if (v1[mid] < v2[i]) left = mid + 1;
		}
		if (flag) cout << "1 ";
		else cout << "0 ";
	}
}