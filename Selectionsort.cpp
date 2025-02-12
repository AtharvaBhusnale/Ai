#include<bits/stdc++.h>
#include <iostream>
using namespace std ;
class Selection
{
	int arr[100] , size;

	public :

	void init()
	{
		int val;
		cout<<"Enter the size of array :: ";
		cin>>size ;
		arr[size];
		for (int i=0 ; i<size ; i++)
		{
			printf("Enter the value at %d :",i);
			scanf("%d" , &val);
			arr[i]=val;
		}
	}

	void disp()
	{
		for (int i=0 ; i<size ; i++)
		{
			
			cout<<arr[i]<<" ";
		}
	}

	void sel_sort()
	{
		int min , temp;

		for(int i=0 ; i<size-1 ; i++)
		{
			min=i;
			for (int j = i+1; j < size; j++)
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
