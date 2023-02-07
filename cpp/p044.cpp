#include <iostream>
#include <cmath>
using namespace std;

#define MAX 5000 

double p(int n);
bool isPentagonal(double Pn);

int main() {
    double D = p(MAX); // difference between pentagonals
    double diff; double Pj; double Pk;
    for(int j = 1; j < MAX; j++) {
        for(int k = j+1; k < MAX; k++) {
            Pj = p(j);
            Pk = p(k);
            diff = Pk - Pj;
            if(isPentagonal(Pj+Pk) && isPentagonal(Pk - Pj))
                D = (diff < D) ? diff : D;
        }
    } 
    cout << int(D) << endl;
    return 0;
}

double p(int n) {
    return n*(3*n - 1)/2;
}

bool isPentagonal(double Pn) {
    // P_n = n(3n-1)/2 --> 3n^2 - n - 2P_n = 0
    float n1 = (1.0 + sqrt(1.0 + 24.0*Pn))/6.0;
    return int(n1) == n1;
}
