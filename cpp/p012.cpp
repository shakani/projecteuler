#include <iostream>
#include <math.h>
using namespace std;

int triangle(int n);
int n_divisors(long int n);

int main() {
    int u = 500; // max divisors needed
    int i = 1;
    while(n_divisors(triangle(i)) < u) {
        i += 1;
    }
    cout << triangle(i) << endl;
    return 0;
}

int triangle(int n) {
    return n*(n+1)/2;
}

int n_divisors(long int n) {
    int divs = 0;
    for(int d = 1; d <= sqrt(n); d++) {
        if(n%d == 0)
            divs += 1;
    }
    divs *= 2;
    if(sqrt(n) == int(sqrt(n)))
        divs -= 1;
    return divs;
}
