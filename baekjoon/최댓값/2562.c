#include <stdio.h>

int main(){
  int arr[9] = {0, };
  int max = -1, index = 0;

  for (int i = 0; i < 9; i++){
    scanf("%d", &arr[i]);
  }

  for (int i = 0; i < 9; i++){
    if (arr[i] > max){
      max = arr[i];
      index = i;
    }
  }
  printf("%d\n%d\n", max, index + 1);

}