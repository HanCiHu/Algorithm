#include <stdio.h>

void binary(long long n){
  if (n == 1) {
    printf("1");
    return ;
  }

  binary(n / 2);
  printf("%lld", n % 2);
}

int main(){
  long long n; scanf("%lld", &n);
  binary(n);
}