// https://www.beecrowd.com.br/judge/pt/problems/view/1847

#include <iostream>
using namespace std;
int main() 
{
    int a, b, c; cin >> a >> b >> c;
    if (a > b && b <= c)
    cout << ":)" << endl;
    else if (a < b && b >= c)
    cout << ":(" << endl;
    else if (a < b && b < c && (b-c) > (a-b))
    cout << ":(" << endl;
    else if (a < b && b < c && (b-c) <= (a-b))
    cout << ":)" << endl;
    else if (a > b && b > c && (b-c) < (a-b))
    cout << ":)" << endl;
    else if (a > b && b > c && (b-c) >= (a-b))
    cout << ":(" << endl;
    else if (a == b && b < c)
    cout << ":)" << endl;
    else if (a == b && b > c)
    cout << ":(" << endl;
    else
    cout << ":(" << endl;
}