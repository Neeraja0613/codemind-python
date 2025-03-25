#include <stdio.h>
#include <string.h>

int main() {
    char n[50];  // Assuming the input string won't exceed 50 characters
    scanf("%s", n);

    if (strcmp(n, "WECNITK") == 0) {
        printf("Welcome to Web Club!\n");
    } else {
        printf("Access denied\n");
    }

    return 0;
}
