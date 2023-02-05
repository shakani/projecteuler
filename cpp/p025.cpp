#include <iostream>
#include <math.h>
using namespace std;

/*

Binet formula for Fibonacci numbers:

(phi^n - psi^n)/sqrt(5) = F_n

phi = (1+sqrt(5))/2 > 1
psi = (1-sqrt(5))/2 < 1

For large n, approximate

F_n = phi^n / sqrt(5)

log10(F_n) = n log10(phi) - 0.5 log10(5)

Find n such that n_digits of F_n is 1000

*/

const double phi = (1 + sqrt(5)) / 2;

long int n_digits(double x);
long int fib_digits(long int n);

int main() {
    long int index = 1;
    while(fib_digits(index) < 1000)
        index++;
    cout << index << endl; 
    return 0;
}

long int n_digits(double x) {
    return ceil(log10(x));
}

long int fib_digits(long int n) {
    return ceil(n*log10(phi) - 0.5 * log10(5));
}
