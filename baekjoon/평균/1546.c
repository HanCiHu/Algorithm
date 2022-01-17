#include<stdio.h>

int main(){
  int N, num, max = -1; scanf("%d", &N);
  double arr[1000] = {0, };
  for (int i = 0;i < N; i++){
    scanf("%d", &num);
    arr[i] = num;
    if (max < num) max = num;
  }

  double sum = 0;

  for (int i = 0; i < N; i++){
    sum += arr[i] / max * 100;
  }
  printf("%f\n", sum / N);

}