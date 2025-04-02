#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Graph 
{
    int adjMtx[100][100]; //Graph Initialized
    bool visited[100];   //Value initialized to check if the node is visited or not 
    int size;  //No. of nodes in graph           

    public :

    void create_adjMtx() 
    {
        cout << "Enter the number of vertices in the graph: ";
        cin >> size;

        for (int i = 0; i < size; i++) 
        {
            for (int j = 0; j < size; j++) 
            {
                adjMtx[i][j] = 0; //initialization of matirx values with zeros
                if(adjMtx[i][j]==1)
                    cout<<"Entered element other than 1";
                    break;
            }
            visited[i] = false; //Initialize all the node to be not visited
        }

        cout << "\nEnter adjacency matrix values (0 for no edge, 1 for edge):\n";
        for (int i = 0; i < size; i++) 
        {
            for (int j = i; j < size; j++) 
            { 
                if (i != j) 
                {
                    // cout << "Is there an edge between " << (i) << " and " << (j) << "? (1/0): ";
                    printf("Is there an edge between %c and %c (1/0) :", i+65 , j+65 ); //Using printf to print alphabetical values of node
                    cin >> adjMtx[i][j]; //Input of matrix
                    adjMtx[j][i] = adjMtx[i][j]; //As undirected graph hence input of a-b is equal to b-a
                }
            }
        }
    }

    
    void display_adjMtx() 
    {
        cout << "\nAdjacency Matrix:\n   ";
        for (int i = 0; i < size; i++) 
        {
            // cout << (i) << " ";
            printf("%c ",i+65); //to diplay top layer of matrix with node name
        }
        cout << endl;

        for (int i = 0; i < size; i++) 
        {
            // cout << (i) << "  ";
            printf("%c  ",i+65);//to diplay side layer of matrix with node name
            for (int j = 0; j < size; j++) 
            {
                 cout << adjMtx[i][j] << " "; //display the visited matrix
                
            }
            cout << endl;
        }
    }

    
    void reset_visited() 
    {
        for (int i = 0; i < size; i++) 
        {
            visited[i] = false; // to initalized all the nodes to be not visited
        }
    }

    
    void DFS(int start)  // Depth first search starts
    {
        int stack[100], top = -1; //initalize stack array and top as -1
        stack[++top] = start;  // start is initialized to top of stack 
        visited[start] = true; // start is marked as visited

        cout << "\nDFS Traversal: ";

        while (top >= 0) // stack to operate until is becomes empty
        {
            int node = stack[top--]; //pop the top element and store it in node
            // cout << (node) << " ";
            printf("%c ",node+65); // print node as it is visited
            
            for (int i =size - 1; i >=0; i--) 
             {
                if (adjMtx[node][i] == 1 && !visited[i])  // check if edge betwn the two nodes i.e node and i ans also check if i is visited
                {
                    //if not visited and have an edge
                    stack[++top] = i;  // push the i node into stack 
                    visited[i] = true; // mark it as visited
                }
            }
        }
        cout << endl;
    }

    
    void BFS(int start)
    {
        int queue[100], front = 0, rear = 0; //initialize the queue array and 2 varibles front and rear with 0 to mark the start and end of the queue
        queue[rear++] = start; //initialize the start node to queue
        visited[start] = true; // mark that node as visited

        cout << "\nBFS Traversal: ";

        while (front < rear) 
        {
            int node = queue[front++];  // dequeue the front element and store it in node
            printf("%c ",node+65);  // print the node element 

           
            for (int i = 0; i < size; i++) 
            {
                if (adjMtx[node][i] == 1 && !visited[i])  // check if edge betwn the two nodes i.e node and i ans also check if i is visited
                {
                    queue[rear++] = i; // push into queue using rear end
                    visited[i] = true; // mark the node as visited
                }
            }
        }
        cout << endl;
    }
};


int main() {
    Graph g;

    g.create_adjMtx();
    g.display_adjMtx();

    g.reset_visited();
    g.DFS(0); 

    g.reset_visited();
    g.BFS(0); 

    return 0;
}
