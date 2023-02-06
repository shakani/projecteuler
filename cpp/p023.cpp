#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

long int d(long int n); // sum of proper divisors

int main() {

    // find all abundant numbers below limit
    long int u = 28123; // upper bound for this problem
    long int total = u * (u + 1) / 2; // all numbers less than or equal to u sum up to this
    vector<long int> abundants; // abundant numbers
    for(int i = 1; i < u; i++) {
        if(d(i) > i)
            abundants.insert(abundants.end(), i);
    }

    long int s = 0;
    vector<long int> abundant_sums; 
    for(int i = 0; i < abundants.size(); i++) { // populate abundant sums
        for(int j = i; j < abundants.size(); j++) {
            s = abundants[i] + abundants[j];
            if(s > u)
                break;
            else {
                abundant_sums.insert(abundant_sums.end(), s);
            }
        }
    }

    //cout << abundant_sums.size() << endl;

    // delete duplicates of abundant sums
    sort(abundant_sums.begin(), abundant_sums.end());
    abundant_sums.erase(unique(abundant_sums.begin(), abundant_sums.end()), abundant_sums.end());

    for(auto& n : abundant_sums)
        total -= n;

    cout << total << endl;

    return 0;
}

long int d(long int n) {
    long int s = 1;
    for(long int i = 2; i <= sqrt(n); i++) {
        if(n%i == 0) {
            s += i + n/i;
        }
    }
    if(sqrt(n) == int(sqrt(n)))
        s -= sqrt(n);
    return s;
}
