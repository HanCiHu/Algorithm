#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct queue{
    int count;
    struct node *front;
    struct node *back;
}               queue;

typedef struct node{
    int data;
    struct node *next;
}               node;


void push(queue *Q, int data){
    node *newNode = (node*)malloc(sizeof(node *));
    newNode->next = NULL;
    newNode->data = data;
    if (Q->count == 0){
        Q->front = newNode;
        Q->back = newNode;
    }
    else{
        Q->back->next = newNode;
        Q->back = newNode;
    }
    Q->count++;
    return ;
}

int pop(queue *Q){
    if (Q->count == 0){
        return -1;
    }
    struct node *p = Q->front;
    int data = p->data;
    p = p->next;
    Q->front = p;
    Q->count --;
    return data;
}

int empty(queue *Q){
    if (Q->count == 0){
        return 1;
    }
    else{
        return 0;
    }
}

int front(queue *Q){
    if(Q->count == 0){
        return -1;
    }
    return Q->front->data;
}

int back(queue *Q){
    if(Q->count == 0){
        return -1;
    }
    return Q->back->data;
}

int main(){
    struct queue *Q = (queue*)malloc(sizeof(queue*));
    Q->count = 0;
    Q->back = NULL;
    Q->front = NULL;

    int count = 0;
    int i = 0;
    int result_index = 0;
    char command[100010];
    int *result;
    int j = 0;
    int data = 0;

    scanf("%d\n",&count);
    result = (int*)malloc(sizeof(int)*count);

    while (i < count){
        gets(command);
        if(!strcmp(command,"pop")){
            result[result_index++] = pop(Q);
        }
        else if(!strcmp(command,"size")){
            result[result_index++] =  Q->count;
        }
        else if(!strcmp(command,"empty")){
            result[result_index++] =  empty(Q);
        }
        else if(!strcmp(command,"front")){
            result[result_index++] = front(Q);
        }
        else if(!strcmp(command,"back")){
            result[result_index++] = back(Q);
        }
        else if(command[1] == 'u'){
            while (command[j] != '\0'){
                if (command[j] >= '0' && command[j] <='9'){
                    data = (data * 10) + (command[j] - '0');
                }
                j++;
            }
            push(Q,data);
        }
        i++;
        j = 0;
        data = 0;
    }
    i = 0;
    while (i < result_index){
        printf("%d\n",result[i]);
        i++;
    }
    return 0;
}