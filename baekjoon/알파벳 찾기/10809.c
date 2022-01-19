#include <stdio.h>

int main(){
  char str[100]; scanf("%s", str);
  int alphabet[26] = {0, };

  for (int i = 0 ;i < 26; i++) alphabet[i] = -1;

  for (int i = 0; str[i]; i++) if (alphabet[str[i] - 'a'] < 0) alphabet[str[i] - 'a'] = i;
  for (int i = 0; i < 26; i++) printf("%d ", alphabet[i]);
}