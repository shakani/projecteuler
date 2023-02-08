#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int p);
int cycle(int n, int times);
bool isCyclePrime(int p);

int main() {
    double cycle_primes = 1;
    for(double i = 3; i < pow(10, 6); i+=2) {
        if(isCyclePrime(i))
            cycle_primes++;
    }
    cout << cycle_primes << endl;
    return 0;
}

bool isPrime(int p) {
    for(int d = 2; d <= sqrt(p); d++) {
        if(p % d == 0)
            return false;
    }
    return true;
}

int cycle(int n, int times) {
    if(times == 0)
        return n;
    else if(times == 1)
        return n/10 +  (n%10)*pow(10, int(log10(n)));
    else
        return cycle(n/10 +  (n%10)*pow(10, int(log10(n))), times-1);
}

bool isCyclePrime(int p) {
    bool icp = true;
    for(int i = 0; i < log10(p); i++) {
        icp = icp && isPrime(cycle(p, i));
    }
    return icp;
}
