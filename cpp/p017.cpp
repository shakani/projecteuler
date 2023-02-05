#include <iostream>
using namespace std;

/*

Digit sum of 100!. Via Stirling's approximation, 

ln(100!) is approximately 100ln(100) - 100

so log10(100!) is approx (100ln(100) - 100) / ln(10) = 156.5

There are 157 digits in 100!

Approach: Store digits in large register array, multiply to target, sum digits and output

*/

int multiply(int x, int res[], int res_size);
void print_register(int res[], int res_size);
int digit_sum_register(int res[], int res_size);

int main() {
    int reg[157]; 
    reg[0] = 1; int reg_size = 1;

    for(int k = 1; k < 100; k++) {
        reg_size = multiply(k, reg, reg_size);
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
