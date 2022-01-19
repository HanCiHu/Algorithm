#include <stdio.h>

int main(){
	int arr[42] = {0, };
	int num, result = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &num);
		arr[num % 42]++;
	}

	for (int i = 0; i < 42; i++) if (arr[i] > 0) result++;

	printf("%d\n", result);
}