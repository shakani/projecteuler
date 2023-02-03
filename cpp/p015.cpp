#include <iostream>
using namespace std;

#define MAX 500 // max number of digits for buffer

/*
Answer comes out to 40 choose 20
Using factorial properties, I compute

= 4 * (39!! / 27!!) * 23

*/

void factorial(int n);
int multiply(int x, int res[], int res_size);

int main() {
    // need to return 40 choose 20

    int res[MAX]; 
    res[0] = 1;
    int res_size = 1;

    int factors[8] = {39, 37, 35, 33, 31, 29, 23, 4};

    for(int i = 0; i < 8; i++) {
        res_size = multiply(factors[i], res, res_size);
    }

    for(int i = res_size - 1; i >= 0; i--) {
        cout << res[i];
    }
    cout << endl;

    return 0;
}

int multiply(int x, int res[], int res_size) {
    int carry = 0; // initialize carry

    for(int i = 0; i < res_size; i++) {
        int prod = res[i] * x + carry;
        res[i] = prod % 10;
        carry = prod / 10;
    }
    while(carry) {
        res[res_size] = carry % 10;
        carry /= 10;
        res_size++;
    }
    return res_size;
}
