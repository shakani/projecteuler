#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int n);

int main() {
    int u = 10001; int primes = 0; int tmp = 2;
    while(primes < u) {
        if(isPrime(tmp)) {
            primes += 1;
        }
        tmp += 1;
    }
    cout << tmp-1 << '\n';
    return 0;
}

bool isPrime(int n) {
    for(int d = 2; d <= int(sqrt(n)); d++) {
        if(n%d == 0)
            return false;
    }
    return true;
}
