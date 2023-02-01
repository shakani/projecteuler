#include <iostream>
using namespace std;

int pFinder(int u);

int main() {
    cout << pFinder(1000) << endl;
    return 0;
}

int pFinder(int u) {
    int c = 0;
    for(int a = 1; a < u; a++) {
        for(int b = a+1; b < u; b++) {
            c = 1000 - (a + b);
            if(a*a + b*b == c*c)
                return a*b*c;
        }
    }
    return 0;
}
