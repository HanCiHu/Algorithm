#include <string>
#include <iostream>
#include <map>

using namespace std;

int main(){
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	int n,m;
	cin >> n >> m;

	map<string, int> dict;
	string *arr = new string[n + 1];

	for (int i = 0; i < n; i++){
		string name; cin >> name;

		dict[name] = i + 1;
		arr[i + 1] = name;
	}

	while (m--){
		string input; cin >> input;
		if (input[0] > '0' && input[0] <= '9') cout << arr[stoi(input)] << '\n';
		else cout << dict[input] << '\n';
	}
}