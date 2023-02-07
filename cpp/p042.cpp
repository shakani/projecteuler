#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

int triangle_roots(int t);
int word_score(string word);
bool isTriangle(string word);

int main() {
    // read file
    fstream myfile("p042-data.txt");
    string tmp;

    int triangle_words = 0;
    for(int i = 0; i < 1786; i++) {
        myfile >> tmp;
        triangle_words += int(isTriangle(tmp));
    }
    cout << triangle_words << endl;

    return 0;
}

int triangle_roots(int t) {
    float a, b;
    a = (-1.0 + sqrt(1.0 + 8.0*t))/2.0;
    b = (-1.0 - sqrt(1.0 + 8.0*t))/2.0;
    if(a > 0 && int(a) == a)
        return int(a);
    else if(b > 0 && int(b) == b) 
        return int(b);
    else
        return 0;
}

int word_score(string word) {
    int s = 0;
    for(int i = 0; i < word.length(); i++) {
        s += word[i] - 'A' + 1;
    }
    return s;
}

bool isTriangle(string word) {
    return triangle_roots(word_score(word));
}
