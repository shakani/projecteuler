#include <iostream>
#include <cmath>
using namespace std;

int n_digits(long n);
bool is_perm(long n, long m);

int main() {
    for(int x = 1; x < 6; x++) {
        for(int j = int(pow(10, x)); j <= (pow(10,x+1) - 1)/6; j++) {
            if(is_perm(j, 6*j)) {
                bool found = true;
                for(int c = 2; c <= 6; c++) {
                    found = found && is_perm(j, c*j);
                }
                if(found) {
                    cout << j << endl;
                    return 1;
                }
            }
        }
    }
    return 0;
}

int n_digits(long n) {
    return 1 + floor(log10(n));
}

bool is_perm(long n, long m) {
    int d_n = n_digits(n);
    int d_m = n_digits(m);
    if(d_n != d_m)
        return false;
    else {
        int arr[10];
        for(int i = 0; i < 10; i++)
            arr[i] = 0;

        for(int j = 0; j < d_n; j++) {
            arr[ n % 10 ]++;
            arr[ m % 10 ]--;
            n /= 10;
            m /= 10;
        }
        for(int k = 0; k < 10; k++) {
            if(arr[k] != 0)
                return false;
        }
        return true;
    }
}
