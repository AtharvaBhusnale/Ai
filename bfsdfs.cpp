#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Graph 
{
    int adjMtx[100][100]; 
    bool visited[100];    
    int size;             

    public :

    void create_adjMtx() 
    {
        cout << "Enter the number of vertices in the graph: ";
        cin >> size;

        for (int i = 0; i < size; i++) 
        {
            for (int j = 0; j < size; j++) 
            {
                adjMtx[i][j] = 0;
            }
            visited[i] = false;
        }

        cout << "\nEnter adjacency matrix values (0 for no edge, 1 for edge):\n";
        for (int i = 0; i < size; i++) 
        {
            for (int j = i; j < size; j++) 
            { 
                if (i != j) 
                {
                    // cout << "Is there an edge between " << (i) << " and " << (j) << "? (1/0): ";
                    printf("Is there an edge between %c and %c (1/0) :", i+65 , j+65 );
                    cin >> adjMtx[i][j];
                    adjMtx[j][i] = adjMtx[i][j]; 
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
            printf("%c ",i+65);
        }
        cout << endl;

        for (int i = 0; i < size; i++) 
        {
            // cout << (i) << "  ";
            printf("%c  ",i+65);
            for (int j = 0; j < size; j++) 
            {
                 cout << adjMtx[i][j] << " ";
                
            }
            cout << endl;
        }
    }

    
    void reset_visited() 
    {
        for (int i = 0; i < size; i++) 
        {
            visited[i] = false;
        }
    }

    
    void DFS(int start) 
    {
        int stack[100], top = -1;
        stack[++top] = start;
        visited[start] = true;

        cout << "\nDFS Traversal: ";

        while (top >= 0) 
        {
            int node = stack[top--]; 
            // cout << (node) << " ";
            printf("%c ",node+65);
            
            for (int i =size - 1; i >=0; i--)
             {
                if (adjMtx[node][i] == 1 && !visited[i]) 
                {
                    stack[++top] = i;
                    visited[i] = true;
                }
            }
        }
        cout << endl;
    }

    
    void BFS(int start)
    {
        int queue[100], front = 0, rear = 0;
        queue[rear++] = start;
        visited[start] = true;

        cout << "\nBFS Traversal: ";

        while (front < rear) 
        {
            int node = queue[front++]; 
            printf("%c ",node+65);

           
            for (int i = 0; i < size; i++) 
            {
                if (adjMtx[node][i] == 1 && !visited[i]) 
                {
                    queue[rear++] = i; 
                    visited[i] = true;
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
