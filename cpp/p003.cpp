#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long n = 600851475143; // find its largest prime factor
    int dmax = 2;
    for(int d = 2; d < n; d++) {
        if(n%d == 0) {
            dmax = d;
        }
        while(n%d == 0) {
            n /= d; // keep dividing out this factor
        }
    }
    cout << "Largest prime factor of 600851475143: " << n << "\n";
    return 0;
}
