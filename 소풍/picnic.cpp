#include<iostream>

using namespace std;

int n;
bool areFriends[10][10] = {false};

int countPairings(bool taken[10]){
	int firstFree = -1;
	for (int i = 0;i < n; i++){
		if (!taken[i]){
			firstFree = i;
			break;
		}
	}
	if (firstFree == -1) return 1;
	int ret = 0;
	for (int pairWidth = firstFree+1; pairWidth < n; pairWidth++){
		if (!taken[pairWidth] && areFriends[firstFree][pairWidth]){
			taken[firstFree] = taken[pairWidth] = true;
			ret += countPairings(taken);
			taken[firstFree] = taken[pairWidth] = false;
		}
	}
	return ret;
}

int main(){
	int C;
	cin >> C;
	for (int i =0; i < C; i++){
		int peopleNum,edges;
		cin >> n >> edges;
		for (int j = 0; j < edges; j++){
			int a,b;
			cin >> a >> b;
			areFriends[a][b] = true;
			areFriends[b][a] = true;
		}
		bool taken[10] = {false};
		cout << countPairings(taken) << endl;
		for (int j = 0; j < 10; j++){
			for (int k = 0; k< 10; k++){
				areFriends[j][k] = false;
			}
		}
	}
}
