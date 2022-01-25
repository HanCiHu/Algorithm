#include <stdio.h>

int main(){
  int num;
  int max = -1, index = 0;

  for (int i = 0; i < 9; i++){
    scanf("%d", &num);
    if (num > max) {
      max = num;
      index = i;
    }
  }

  printf("%d\n%d\n", max, index + 1);

}