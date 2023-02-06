#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

    // import file
    ifstream myfile("p011-data.txt");
    int tmp;

    // read file to 2D array
    int grid[20][20];
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20; j++) {
            myfile >> tmp;
            grid[i][j] = tmp;
        }
    }

    // find largest product 
    long int p = 0;
    long int p_max = 0;


    // horizontally
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20-4; j++) {
            p = 1;
            for(int k = 0; k < 4; k++)
                p *= grid[i][j+k];
            if(p > p_max)
                p_max = p;
        }
    }

    // vertically
    for(int i = 0; i < 20 - 4; i++) {
        for(int j = 0; j < 20; j++) {
            p = 1;
            for(int k = 0; k < 4; k++)
                p *= grid[i+k][j];
            if(p > p_max)
                p_max = p;
        }
    }

    // right-down diagonal
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20; j++) {
            p = 1;
            for(int k = 0; k < 4; k++) {
                if(i+k >= 20 || j+k >= 20)
                    p *= 0;
                else
                    p *= grid[i+k][j+k];
            }
            if(p > p_max)
                p_max = p;
        }
    }

    // left-down diagonal
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20; j++) {
            p = 1;
            for(int k = 0; k < 4; k++) {
                if(i+k >= 20 || j-k < 0)
                    p *= 0;
                else
                    p *= grid[i+k][j-k]; 
            }
            if(p > p_max)
                p_max = p;
        }
    }

    cout << p_max << endl;

    return 0;
}
