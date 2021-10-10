/*
Description
从小到大输出所有3位数中7的倍数的数。

Input
一行整数，之间用空格隔开。

Output
null
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int i = 105;
	while (i < 1001) {
		cout << i << " ";
		i = i + 7;
	}
}