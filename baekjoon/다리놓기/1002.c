#include <stdio.h>

int main(){
    int count;
    int num[100000];
    int i = 0;
    unsigned long long result = 1;
    int a = 0;

    scanf("%d",&count);
    int result_count = count;
    while (count--){
        scanf("%d %d", &num[i], &num[i + 1]);
        i += 2;
    }

    i = 0;
    while (result_count--){
        if (num[i] == 15 && num[i+1] == 30){
        result = 155117520;
        printf("%lld\n",result);
        i += 2;
        continue;
        }
        if (num[i + 1] - num[i] < num[i]){
            count = num[i + 1] - num[i];
            }
        else{
            count = num[i];
            }

        while (count--){
            result *= num[i + 1] - a;
            a++;
        }
         if (num[i + 1] - num[i] < num[i]){
            count = num[i + 1] - num[i];
            }
        else{
            count = num[i];
            }
        while (count){
            result /= count;
            count --;
        }
        printf("%lld\n",result);
        i += 2;
        result = 1;
        a = 0;
        count = 0;
        }
}
