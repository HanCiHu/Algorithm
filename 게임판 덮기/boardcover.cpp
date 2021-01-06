#include <iostream>
#include <vector>

using namespace std;
//주어진 칸을 덮을수 있는 4가지 경우의 수
const int coverType[4][3][2] = {
	{{0,0}, {1,0}, {0,1}},
	{{0,0}, {0,1}, {1,1}},
	{{0,0}, {1,0}, {1,1}},
	{{0,0}, {1,0}, {1,-1}}
};

bool cover(vector<vector<int> >& board, int y, int x, int type, int delta){
	bool flag = true;
	for (int i = 0; i < 3; i++){
		int nx = coverType[type][i][1] + x;
		int ny = coverType[type][i][0] + y;
		if (nx < 0 || nx >= board[0].size() || ny >= board.size() || ny < 0) flag = false;
		else if ((board[ny][nx] += delta) > 1) flag = false;
	}
	return flag;
}

int boardCover(vector<vector<int> >&board){
	int x = -1;
	int y = -1;
	for (int i = 0; i < board.size(); i++){
		for (int j = 0; j < board[i].size(); j++){
			if (board[i][j] == 0){
				x = j;
				y = i;
				break;
			}
		}
		if (y != -1) break;
	}
	if (y == -1) return 1;
	int ret = 0;
	for (int type = 0; type < 4; type++){
		if (cover(board,y,x,type,1)) ret += boardCover(board);
		cover(board,y,x,type,-1);
	}
	return ret;
}

int main(){
	int C;
	cin >> C;
	for (int i = 0; i < C; i++){
		int height, width;
		cin >> height >> width;
		vector<vector<int> >board;
		for (int j = 0; j < height; j++){
			vector<int> line;
			for (int k = 0; k < width; k++){
				char a;
				cin >> a;
				//검정색은 1로 저장 , 흰색은 0으로 저장
				if (a == '#') line.push_back(1);
				else line.push_back(0);
			}
			board.push_back(line);
		}
		cout << boardCover(board) << endl;
	}
}