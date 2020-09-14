#include <iostream>

using namespace std;

int max(int a, int b, int c){
	return (a > b ? a : b) > c ? (a > b ? a : b) : c;
}

int main(){
	cout << max(1,5,-1);
}
