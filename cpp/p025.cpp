#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

const double phi = (1.0 + sqrt(5))/2.0;
const double psi = (1.0 - sqrt(5))/2.0;

double fib(int n);
int n_digits(float n);

int main() {
    // 4787 is estimated from binet formula
    cout << fib(4787) << '\n';
    return 0;
}

double fib(int n) {
    return (pow(phi, n) - pow(psi, n))/sqrt(5);
}

int n_digits(float n) {
    return ceil(log10(n));
}
