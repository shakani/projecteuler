#include <iostream>
using namespace std;

/*

sum square difference
sum of squares is 1^2 + 2^2 + ... + n^2
square of sum is (1 + 2 + ... + n)^2
find difference between sum of squares and square of sum

*/

int sum_squares(int n);
int square_sum(int n);

int main() {
    cout << square_sum(100) - sum_squares(100) << '\n';
    return 0;
}

// sum of squares 1^2 + 2^2 + ... + n^2
int sum_squares(int n) {
    return n*(n+1)*(2*n+1)/6;
}

int square_sum(int n) {
    return n*n*(n+1)*(n+1)/4;
}
