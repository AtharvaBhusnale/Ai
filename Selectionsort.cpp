#include<bits/stdc++.h>
#include <iostream>
using namespace std ;
class Selection
{
	int arr[100] , size; // declare array and its size

	public :

	void init()
	{
		int val;
		cout<<"Enter the size of array :: ";
		cin>>size ; // Initialize the size of the array
		arr[size];
		for (int i=0 ; i<size ; i++)
		{
			printf("Enter the value at %d :",i);
			scanf("%d" , &val); // input value for each element 
			arr[i]=val;
		}
	}

	void disp()
	{
		for (int i=0 ; i<size ; i++)
		{
			
			cout<<arr[i]<<" "; // display the array
		}
	}

	void sel_sort()
	{
		int min , temp; // declare min element and temporary element

		for(int i=0 ; i<size-1 ; i++)
		{
			min=i; // initlaize i as the min element
			for (int j = i+1; j < size; j++)
			{
				if (arr[min]>=arr[j]) // if min element is greater the jth element  
					min=j ; // assign j as min element
			}
			if(min != i) // swapping the two variable
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
