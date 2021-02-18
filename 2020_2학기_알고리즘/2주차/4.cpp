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

	for (int i = 0; i < b; i++){
		for (int di = i; di < b; di++){
			for (int j = 0; j < b; j++){
				for (int dj = j; dj < b; dj++){
					cur = map[di][dj];
					if (i > 0 && j > 0){
						cur1 = cur - map[i - 1][dj] - map[di][j - 1] + map[i - 1][j - 1];
					}
					else if (i > 0){
						cur1 = cur - map[i - 1][dj];
					}
					else if (j > 0){
						cur1 = cur - map[di][j - 1];
					}

					if (cur > ret || cur1 > ret)
						ret = cur > cur1 ? cur : cur1;
				}
			}
		}
	}
	cout << ret;
}
