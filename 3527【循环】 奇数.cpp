/*
描述
给定N，输出1到N之间的奇数。

输入
一行1个正整数：N，范围在[1,10000]。

输出
[1…N]内的正奇数。
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int i, a;
	cin >> i;
	a = 1;
		while (a < i+1)
		{
			cout << a << " ";
			a = a + 2;
		}
}