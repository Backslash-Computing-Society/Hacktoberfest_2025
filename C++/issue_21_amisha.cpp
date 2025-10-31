#include <iostream>
using namespace std;

void printStarTriangle(int rows) {
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) {
            cout << "* ";
        }
        cout << endl;
    }
}

void printNumberTriangle(int rows) {
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void printCharTriangle(int rows) {
    for (int i = 1; i <= rows; ++i) {
        for (int j = 0; j < i; ++j) {
            cout << (char)('A' + j) << " ";
        }
        cout << endl;
    }
}

void printPyramid(int rows) {
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= rows - i; ++j) {
            cout << " ";
        }
        for (int k = 1; k <= (2 * i - 1); ++k) {
            cout << "*";
        }
        cout << endl;
    }
}

void printDiamond(int rows) {
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= rows - i; ++j) {
            cout << " ";
        }
        for (int k = 1; k <= (2 * i - 1); ++k) {
            cout << "*";
        }
        cout << endl;
    }
    for (int i = rows - 1; i >= 1; --i) {
        for (int j = 1; j <= rows - i; ++j) {
            cout << " ";
        }
        for (int k = 1; k <= (2 * i - 1); ++k) {
            cout << "*";
        }
        cout << endl;
    }
}

void printHollowSquare(int size) {
    for (int i = 1; i <= size; ++i) {
        for (int j = 1; j <= size; ++j) {
            if (i == 1 || i == size || j == 1 || j == size) {
                cout << "* ";
            } else {
                cout << "  "; 
            }
        }
        cout << endl;
    }
}

int main() {
    int choice;
    int rows;

    cout << "Choose a pattern to print:" << endl;
    cout << "1. Star Triangle" << endl;
    cout << "2. Number Triangle" << endl;
    cout << "3. Character Triangle" << endl;
    cout << "4. Pyramid" << endl;
    cout << "5. Diamond" << endl;
    cout << "6. Hollow Square" << endl;
    cout << "Enter your choice (1-6): ";
    cin >> choice;

    cout << "Enter the number of rows/size: ";
    cin >> rows;

    switch (choice) {
        case 1:
            printStarTriangle(rows);
            break;
        case 2:
            printNumberTriangle(rows);
            break;
        case 3:
            printCharTriangle(rows);
            break;
        case 4:
            printPyramid(rows);
            break;
        case 5:
            printDiamond(rows);
            break;
        case 6:
            printHollowSquare(rows);
            break;
        default:
            std::cout << "Invalid choice." << std::endl;
            break;
    }

    return 0;
}
