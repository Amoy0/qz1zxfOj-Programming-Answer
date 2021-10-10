/*
Description
如果你知道一个整数a，想输出a前面的N个数，怎么办？

Input
一行2个正整数：a和N，范围在[1,10000]。

Output
一行n个整数：……a-2  a-1
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int i, a, b;
	cin >> i;
	cin >> a;
	b = i - a;
		while (b != i)
		{
			cout << b << " ";
			b = b + 1;
		}
}