#include <iostream>
#include <cmath>
using namespace std;

/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

c = sqrt(a^2 + b^2)
loop through a, b with a <= b up to a = p

*/

double solutions(int p);

int main() {
    int pmax = 0; double psols = 0; double tmp;

    for(int p = 2; p <= 1000; p+=2) { // only need to check even p
        tmp = solutions(p);
        if(tmp > psols) {
            psols = tmp;
            pmax = p;
        }
    }

    cout << pmax << endl;
    return 0;
}

double solutions(int p) {
    double nsols = 0; float cp; 
    for(int a = 1; a < p; a++) {
        for(int b = a; b < p-a; b++) {
            cp = sqrt(pow(a, 2) + pow(b, 2));
            if(cp == p - (a+b)) {
                    nsols++;
            }
            else
                continue;
        }
    }
    return nsols;
}
