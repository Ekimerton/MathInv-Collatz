import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
from graphviz import Digraph

nodeCount = int(input("enter number to go up to: ")) + 1

graph = Digraph(comment='Collatz-by-kimmy')

class Node:
    def __init__(self, value):
        self.value = value
        self.parents = []
        self.child = None

nodes = [None for i in range(100000)]
nodes[1] = Node(1)

for i in range(1, nodeCount):
    curr = i
    next = -1
    if(nodes[curr] != None):
        continue

    while(curr != 1):

        ##Where the operations are applied
        if(curr % 2 == 0):
            next = int(curr / 2)
        else:
            next = int(3 * curr + 1)

        if(nodes[curr] == None):
            nodes[curr] = Node(curr)
            graph.node(str(curr))

        if(nodes[next] == None):
            nodes[next] = Node(next)
            graph.node(str(next))
        else:
            nodes[next].parents.append(nodes[curr])
            nodes[curr].child = nodes[next]
            graph.edge(str(curr), str(next), constraint='false')
            break

        nodes[next].parents.append(nodes[curr])
        nodes[curr].child = nodes[next]
        graph.edge(str(curr), str(next), constraint='false')

        curr = next


graph.render('Collatz-by-kimmy', view=True)
