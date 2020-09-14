#include <iostream>

using namespace std;

int map[31][31] = {0, };

int max(int a, int b, int c){
	return (a > b ? a : b) > c ? (a > b ? a : b) : c;
}

int main(){
	int b;
	cin >> b;
	for (int i = 0; i < b; i++){
		for (int j = 0; j < b; j++){
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < b; i++){
		for (int j = 0; j < b; j++){
			if (i == 0){
				if (j == 0)
					continue;
				map[i][j] += map[i][j - 1];
			}
			else if (j == 0){
				map[i][j] += map[i - 1][j];
			}
			else{
				map[i][j] += map[i - 1][j] + map[i][j - 1] - map[i - 1][j - 1];
			}
		}
	}

	int ret = map[0][0];
	int cur = 0;
	int cur1 = 0;
	int cur2 = 0;

	for (int i = 0; i < b; i++){
		for (int di = i; di < b; di++){
			for (int j = 0; j < b; j++){
				for (int dj = j; dj < b; dj++){

					if (di == 0 && dj > 0){
						cur = map[di][dj] - map[di][j];
					}
					else if (dj == 0 && di > 0){
						cur = map[di][dj] - map[i][dj];
					}
					else{
						cur2 = map[di][dj] - map[di][j];
						cur1 = map[di][dj] - map[i][dj];
						cur = map[di][dj] - map[di - 1][dj] - map[di][dj - 1] + map[di - 1][dj - 1];
					}

					if (max(cur,cur1,cur2) > ret)
						ret = max(cur,cur1,cur2);
				}
			}
		}
	}
	cout << ret;
}
