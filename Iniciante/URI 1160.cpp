// https://www.beecrowd.com.br/judge/pt/problems/view/1160 //

#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i=0; i < n;i++)
    {
    int pa, pb, anos=0; float g1,g2;
    cin >> pa >> pb >> g1 >> g2;
    while(pa <= pb)
    {
        int cresc1 = (pa*(g1/100));
        int cresc2 = (pb*(g2/100));
        anos += 1;
        pa += cresc1;
        pb += cresc2;
        
        if(anos > 100)
            break;
    }
    if(anos>100)
        cout << "Mais de 1 seculo." << endl;
    else
        cout << anos << " anos." << endl;
    }
}