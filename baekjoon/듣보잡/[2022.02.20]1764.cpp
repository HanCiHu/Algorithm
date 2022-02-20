#include <map>
#include <iostream>
#include <string>

using namespace std;

int main(){
	map<string, int> names;

	int n,m, size = 0; cin >> n >> m;

	while (n--){
		string name;
		cin >> name;
		names[name] = 1;
	}

	while (m--){
		string name;
		cin >> name;

		if (names.find(name) != names.end()){
			size++;
			names[name]++;
		}
	}

	cout << size << '\n';
	for (auto p : names) {
		if (p.second == 2) cout << p.first << '\n';
	}
}