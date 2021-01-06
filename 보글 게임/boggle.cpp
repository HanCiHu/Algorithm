#include<iostream>

using namespace std;

int dx[] = {1,-1,0,0,1,-1,1,-1};
int dy[] = {0,0,1,-1,1,-1,-1,1};
char board[5][5];

bool hasWord(int y, int x, const string& word){
}

int main(){
	int count = 0;
	cin >> count;
	for (int i = 0; i < count; i++){
		for (int j = 0; j < 5; j++){
			for (int k = 0; k < 5; k++){
				cin >> board[j][k];
			}
		}
		int wordCount;
		cin >> wordCount;
		string word;
		for (int j = 0; j < wordCount; j++){
			cin >> word;
			if (hasWord(0,0,word)){
				cout << word << " " << "YES";
			}
			else{
				cout << word << " " << "NO";
			}
		}
	}
}