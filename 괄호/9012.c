#include <stdio.h>

char stack[50];
int i = 0;
int j = 0;

int is_empty(){
    if(stack[0] != '\0'){
        return -1;
    }
    else{
        return 0;
    }
}

int pop(){
    if (stack[j - 1] == '('){
        stack[j - 1] = '\0';
        j--;
        return 0;
    }
    else{
        return -1;
    }
}

void push(){
    stack[j] = '(';
    j++;
}

int main(){
    int index = 0;
    char *result[1000];
    char input[50];
    int count;
    scanf("%d",&count);
    while(i < count){
        scanf("%s",input);
        while(1){
        if (input[index] == '('){
            index++;
            push();
        }
        else if(input[index] == ')'){
            index++;
            if(pop()){
                result[i] = "NO";
                i++;
                j = 0;
                break;
            }
        }
        else if(input[index] == '\0'){
            index++;
            if(is_empty()){
                result[i] = "NO";
                i++;
                j = 0;
                break;
            }
            else{
                result[i] = "YES";
                i++;
                j = 0;
                break;
            }
        }
        }
        index = 0;
    }
    i = 0;
    while (i < count){
        printf("%s\n",result[i++]);
    }
}