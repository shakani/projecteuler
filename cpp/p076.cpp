#include <iostream>
#include <vector>
using namespace std;

#define u 100 // integer partition to compute

int main() {
    long data[u+1][u+1];
    for(int i = 0; i < u+1; i++) {
        for(int j = 0; j < u+1; j++) {
            data[i][j] = 0;
        }
    }

    for(int k = 0; k < u+1; k++) {
        for(int n = k; n < u+1; n++) {
            if(k > 0 && n > 0)
                data[n][k] = data[n-k][k] + data[n-1][k-1];
            else
                data[0][0] = 1;
        }
    }

    long total = 0;
    for(int k = 0; k < u+1; k++)
        total += data[u][k];

    cout << total - 1 << endl;

    return 0;
}
