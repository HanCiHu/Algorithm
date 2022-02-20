#include <iostream>
#include <map>

using namespace std;

int main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
	int T; cin >> T;

	while (T--){
		int n,m;
		map<int, int> memo;
		cin >> n;

		while (n--) {
			int num; cin >> num;
			memo[num] = 1;
		}

		cin >> m;
		while (m--){
			int num; cin >> num;

			if (memo[num] == true) cout << '1' << '\n';
			else cout << '0' << '\n';
		}
	}
}