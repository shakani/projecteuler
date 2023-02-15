#include <iostream>
#include <cmath>
using namespace std;

long digit_square_sum(long n);
bool hits_89(long n);

int main() {
    long total = 0;
    for(int i = 1; i < pow(10, 6); i++) {
        if(hits_89(i))
            total++;
    }
    cout << total << endl;
    return 0;
}

long digit_square_sum(long n) {
    long s = 0; int digits = 1 + floor(log10(n));
    for(int i = 0; i < digits; i++) {
        s += (n % 10) * (n % 10);
        n /= 10;
    }
    return s;
}

bool hits_89(long n) {
    while(n != 1 || n != 89) {
        n = digit_square_sum(n);
        if(n == 1 || n == 89)
            break;
    }
    return n == 89;
}
