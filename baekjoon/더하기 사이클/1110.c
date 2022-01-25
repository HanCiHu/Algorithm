#include <stdio.h>

int main(){
  int n1, n2, origin, count = 0; scanf("%d", &origin);
  n2 = origin;
  do {
    count ++;
    n1 = (n2 % 10 * 10) + ((n2 / 10 + n2 % 10) % 10);
    n2 = n1;
  } while(n1 != origin);
  printf("%d\n", count);
}