#include <iostream>
#include <math.h>
using namespace std;

int n_digits(int n);
int n_reversed(int n);
bool isPalindrome(int n);

int main() {
    int pmax = 0; int tmp;
    for(int i = 100; i < 1000; i++) {
        for(int j = i; j < 1000; j++) {
            tmp = i*j;
            if(isPalindrome(tmp) && tmp > pmax) {
                pmax = tmp;
            }
        }
    }
    cout << pmax << '\n';
    return 0;
}

int n_digits(int n) {
    return ceil(log10(n));
}

int n_reversed(int n) {
    if(n < 10) {
        return n;
    }
    else {
        int m = 0;
        for(int j = n_digits(n) - 1; j >= 0; j--) {
            m += (n%10) * pow(10, j);
            n /= 10;
        }
        return m;
    }
}

bool isPalindrome(int n) {
    return n == n_reversed(n);
}
