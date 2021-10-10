/*
描述
输入规定个数个整数并显示出它们的合计值和平均值

输入
输入为n+1行，第一行为整数n
第2~n+1行为n个整数

输出
输出为两行，第一行为n个整数的总和
第二行为n个整数平均值，其中平均值保留两位小数
*/
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	float n, i, input, sum;
	float average;
	sum = 0;
	cin >> n;
	i = n;
	while (n > 0) {
		cin >> input;
		sum = sum + input;
		n = n - 1;
	}
	average = sum / i;
	cout << "sum=" << sum << endl;
	cout.setf(ios::fixed);
	cout << setprecision(2);
	cout << "average=" << average << endl;
}