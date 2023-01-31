#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int n);

int main() {
    long int s = 0;
    for(int p = 2; p < 2000000; p++) {
        if(isPrime(p))
            s += p;
    }
    cout << "Total: " << s << '\n';
    return 0;
}

bool isPrime(int n) {
    for(int d = 2; d <= sqrt(n); d++) {
        if(n%d == 0)
            return false;
    }
    return true;
}
