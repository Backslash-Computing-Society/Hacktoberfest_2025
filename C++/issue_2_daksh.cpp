#include <iostream>
#include <cmath>
#include <limits>
using namespace std;

int main() {
    while (true) {
        cout << "\n=== simple calculator ===\n";
        cout << "1) add\n";
        cout << "2) subtract\n";
        cout << "3) multiply\n";
        cout << "4) divide\n";
        cout << "5) power\n";
        cout << "6) modulus\n";
        cout << "7) exit\n";

        int ch;
        cout << "choice: ";
        if (!(cin >> ch)) break;

        if (ch == 7) {
            cout << "bye\n";
            break;
        }

        if (ch >= 1 && ch <= 5) {
            double a, b;
            cout << "enter a: ";
            cin >> a;
            cout << "enter b: ";
            cin >> b;

            if (ch == 1) cout << "result: " << a + b << "\n";
            else if (ch == 2) cout << "result: " << a - b << "\n";
            else if (ch == 3) cout << "result: " << a * b << "\n";
            else if (ch == 4) {
                if (b == 0) cout << "error: division by zero\n";
                else cout << "result: " << a / b << "\n";
            }
            else if (ch == 5) cout << "result: " << pow(a, b) << "\n";
        }
        else if (ch == 6) {
            int a, b;
            cout << "enter integer a: ";
            cin >> a;
            cout << "enter integer b: ";
            cin >> b;
            if (b == 0) cout << "error: division by zero\n";
            else cout << "result: " << a % b << "\n";
        }
        else cout << "invalid choice\n";

        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    return 0;
}
