#include <iostream>

using namespace std;

int* neighbors(int* cells) {
    //int* temp = cells;
    cout << cells[0] << endl;
    cells[0] = 9;
    cout << cells[0] << endl;
    return cells; 
}

int main() {
    int* cells = new int[4];
    for(int i = 0; i < 4; i++) {
        cells[i] = 0;
    }
    neighbors(cells);
    return 0;
} 
