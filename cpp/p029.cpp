#include <iostream>
#include <set>
#include <math.h>
using namespace std;

#define MAX 100 

int main() {
    // put all a^b into a set 
    set<double> s;
    for(int a = 2; a <= MAX; a++) {
        for(int b = 2; b <= MAX; b++) {
            s.insert(pow(a, b));
        }
    }

    cout << s.size() << endl;

    return 0;
}
