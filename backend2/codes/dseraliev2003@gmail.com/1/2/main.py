#include<iostream>
#include<fstream>
using namespace std;
int a[100][100];main()
{
freopen("INPUT.txt","r",stdin);
ofstream out("output.txt");
int l,h,n,i,j,k,x1,y1,x2,y2,s=0;
cin>>l>>h>>n;
for(i=0;i<n;++i)
{
	cin>>x1>>y1>>x2>>y2;
	for(j=x1;j<x2;++j)
	{
		for(k=y1;k<y2;++k)
		{
			if(a[j][k]==0)
			{
				s++;a[j][k]=1;
			}
		}
	}
}
cout<<l*h-s;
out<<l*h-s;
}
