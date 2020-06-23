#include<stdio.h>
int map[51][51] = {0, };
int visit[51][51] = {0, };
int XVec[5] = {1, -1, 0, 0};
int YVec[5] = {0, 0, 1, -1};
int M,N;

void loop(int j, int l){
    int k;
    if (map[j][l] == 1 && visit[j][l] == 0){
        visit[j][l] = 1;
        for (k = 0; k < 4; k++){
            if ((j + XVec[k] >= 0 && l + YVec[k] >= 0) || (j + XVec[k] < M && l + YVec[k] < N))
                loop(j + XVec[k], l + YVec[k]);
        }
    }
}

int main(){
    int c; scanf("%d",&c);
    int i = 0;
    int j = 0;
    int l = 0;

    for (i = 0; i < c; i++){
        int K,X,Y;
        int ans = 0;
        scanf("%d %d %d",&M,&N,&K);
        for (j = 0; j < K; j++){
            scanf("%d %d",&X, &Y);
            map[X][Y] = 1;
        }
        for (j = 0; j < M; j++){
            for (l = 0; l < N; l++){
                if (map[j][l] == 1 && visit[j][l] == 0){
                    loop(j,l);
                    ans++;
                }
            }
        }
        printf("%d\n",ans);
        for (j = 0; j < M; j++){
            for (l = 0; l < N; l++){
                map[j][l] = 0;
                visit[j][l] = 0;
            }
        }

    }
}