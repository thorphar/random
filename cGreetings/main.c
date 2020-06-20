#include <stdio.h>

int main(int argc, char *argv[]){
    char strName[512];
    printf("Enter your name: ");
    scanf("%s", strName);
    printf("Your name is: %s\n", strName);
    return 0;
}