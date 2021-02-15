#include<cstdio>

int ans = 0;
int n,r,c;

void func(int x, int y, int size){
	if (x == c && y == r){
		printf("%d\n",ans);
		return ;
	}
	if (c >= x && c < x + size && r >= y && r < y + size){
		func(x,y,size/2);
		func(x + size/2, y, size/2);
		func(x,y + size/2, size/2);
		func(x+size/2, y+size/2, size/2);
	}
	else ans += size*size;
}

int main(){
	scanf("%d %d %d",&n, &r, &c);
	func(0,0,(1 << n));
}