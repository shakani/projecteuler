#include <iostream>
using namespace std;

/*

Digit sum of 2^1000. First note log10(2^1000) is approximately 301.02 
There are 302 digits in this number. 

Approach: Store digits in large register array, multiply to target, sum digits and output

*/

int multiply(int x, int res[], int res_size);
void print_register(int res[], int res_size);
int digit_sum_register(int res[], int res_size);

int main() {
    int reg[302]; 
    reg[0] = 1; int reg_size = 1;

    for(int k = 0; k < 1000; k++) {
        reg_size = multiply(2, reg, reg_size);
    }

    //print_register(reg, reg_size);
    cout << digit_sum_register(reg, reg_size) << endl;

    return 0;
}

int multiply(int x, int res[], int res_size) {

    int carry = 0;

    for(int j = 0; j < res_size; j++) {
        int p = res[j] * x + carry;
        res[j] = p % 10;
        carry = p / 10;
    }

    while(carry) {
        res[res_size] = carry % 10;
        carry /= 10;
        res_size++;
    }

    return res_size;
}

void print_register(int res[], int res_size) {
    for(int j = res_size - 1; j >= 0; j--) {
        cout << res[j];
    }
    cout << endl;
}

int digit_sum_register(int res[], int res_size) {
    int s = 0;
    for(int i = 0; i < res_size; i++)
        s += res[i];
    return s;
}
