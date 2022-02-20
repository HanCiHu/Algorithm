#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int n; cin >> n;
	map<string, int> books;

	while (n--){
		string title;
		cin >> title;

		if (books.find(title) == books.end()) books[title] = 1;
		else books[title]++;
	}

	string key;
	int m = 0;
	for (auto iter : books) {
		if (iter.second > m) {
			m = max(m, iter.second);
			key = iter.first;
		}
	}
	cout << key << '\n';
}