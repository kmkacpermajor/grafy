from collections import defaultdict
import random

def create_matrix(n,cnt):
    matrix=[]               # tworzymy wyzerowaną 2 wymiarową tablicę
    for i in range(n):
        matrix.append([0 for j in range(n)])

    while cnt:              # dopóki liczba większa od zera
        x = random.randint(0, n - 2)    # losujemy koordynaty w górnym trójkącie
        y = random.randint(x + 1, n - 1)
        if matrix[x][y] == 0:   # jeśli puste dodajemy krawędź i zmniejszamy liczbe
            matrix[x][y] = 1
            cnt -= 1

    return matrix

def matrix_to_list(matrix):
    adjList = defaultdict(list) # tworzymy słownik
    for i in range(len(matrix)): # przechodzimy przez całą macierz sąsiedztwa 
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:   # jeśli istnieje krawędź w danym koordynacie
                adjList[i].append(j)   # do itego elementu słownika dodajemy jty indeks
    return adjList

def matrix_to_edge(matrix):
    edgeList=[] # tworzymy pustą tablicę
    for i in range(len(matrix)): # przechodzimy przez całą macierz sąsiedztwa 
        for j in range(len(matrix[i])):
            if matrix[i][j]==1: # jeśli istnieje krawędź w danym koordynacie
                edgeList.append([i, j]) # do tablicy dodajemy tablicę dwuelementową z itym i jtym indeksem

    return edgeList


def show_adj_list(adjList):
    for i in adjList:
        print(i, end="")
        for j in adjList[i]:
            print(" ->  {}".format(j),end="")
        print()
    print()


def BFS(graph, v, n, reprezentacja):

    visited = [False] * n   # tworzymy tablicę odwiedzonych wierzchołków

    queue = [] # tworzymy kolejkę

    queue.append(v) # dodajemy do kolejki podany wierzchołek
    
    while True:
        while queue: # dopóki kolejka nie jest pusta

            v = queue.pop(0) # ściągamy pierwszy element z kolejki 
            print (v, end = " ") # wypisujemy
            visited[v] = True # i odznaczamy jako odwiedzony

            # zależnie od reprezentacji szukamy następników i podajemy do kolejki
            if reprezentacja == "adjList":
                for i in graph[v]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            elif reprezentacja == "adjMatrix":
                for i in range(n):
                    if graph[v][i] == 1:
                        if visited[i] == False:
                            queue.append(i)
                            visited[i] = True
            elif reprezentacja == "edgeList":
                for el in graph:
                    if el[0] == v:
                        if visited[el[1]] == False:
                            queue.append(el[1])
                            visited[el[1]] = True

        # sprawdzamy czy przeszliśmy wszystkie wierzchołki, jeśli nie losujemy nieodwiedzony
        if False in visited:
            while True: 
                v = random.randint(0,n-1)
                if visited[v] == False:
                    queue.append(v)
                    break
        else:
            print()
            return

def DFS(graph, v, n, reprezentacja):

    visited = [False] * n # tworzymy tablicę odwiedzonych wierzchołków

    DFSalg(graph, v, visited, reprezentacja) # podajemy wierzchołek do algorytmu

    # dopóki nie przeszliśmy wszystkich wierzchołków losujemy nieodwiedzony
    while False in visited:
        while True:
            v = random.randint(0,n-1)
            if visited[v] == False:
                DFSalg(graph, v, visited, reprezentacja)
                break

    print()

def DFSalg(graph, v, visited, reprezentacja):
 
    visited[v] = True # odznaczamy wierzchołek jako odwiedzony
    print(v, end=' ') # wypisujemy

    # zależnie od reprezentacji poszukujemy następników i wywołujemy dla nich DFS 
    if reprezentacja == "adjList":
        for i in graph[v]:
            if visited[i] == False:
                DFSalg(graph, i, visited, reprezentacja)
    elif reprezentacja == "adjMatrix":
        for i in range(n):
            if graph[v][i] == 1:
                if visited[i] == False:
                    DFSalg(graph, i, visited, reprezentacja)
    elif reprezentacja == "edgeList":
        for el in graph:
            if el[0] == v:
                if visited[el[1]] == False:
                    DFSalg(graph, el[1], visited, reprezentacja)


