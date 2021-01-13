#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 9999, SWITCH = 10, CLOCKS = 16;

const char linked[SWITCH][CLOCKS + 1] = {
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",
	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
};

bool areAlined(const vector<int>& clocks){
	for (int i = 0; i < CLOCKS; i++){
		if (clocks[i] != 12) return false;
	}
	return true;
}

void push(vector<int>& clocks, int swtch){
	for(int i = 0 ;i < CLOCKS; i++){
		if (linked[swtch][i] == 'x'){
			clocks[i] += 3;
			if (clocks[i] == 15) clocks[i] = 3;
		}
	}
}

int solve(vector<int>& clocks, int swtch){
	if (swtch == SWITCH) return areAlined(clocks) ? 0 : INF;
	int ret = INF;
	for (int i = 0; i < 4; i++){
		ret = min(ret, i + solve(clocks, swtch + 1));
		push(clocks, swtch);
	}
	return ret;
}

int main(){
	int C;
	cin >> C;
	for (int i = 0; i < C; i++){
		vector<int> clocks;
		int a;
		for (int j = 0; j < CLOCKS; j++){
			cin >> a;
			clocks.push_back(a);
		}
		int ans = solve(clocks,0);
		if (ans == INF) cout << -1 << endl;
		else cout << ans << endl;
		clocks.clear();
	}
}