#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int ctoi(char c); 

int main() {
    ifstream myfile("p008-data.txt");
    string mystring;
    myfile >> mystring;

    long int maxp = 0; int w = 13; long int tmp = 1;
    for(int i = 0; i < 1000-w; i++) {
        // compute product in window
        tmp = 1;
        for(int j = 0; j < w; j++) {
            tmp *= ctoi(mystring[i+j]);
        }
        if(tmp > maxp)
            maxp = tmp;
    }
    cout << maxp << '\n';

    return 0;
}

int ctoi(char c) {
    return int(c)-int('0');
}
