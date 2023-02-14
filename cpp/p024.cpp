#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {

    int v[10];
    for(int i = 0; i < 10; i++)
        v[i] = i;

    for(int k = 0; k < pow(10, 6) - 1; k++)
        next_permutation(v, v+10);

    for(int j = 0; j < 10; j++)
        cout << v[j];
    cout << endl;

    return 0;
}
