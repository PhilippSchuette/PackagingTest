#include <stdio.h>
#include "hello.h"
#include "extension1.h"


int main(void) {
    int tmp;
    int x = 1;
    int y = 2;

    tmp = add(x, y);
    printf("%d\n", tmp);

    return 0;
}


int add(int x, int y) {
    say_hi_from_cy();
    return x + y;
}
