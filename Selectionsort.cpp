#include<bits/stdc++.h>
#include <iostream>
using namespace std ;
class Selection
{
	int arr[5] , size;

	public :

	void init()
	{
		int val;
		for (int i=0 ; i<5 ; i++)
		{
			printf("Enter the value at %d :",i);
			scanf("%d" , &val);
			arr[i]=val;
		}
	}

	void disp()
	{
		for (int i=0 ; i<5 ; i++)
		{
			
			cout<<arr[i]<<" ";
		}
	}

	void sel_sort()
	{
		int min , temp;

		for(int i=0 ; i<4 ; i++)
		{
			min=i;
			for (int j = i+1; j < 5; j++)
			{
				if (arr[min]>=arr[j])
					min=j ;
			}
			if(min != i)
			{
				temp=arr[min];
				arr[min]=arr[i];
				arr[i]=temp;
			}
		}
	}

};

int main()
{
	Selection s;
	s.init();
	s.sel_sort();
	s.disp();
}