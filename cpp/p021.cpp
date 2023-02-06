#include <iostream>
#include <math.h>
using namespace std;

long int d(long int n);

int main() {
    long int amicables = 0;
    for(long int i = 2; i < 10000; i++) {
        long int tmp = d(i);
        if(i == d(tmp) && i != tmp)
            amicables += i;
    }
    cout << amicables << endl;
    return 0;
}

long int d(long int n) {
    long int sum = 1;
    for(int i = 2; i <= sqrt(n); i++) {
        if(n%i == 0) {
            sum += i + n/i;
        }
    }
    if(sqrt(n) == int(sqrt(n)))
        sum -= sqrt(n);
    return sum;
}
