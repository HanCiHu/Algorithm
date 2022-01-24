#include <stdio.h>

int f(int number) {
	if (number == 0) return 0;
	if(number == 1) return 1;
	return f(number - 2) + f(number - 1);
}

int main(){
  int n; scanf("%d", &n);
  printf("%d\n", f(n));
}