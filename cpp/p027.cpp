#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int p);
double poly(int a, int b, int n);
double poly_count(int a, int b);

int main() {
    int max_primes = 0; double prod = 0; int tmp;
    for(int a = -1000; a <= 1000; a++) {
        for(int b = -1000; b <= 1000; b++) {
            tmp = poly_count(a, b);
            if(tmp > max_primes) {
                max_primes = tmp;
                prod = a*b;
            }
        }
    }
    cout << prod << endl;
    return 0;
}

bool isPrime(int p) {
    if(p < 0)
        return isPrime(-1*p);
    for(int d = 2; d <= sqrt(p); d++) {
        if(p % d == 0)
            return false;
    }
    return true;
}

double poly(int a, int b, int n) {
    return n*n + a*n + b;
}

double poly_count(int a, int b) {
    double pc = 0; int n = 0;
    if(!isPrime(b))
        return pc;
    else {
        while(isPrime(poly(a, b, n))) {
            pc++;
            n++;
        }
        return pc;
    }
}
