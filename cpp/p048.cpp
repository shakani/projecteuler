#include <iostream>
#include <math.h>
using namespace std;

const long int MAX = pow(10, 10);
long int selfpower(int x);

int main() {
    long int total = 0;
    for(int i = 1; i <= 1000; i++) {
        total += selfpower(i);
        total = total % MAX;
    }   
    cout << total << endl;
    return 0;
}

long int selfpower(int x) {
    long int p = 1;
    for(int i = 0; i < x; i++) {
        p *= x;
        p = p % MAX;
    }
    return p;
}
