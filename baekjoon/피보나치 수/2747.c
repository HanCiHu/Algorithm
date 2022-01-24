#include <stdio.h>

int fibbonacci_func(int number) {
	if (number == 0) return 0;
	if (number == 1) return 1;
	int fn2 = 0, fn1 = 1, fn;
	for (int i = 2; i <= number; i++){
		fn = fn1 + fn2;
		fn2 = fn1;
		fn1 = fn;
	}
	return fn;
}

int main(){
  int n; scanf("%d", &n);
  printf("%d\n",fibbonacci_func(n));
}