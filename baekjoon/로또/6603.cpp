#include<iostream>

using namespace std;

int *selectList;

void Lotto(int len, int lotto[], int count, int k){
	if (len == 6){
		for (int i = 0; i < 6; i++) cout << lotto[i] << " ";
		cout << endl;
		return ;
	}
	for (int i = k; i < count; i++){
		lotto[len] = selectList[i];
		Lotto(len + 1, lotto, count, i + 1);
	}
}

int main(){
	int count = -1;
	while (true){
		cin >> count;
		if (count == 0) break;
		selectList = new int[count];
		int lotto[6] = {0, };
		for (int i = 0; i < count; i++) cin >> selectList[i];
		Lotto(0, lotto, count, 0);
		cout << endl;
		delete[] selectList;
	}
}