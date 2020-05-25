#include <stdio.h>

int main(){
    int arr[100010] = {0, };
    int i = 0;
    int n;scanf("%d",&n);
    int target;scanf("%d",&target);
    int k = 0;
    int max = 0;
    for (i = 0; i < n ; i++){
        scanf("%d",&k);
        arr[k] = 1;
        if (max < k)
            max = k;
    }
    int end = max;
    int start = target - end;
    int ans = 0;
    while (start < end){
        if (arr[start] + arr[end] == 2 && start + end == target)
            ans++;
        start++;
        end--;
    }
    printf("%d\n",ans);
}