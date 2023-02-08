#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>
using namespace std;

#define MAX 1455

void xor_encode(int arr[], int arr_length, int pwd[]);
void print_arr(int arr[], int arr_length);
int mostFrequent(int arr[], int arr_length);

int main() {

    // read file to array
    fstream myfile("p059-data.txt");
    int data[MAX];
    int tmp;

    for(int i = 0; i < MAX; i++) {
        myfile >> tmp;
        data[i] = tmp;
    }

    int pwd[3] = {int('e'), int('x'), int('p')};
    xor_encode(data, MAX, pwd);
    double total = 0;
    for(int i = 0; i < MAX; i++) {
        total += data[i];
    }
    cout << total << endl;

    return 0;
}

void xor_encode(int arr[], int arr_length, int pwd[]) {
    int tmp;
    for(int i = 0; i < arr_length; i++) {
        tmp = arr[i];
        arr[i] = tmp ^ pwd[i % 3];
    }
}

void print_arr(int arr[], int arr_length) {
    for(int i = 0; i < arr_length; i++)
        cout << char(arr[i]);
    cout << endl;
}

int mostFrequent(int arr[], int arr_length) {
    map<int, int> hash;
    for(int i = 2; i < arr_length; i+=3) {
        hash[arr[i]]++;
    }
    int max_count = 0; 
    int res = -1;
    for(auto i : hash) {
        if(max_count < i.second) {
            res = i.first;
            max_count = i.second;
        }
    }
    return res;
}

