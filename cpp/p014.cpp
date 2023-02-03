#include <iostream>
using namespace std;

long int collatz(long int n, long int chain = 1);
int tmp;

int main() {
    long long int max_n = 0; long int max_chain = 0; long int chain_now = 0;
    for(long long int j = 1; j < 1000000; j++) {
        chain_now = collatz(j);
        if(chain_now > max_chain) {
            max_n = j;
            max_chain = chain_now;
        }
    }

    cout << max_n << endl;

    return 0;
}

long int collatz(long int n, long int chain) {
    if(n == 1)
        return chain;
    else if(n%2 == 0) {
        tmp = 0;
        while(n%2 == 0) {
            n /= 2;
            tmp++;
        }
        return collatz(n, chain+tmp);
    }
    else {
        return collatz((3*n+1)/2, chain+2);
    }
}
