#include <iostream>
#include <cmath>
using namespace std;


double facts[101];
double binom(int n, int r);

int main() {

    facts[0] = 1;
    for(int i = 1; i < 101; i++)
        facts[i] = i * facts[i-1]; // dynamically create all factorials needed

    double answer = 0;
    for(int n = 1; n <= 100; n++) {
        for(int r = 1; r <= n; r++) {
            if(binom(n, r) > pow(10, 6))
                answer++;
        }
    }
    cout << answer << endl;
}

double binom(int n, int r) {
    return facts[n] / (facts[n - r] * facts[r]);
}
