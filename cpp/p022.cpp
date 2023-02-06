#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

void print(const string& item) {
    cout << item << endl;
}

long int namescore(string str, int index) {
    long int s = 0;
    for(int i = 0; i < str.length(); i++) {
        s += str[i] - 'A' + 1;
    } 
    s *= (index + 1);
    return s;
}

int main() {
/*
    vector<string> v = { "xyzzy", "plugh", "abracadabra" };
    sort(v.begin(), v.end());
    for (auto x : v)
        print(x);
*/
    // read file into string vector
    fstream myfile("p022-data.txt");
    vector<string> names;
    string tmp; 
    for(int i = 0; i < 5163; i++) {
        myfile >> tmp; 
        names.insert(names.end(), tmp);
    }

    // sort string vector
    sort(names.begin(), names.end());

    // score names
    long int total = 0;
    for(int i = 0; i < names.size(); i++) {
        total += namescore(names[i], i);
    }
    cout << total << endl;

    return 0;
}