def BFSlikeSort(graph, n, reprezentacja):
        
    in_degree = [0] * n # tworzymy tablicę pomocniczą ze stopniami wierzchołków
        
    # zależnie od reprezentacji ustalamy stopnie wierzchołków
    if reprezentacja == "adjList":
        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1
    elif reprezentacja == "adjMatrix":
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    in_degree[j] += 1
    elif reprezentacja == "edgeList":
        for el in graph:
            in_degree[el[1]] += 1

    queue = [] # tworzymy kolejkę
    for i in range(n): # dopisujemy do kolejki wszystkie wierzchołki o stopniu 0
        if in_degree[i] == 0:
            queue.append(i)

    sorted_nodes = [] # tworzymy tablicę wynikową

    while queue: # dopóki kolejka nie jest pusta

        v = queue.pop(0) # ściągamy pierwszy element z kolejki 
        sorted_nodes.append(v) # i dopisujemy go jako posortowany

        # zależnie od reprezentacji poszukujemy następników i dodajemy je do tablicy z następnikami 
        next = []
        if reprezentacja == "adjList":
            next = graph[v]
        elif reprezentacja == "adjMatrix":
            for i in range(n):
                if graph[v][i]:
                    next.append(i)
        elif reprezentacja == "edgeList":
            for el in graph:
                if el[0] == v:
                    next.append(el[1])

        # dla każdego następnika zmniejszamy jego stopień i jeśli jest równy 0 dodajemy go do kolejki
        for i in next:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    print (*sorted_nodes)

def DFSlikeSort(graph, n, reprezentacja):
    sorted_nodes = [] # tworzymy tablicę wynikową
    visited = [False] * n # tworzymy tablicę odwiedzonych wierzchołków

    # dopóki nie przeszliśmy wszystkich wierzchołków losujemy nieodwiedzony i podajemy go do algorytmu
    while False in visited:
        while True:
            v = random.randint(0,n-1)
            if visited[v] == False:
                DFSlikealg(graph, v, n, visited, sorted_nodes, reprezentacja)
                break
          
    print(*sorted_nodes[::-1])
 
def DFSlikealg(graph, v, n, visited, sorted_nodes, reprezentacja):
    visited[v] = True # odznaczamy wierzchołek jako odwiedzony

    # zależnie od reprezentacji poszukujemy następników i dodajemy je do tablicy z następnikami 
    next = []
    if reprezentacja == "adjList":
        next = graph[v]
    elif reprezentacja == "adjMatrix":
        for i in range(n):
            if graph[v][i] == 1:
                next.append(i)
    elif reprezentacja == "edgeList":
        for el in graph:
            if el[0] == v:
                next.append(el[1])

    # dla każdego nieodwiedzonego następnika wywołujemy algorytm
    for j in next:
        if visited[j] == False:
            DFSlikealg(graph, j, n, visited, sorted_nodes, reprezentacja)

    # po przejściu wszystkich następników danego wierzchołka dodajemy go jako posortowany
    sorted_nodes.append(v)

x = 1
while x:
    while True:
        print("Wybierz opcje")
        print("1 - generowanie grafu o n wierzchołkach")
        print("2 - generowanie grafu poprzed podanie wierszy macierzy sasiedztwa")
        op = int(input())
        if op in [1,2]:
            break

    while True:
        print("Podaj n")
        n = input()
        if n.isnumeric():
            n = int(n)
            break

    edges = (n*(n-1))//4
    adjMatrix = []

    if op == 1:

        adjMatrix = create_matrix(n,edges)

    if op == 2:
        for i in range(n):
            flag = True
            while flag:
                tmp = []
                print("Podaj wiersz nr: {}".format((i+1)))
                inp = input().split()
                for x in inp:
                    if x in ['0','1']:
                        tmp.append(int(x))
                if len(inp) == len(tmp) and len(tmp) == n:
                    break
            adjMatrix.append(tmp)



    adjList = matrix_to_list(adjMatrix)
    edgeList = matrix_to_edge(adjMatrix)

    print("\n\nAdjMatrix")
    print("   ",end="")
    print(*range(n))
    print()
    for x in range(n):
        print(x, end="  ")
        print(*adjMatrix[x])

    print("\n\nEdge list")
    for x in range(len(edgeList)):
        print(*edgeList[x])

    print("\n\nAdjList")
    show_adj_list(adjList)

    rand = random.randint(0,n-1)

    print("BFS")
    BFS(adjList, rand, n, "adjList")

    BFS(adjMatrix, rand, n, "adjMatrix")

    BFS(edgeList, rand, n, "edgeList")

    print()

    print("DFS")
    DFS(adjList, rand, n, "adjList")

    DFS(adjMatrix, rand, n, "adjMatrix")

    DFS(edgeList, rand, n, "edgeList")

    print()

    print("BFSlikeSort")
    BFSlikeSort(adjList, n, "adjList")

    BFSlikeSort(adjMatrix, n, "adjMatrix")

    BFSlikeSort(edgeList, n, "edgeList")

    print()

    print("DFSlikeSort")
    DFSlikeSort(adjList, n, "adjList")

    DFSlikeSort(adjMatrix, n, "adjMatrix")

    DFSlikeSort(edgeList, n, "edgeList")

    while True:
        print("0 - jesli chcesz zakonczyc program")
        print("1 - jesli chcesz wykonac go ponownie")
        x = int(input())
        if x in [0,1]:
            break
