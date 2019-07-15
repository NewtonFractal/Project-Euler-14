#include <iostream>
#include<ctime> 
using namespace std;
int chain = 0;
int record = 0;
int start_s=clock() ;
int main()
{
	for (int x = 3; x < 1000000; x += 2) {
		long long y = x;
		if (chain > record) {
			record = chain;
			cout << x - 2 << endl;
		}
		chain = 0;
		while (y > 1) {
			if (y % 2 == 0) {
				y /= 2;
				chain++;
			}
			else {
				y = (3 * y + 1)/2;
				chain += 2;
			}
		}
	}
	int stop_s=clock();
    cout<<(stop_s-start_s)/double(CLOCKS_PER_SEC);
}
