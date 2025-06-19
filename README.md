# Efficient Implementation of Graph Homomorphism Counting Algorithm

## Description

This C++ library computes the number of graph homomorphisms between two graphs H and G using Diaz, Serna and Thilikos's dynamic programming algorithm on a nice tree decomposition. Greedy heuristics are used to find a tree decomposition. 
<br><br>The complexity of this algorithm is polynomial to the treewdith of the NTD - O(poly(|V(H)|)\*|V(G)|^{tw(H)+1}). If H is a tree, the complexity becomes O(|V(H)|\*|E(G)|).
<br><br>Pybind11 is used to run this library in a Python environment.

## Usage

Define Graph by the number of vertices and add edges using addEdge manually:
````
from homlib import Graph, countHom

H = Graph(3)
H.addEdge(0, 1)
H.addEdge(1, 2)

G = Graph(3)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 0)

print(hom(H, G))
````

````
12
````
<br>Define Graph by the adjacency matrix:

## Installation

````
git clone https://github.com/kevinwangwkw/CountHom
pip3 install ./homlib
````
