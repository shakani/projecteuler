#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define MAX 500 // max buffer size

int add_to_register(int arg[], int res[], int res_size);
void print_register(int res[], int res_size);

int main() {
    // initialize register
    static int reg[MAX];
    for(int k = 0; k < MAX; k++) {
        reg[k] = 0;
    }
    long int reg_size = 1;

    // read lines of each file
    ifstream myfile;
    myfile.open("p013-data.txt");
    string mystring;
    int addend[52]; // sum of numbers bounded by 52 digits, so just pad 0s

    for(int k = 0; k < 100; k++) { // loop through file
        myfile >> mystring;

        // cast string to int array
        for(int j = 0; j < 52; j++) {
            addend[49-j] = mystring[j] - '0';
        }
        //print_register(addend, 52); cout << endl;
        reg_size = add_to_register(addend, reg, reg_size);
    }
    
    // read out first 50 digits

    for(int j = 0; j < 10; j++) {
        cout << reg[51-j];
    }
    cout << endl;

    //print_register(reg, 52);
    return 0;
}

void print_register(int res[], int res_size) { // for debugging
    for(int j = res_size - 1; j >= 0; j--)
        cout << res[j];
    cout << endl;
}

int add_to_register(int arg[], int res[], int res_size) {
    int carry = 0;

    for(int i = 0; i < 52; i++) { // add the argument to first 50 digits
        int adder = res[i] + arg[i] + carry;
        res[i] = adder % 10;
        carry = adder / 10;
    }

    int place = 50;

    while(carry) {
        int adder = res[place] + carry;
        res[place] = adder % 10;
        carry = adder / 10;
        place++;
    }

    return place;
}
