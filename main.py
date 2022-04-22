from collections import defaultdict

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


def matrix_to_list(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjList[i].append(j)
    return adjList


def print_adj_list(adjList):
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
    opcja = int(input())

    print("Podaj n")
    n = int(input())

    if opcja == 1:
        adjMatrix = []
        for i in range(n):
            adjMatrix.append([0 for j in range(n)])
        print(adjMatrix)
        print()
        adjMatrix[0][1]=1
        adjMatrix[0][2]=1

        adjList = matrix_to_list(adjMatrix)
        print_adj_list(adjList)






    print("0 - jesli chcesz zakonczyc program")
    print("1 - jesli chcesz wykonac go ponownie")
    x=int(input())





