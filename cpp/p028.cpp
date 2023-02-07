#include <iostream>
#include <math.h>
using namespace std;

/*
    sum of odd squares is a cubic polynomial
    other diagonals are linear shifts from this polynomial
    use lagrange interpolation to find best fitting poly

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

f(1) = 1
f(3) = 25
f(5) = 101
f(7) = 261 

*/

long int poly(int x);

int main() {
    cout << poly(1001) << endl;
    return 0;
}

// interpolation done via WolframAlpha, or could work by hand to get it
long int poly(int x) {
    return (4*pow(x, 3) + 3*pow(x, 2) + 8*x - 9)/6;
}
