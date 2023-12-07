#include <iostream>
#include <list>
using namespace std;

class vertex{
    public:
        int data;
        list<vertex> neighbors;
        bool visited;
        vertex(int data){
            this->data = data;
            this->visited = false;
        }
};

class edge{
    public:
        vertex* v1;
        vertex* v2;
        int weight;
        edge(vertex* v1, vertex* v2, int weight){
            this->v1 = v1;
            this->v2 = v2;
            this->weight = weight;
        }
};

class Graph{
    public:
        list<vertex> vertices;
        list<edge> edges;

        void addVertex(int data){
            vertex* check = find_vertex(data);
            if (!check){
                vertex* v = new vertex(data);
                vertices.push_back(*v);
            }
            else{
                cout << "Vertex already exists" << endl;
            }
        }

        void addEdge(int data1, int data2, int weight){
            vertex* v1 = find_vertex(data1);
            vertex* v2 = find_vertex(data2);
            if (v1 && v2){
                edge* e = new edge(v1, v2, weight);
                edges.push_back(*e);
                v1->neighbors.push_back(*v2);
                v2->neighbors.push_back(*v1);
            }
            else{
                cout << "Enter the valid vertices" << endl;
            }
        }

        vertex* find_vertex(int data){
            for (auto i = vertices.begin(); i != vertices.end(); i++){
                if (i->data == data){
                    return &(*i);
                }
            }
            return NULL;
        }

        void show(){
            cout << "Vertices: " << endl;
            for (auto i = vertices.begin(); i != vertices.end(); i++){
                cout << i->data << " : ";
                for (auto j = i->neighbors.begin(); j != i->neighbors.end(); j++){
                    cout << j->data << " ";
                }
                cout << endl;
            }
            cout << "Edges: " << endl;
            for (auto i = edges.begin(); i != edges.end(); i++){
                cout << i->v1->data << " : " << i->v2->data << endl;
            }
        }
        void showList(list<vertex> l){
            cout << ">>>>>> " ;
            for (auto i = l.begin(); i != l.end(); i++){
                cout << i->data << " ";
            }
            cout << "<<<<<< " << endl;
        }
        // issue is with this function
        // it is not showing the correct neighbours of verices
        // althoug the neighbours are add correctly
        void dfs(vertex* v){
            for (auto i = vertices.begin(); i != vertices.end(); i++){
                i->visited = false;
            }
            v->visited = true;
            cout << v->data << " ";
            showList(v->neighbors);
            for (auto i = v->neighbors.begin(); i != v->neighbors.end(); i++){
                if (!i->visited){
                    dfs(&(*i));
                }
            }
        }
};

main(){
    Graph g;           // default constructor
    cout << "Graph created" << endl;
    g.addVertex(9);
    g.addVertex(1);
    g.addVertex(11);
    g.addVertex(7);
    // g.addVertex(7)
    g.addVertex(43);
    g.addVertex(3);
    g.addVertex(10);
    g.addVertex(15);
    g.addVertex(20);
    g.addEdge(11, 43, 10);
    g.addEdge(9, 7, 20);
    g.addEdge(9, 1, 20);
    g.addEdge(43, 7, 20);
    g.addEdge(20, 7, 20);
    g.addEdge(10, 3, 20);
    g.addEdge(1, 3, 20);
    g.addEdge(10, 1, 20);
    g.addEdge(10, 15, 20);
    // g.show();
    cout << "BFS:  " << endl;
    // g.bfs(g.find_vertex(9))
    cout << "DFS:  " << endl;

    g.dfs(g.find_vertex(9));
}