// https://www.beecrowd.com.br/judge/pt/problems/view/2143

#include <iostream>
using namespace std;
int main() 
{
	while(1)
	{
		int n, pessoas; cin >> n;
		if(n==0) break;
		while(n--)
		{
			cin >> pessoas;
			if (pessoas % 2 == 0)
            pessoas = (pessoas * 2) - 2;
        	else
            pessoas = (pessoas * 2) - 1;
			cout << pessoas << endl;
		}
	}
}
