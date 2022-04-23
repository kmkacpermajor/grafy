from collections import defaultdict
import random

'''
class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        #self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        #self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(val, end=" ")
            print()
'''


def create_matrix(n,edges):
    matrix=[]
    for i in range(n):
        matrix.append([0 for j in range(n)])

    cnt = edges
    while cnt:
        x = random.randint(0, n - 2)
        y = random.randint(x + 1, n - 1)
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            cnt -= 1

    return matrix

def matrix_to_list(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjList[i].append(j)
    return adjList

def matrix_to_edge(matrix):
    edgeList=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                edgeList.append([i, j])

    return edgeList


def show_adj_list(adjList):
    for i in adjList:
        print(i, end="")
        for j in adjList[i]:
            print(" ->  {}".format(j),end="")
        print()


x = 1
while x:
    print("Wybierz opcje")
    print("1 - genetowanie grafu o n wierzchołkach")
    print("2 - genetowanie grafu poprzed podanie wierszy macierzy sasiedztwa")
    op = int(input())

    print("Podaj n")
    n = int(input())
    edges = (n*(n-1))//4
    adjMatrix = []

    if op == 1:

        adjMatrix = create_matrix(n,edges)

    if op == 2:
        for i in range(n):
            print("Podaj wiersz nr: {}".format(i))
            adjMatrix.append([int(x) for x in input().split()])



    adjList = matrix_to_list(adjMatrix)
    edgeList = matrix_to_edge(adjMatrix)

    print("\n\nAdjMatrix")
    for x in range(n):
        print(*adjMatrix[x])

    print("\n\nEdge list")
    for x in range(len(edgeList)):
        print(*edgeList[x])

    print("\n\nAdjList")
    show_adj_list(adjList)




    print("0 - jesli chcesz zakonczyc program")
    print("1 - jesli chcesz wykonac go ponownie")
    x = int(input())





