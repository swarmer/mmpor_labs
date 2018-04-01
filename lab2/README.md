# lab2

Вариант 1

## Описание алгоритма
An implementation of a cost-scaling push-relabel algorithm for the assignment problem (minimum-cost perfect bipartite matching), from the paper of Goldberg and Kennedy (1995). 

This implementation finds the minimum-cost perfect assignment in the given graph with integral edge weights set through the SetArcCost method. 

The running time is O(n*m*log(nC)) where n is the number of nodes, m is the number of edges, and C is the largest magnitude of an edge cost. In principle it can be worse than the Hungarian algorithm but we don't know of any class of problems where that actually happens. An additional sqrt(n) factor could be shaved off the running time bound using the technique described in http://dx.doi.org/10.1137/S0895480194281185 (see also http://theory.stanford.edu/~robert/papers/glob_upd.ps). 

## Installation
Create a python3 virtualenv  
`pip install -Ur requirements.txt`
