#include <iostream>
using namespace std;

/*
Use prime factorization here;

2^x 3^y ... 19^z

such that 2^x < 20, 3^y < 20 for maximal powers x, y

*/

int main() {
    long int p = 1; int u = 20; // u is upper bound
    int primes[8] = {2, 3, 5, 7, 11, 13, 17, 19};
    int tmp;
    for(int i = 0; i < 8; i++) { // loop through primes
        tmp = primes[i];
        while(tmp < u) {
            tmp *= primes[i];
        }
        p *= tmp;
        p /= primes[i]; // correction
    }
    cout << p << '\n';
    return 0;
}
