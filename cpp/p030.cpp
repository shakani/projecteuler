#include <iostream>
#include <cmath>
using namespace std;

/*
    Is there an upper bound for numbers that can be written as sum of p-th powers of their digits?
    Yes. We are bounded by n, where n solves
    n*9^p = 10^n - 1
    LHS is max p-th power digit sum
    RHS is max n-digit number
    for p = 5, we have n approximately 5.51257. Only check below 10^n
*/

double ndsum(int n, int p, double s = 0);

int main() {
    double total = 0; double tmp;
    for(int i = 2; i < pow(10, 5.51257); i++) {
        tmp = ndsum(i, 5);
        if(i == tmp) {
            total += i;
        }
    }
    cout << total << endl;
    return 0;
}

double ndsum(int n, int p, double s) {
    if(n < 10)
        return s + pow(n, p);
    else {
        return ndsum(n/10, p, s + pow(n%10, p));
    }
}

