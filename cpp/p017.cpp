#include <iostream>
#include <string>
using namespace std;

const string ones[20] = {
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };

const string tens[10] = {
        "zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    };
/*
const string hundred[1] = {"hundred"};
const string thousand[1] = {"thousand"};
string and_str = "and";
*/

string writer(int n); 
int num_letter_count(int n);

int main() {
    long int total = 0;
    for(int i = 1; i <= 1000; i++)
        total += num_letter_count(i);
    cout << total << endl;
    return 0;
}

string writer(int n) {
    if(n < 20)
        return ones[n];
    else if(n < 100) {
        return tens[n/10] + writer(n%10);
    }
    else if(n < 1000) {
        if(n%100 == 0)
            return ones[n/100] + "hundred";
        else
            return writer(n - (n%100)) + "and" + writer(n%100);
    }
    else 
        return "onethousand";
}

int num_letter_count(int n) {
    return writer(n).length();
}
