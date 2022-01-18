#include <stdio.h>

int main(){
	int N, num, min = 1000001, max = -1000001; scanf("%d", &N);

	while (N--){
		scanf("%d", &num);
		if (num < min) min = num;
		if (num > max) max = num;
	}
	printf("%d %d\n", min, max);

}