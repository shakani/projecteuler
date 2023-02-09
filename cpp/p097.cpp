#include <iostream>
#include <cmath>
using namespace std;

/*
    p = 28433 * 2^7830457 + 1
*/

int main() {
    double answer = 28433;
    for(int i = 0; i < 7830457; i++) {
        answer = fmod(answer * 2, pow(10, 10));
    }
    answer += 1;
    cout << long(answer) << endl; 
    return 0;
}
