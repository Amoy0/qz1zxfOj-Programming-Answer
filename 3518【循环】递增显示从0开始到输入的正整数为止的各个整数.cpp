/*
Description
输入一个整数，显示从0开始到递增到输入的整数的各个整数

Input
输入一个整数n

Output
输出包含从0开始递增到n的n+1个整数
*/
#include <iostream>
#include <string>
using namespace std;
int main()
{
  	int n,i;
  	i=0;
	cin >> n;
  	while(i<=n){
      	cout << i<<endl;
  		i=i+1;
      }
}