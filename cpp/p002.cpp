#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int total = 0;
    int a = 1; int b = 2; int tmp = 0;
    while(b < 4*pow(10, 6)) {
        if(b%2 == 0) {
            total += b;
        }
        tmp = a;
        a = b;
        b += tmp;
    }
    cout << total << '\n';
    return 0;
}
