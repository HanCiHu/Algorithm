#include <iostream>
#include <set>

using namespace std;

int main() {
	int test_case;

	cin >> test_case;

	while(test_case--){
		int N;
		cin >> N;

		multiset<int> s;

		while(N--) {
			char cmd;
			int num;
			cin >> cmd >> num;

			if (cmd == 'I') {
				s.insert(num);
			}
			else {
				if (!s.empty()) {
					if (num == 1) {
						auto it = s.end();
						it--;
						s.erase(it);
					}
					else
						s.erase(s.begin());
				}
			}
		}

		if (s.empty())
			cout << "EMPTY" << "\n";
		else {
			auto it = s.end();
			it--;
			cout << *it << " " << *s.begin() << "\n";
		}
	}

}