## ex01-06-shortest-path-maximum-flow-and-transport-fernandoorge

### Table of contents
* [Repo organization](#repo-organization)
* [Solution to exercise 00](#solution-to-exercise-00)
* [Solution to exercise 01](#solution-to-exercise-01)
* [Solution to exercise 02](#solution-to-exercise-02)
* [Solution to exercise 03](#solution-to-exercise-03)
* [Solution to exercise 04](#solution-to-exercise-04)
* [Solution to exercise 05](#solution-to-exercise-05)
* [Solution to exercise 06](#solution-to-exercise-06)

### Repo organization

Each exercise of the assignment is solved in a different file
* ex00.py for exercise 00
* ex01.py for exercise 01
* ex02.py for exercise 02
* ex03.py for exercise 03 
* ex04.py for exercise 04 
* ex05.py for exercise 05
* ex06.py for exercise 06

### Solution to exercise 00
* logistics.py constains some useful functions developed by me. 
* The required algorithms to complete the assignment can be found there.
* The function **nn2na** used to convert a Node-Node Matrix into a Node-Arc Matrix can be found there.

### Solution to exercise 01

The raw solution will be: [1. 0. 1. 0. 0. 1. 0.]
Hence, 
* Arc ('s', '2') must be taken.
* Arc ('2', '4') must be taken.
* Arc ('4', 't') must be taken.
* The minimum cost will be: 5.00 .

### Solution to exercise 02

* SOLVING PROBLEM WITH: interior-point
  * The interior-point method is not able to find a solution.
* SOLVING PROBLEM WITH: simplex
  * The simplex algorithm gives us the optimal solution.
  * The raw solution will be: [0. 1. 0. 0. 1. 0. 1.]
  * Arc ('s', '3') must be taken.
  * Arc ('3', '5') must be taken.
  * Arc ('5', 't') must be taken.
  * The minimum cost will be: 5.00. 

### Solution to exercise 03

* Dijkstra algorithm implementacion can be found at **logistics.py**.

##### Solution to ex01 using DIJKSTRA

* Shortest path solution: ['s', '2', '4', 't']
* Cumulative distance   : [0.0, 2.0, 4.0, 5.0]
* Minimum distance      : 5

##### Solution to ex02 using DIJKSTRA

* Shortest path solution: ['s', '3', '5', 't']
* Cumulative distance   : [0.0, 1.0, 3.0, 5.0]
* Minimum distance      : 5


### Solution to exercise 04

The maximum flow will be: 5.00 
The raw solution will be: [4. 1. 1. 3. 1. 1. 1.]
* 4 units must be moved across ('s', '2') arc.
* 1 units must be moved across ('s', '3') arc.
* 1 units must be moved across ('2', '4') arc.
* 3 units must be moved across ('2', 't') arc.
* 1 units must be moved across ('3', '5') arc.
* 1 units must be moved across ('4', 't') arc.
* 1 units must be moved across ('5', 't') arc.

### Solution to exercise 05

##### DFS Algorithm
* **DFS** algorithm can be found at **logistics.py**.
* In order to test the DFS algorithm, I took all nodes permutations and execute DFS for each pair of nodes in G. 
* Some sample solutions can be found below:
```
Search a path between ['s', '2'] using DFS algorithm
    The path found was = ['s', '2']

Search a path between ['s', '3'] using DFS algorithm
    The path found was = ['s', '3']

Search a path between ['s', '4'] using DFS algorithm
    The path found was = ['s', '2', '4']

Search a path between ['s', '5'] using DFS algorithm
    The path found was = ['s', '3', '5']

Search a path between ['s', 't'] using DFS algorithm
    The path found was = ['s', '3', '5', 't']
```

##### Ford-Fulkerson Algorithm
* **DFS** algorithm can be found at **logistics.py**.
* In order to test FF algorithm, the max flow was calculated for graphs in ex02, ex03 y ex05
* Maximum flow solution for graph in EX05 = 5
* Maximum flow solution for graph in EX05 = 3
* Maximum flow solution for graph in EX05 = 4

### Solution to exercise 06
