#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm> // next_permutation
#include <cmath>
using namespace std;

/*
    Shortest passcode is permutation of 01236789
*/

bool validate_pwd(int guess, vector<int> pwd);
bool validate_attempts(int att[], vector<int> pwd);
void print_pwd(vector<int> pwd);

int main() {
    // initialize array with attempts in file
    fstream myfile("p079-data.txt");
    int attempts[50]; int a;
    for(int i = 0; i < 50; i++) {
        myfile >> a;
        attempts[i] = a;
    }

    // initialize password to sorted digits present in valid password
    vector<int> password; //= {0, 1, 2, 3, 6, 7, 8, 9}; // starting permutation
    
    for(int i = 0; i < 10; i++) { // populate vector with initial password guess
        if(i != 4 && i != 5)
            password.insert(password.end(), i);
    }

    for(double i = 0; i < pow(10, 7); i++) {
        if(validate_attempts(attempts, password)) {
            break;
        }
        else
            next_permutation(password.begin(), password.end());
    }

    print_pwd(password);
    return 0;
}

bool validate_pwd(int guess, vector<int> pwd) {
    int digits[3] = {guess/100, (guess/10) % 10, guess % 10};
    int check = 0;
    for(int i = 0; i < pwd.size(); i++) {
        if(pwd[i] == digits[check]) {
            check++;
        }
        if(check == 3)
            return true;
    }
    return check == 3;
}

bool validate_attempts(int att[], vector<int> pwd) {
    for(int i = 0; i < 50; i++)
        if(!validate_pwd(att[i], pwd))
            return false;
    return true;
}

void print_pwd(vector<int> pwd) {
    for(int i = 0; i < pwd.size(); i++)
        cout << pwd[i];
    cout << endl;
}

