/*
Description
输出所有的2位偶数，数字之间留一个空格。

Input
一行，所有2位数偶数。

Output
null
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int i;
	i = 10;
	while (i<100)
	{
		cout << i << " ";
		i = i + 2;
	}
}