#include <stdio.h>

int map[26][26] = {0, };
int visit[26][26] = {0, };
int xLocation[5] = {1, -1, 0, 0};
int yLocation[5] = {0, 0, 1, -1};
int count[320] = {0, };
int c = 0;
int size;

 
void swap(int* arr, int left, int right) {
    int temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;
}
 
void bubble_sort(int* arr) {
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < c - 1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr, j, j+1);
            }
        }
    }
}

int loop(int i, int j){
    int k = 0;
    if (map[i][j] == 1 && visit[i][j] == 0){
        count[c]++;
        visit[i][j] = 1;
        for (k = 0; k < 4; k++){
            if ((i + xLocation[k] >= 0 && j + yLocation[k] >= 0) || (i + xLocation[k] < size && j + yLocation[k] < size))
                loop(i + xLocation[k], j + yLocation[k]);
        }
    }
}

int main(){
    scanf("%d", &size);
    int i = 0;
    int j = 0;
    for (i = 0; i < size; i++)
        for (j = 0; j < size; j++)
            scanf("%1d",&map[i][j]);
    for (i = 0; i < size; i++){
        for (j = 0; j < size; j++){
            if (map[i][j] == 1 && visit[i][j] == 0){
                loop(i,j);
                c++;
            }
        }
    }
    printf("%d\n",c);
    bubble_sort(count);
    for (i = 0; i < c; i++)
        printf("%d\n",count[i]);
}