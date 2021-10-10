/*
Description
输入一个整数，求出该整数以内的从小到这个整数为止的所有偶数并输出

Input
输入一个整数n

Output
输出只有一行，包含小到n的所有偶数，中间用空格隔开
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int i = 2;
	int a;
	cin >> a;
	while (i <= a) {
		cout << i << " ";
		i = i + 2;
	}
}