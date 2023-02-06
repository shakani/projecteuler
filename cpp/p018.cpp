#include <iostream>
#include <fstream>
using namespace std;

#define ROWS 15

void add_pairwise_max_array(int target[], int input[], int arr_length);
// arr_length is length of target

int main() {
    // read file
    fstream myfile("p018-data.txt");
    int tree[ROWS][ROWS];
    for(int i = 0; i < ROWS; i++) {
        for(int j = 0; j < ROWS; j++) {
            if(j > i)
                tree[i][j] = 0;
            else
                myfile >> tree[i][j];
        }
    }

    for(int k = 1; k < ROWS; k++)
        add_pairwise_max_array(tree[ROWS-(k+1)], tree[ROWS-k], ROWS);

    cout << tree[0][0] << endl;

    return 0;
}

void add_pairwise_max_array(int target[], int input[], int arr_length) {
    for(int i = 0; i < arr_length - 1; i++) {
        if(input[i] > input[i+1]) {
            target[i] += input[i];
        }
        else {
            target[i] += input[i+1];
        }
    }
}
