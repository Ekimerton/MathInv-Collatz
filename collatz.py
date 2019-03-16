class Node:
    def __init__(self, value):
        self.value = value
        self.parents = []
        self.child = None

nodes = [None for i in range(100000)]

nodes[1] = Node(1)

for i in range(1, NUM_OF_NODES):
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

        if(nodes[next] == None):
            nodes[next] = Node(next)
        else:
            nodes[next].parents.append(nodes[curr])
            nodes[curr].child = nodes[next]
            break

        nodes[next].parents.append(nodes[curr])
        nodes[curr].child = nodes[next]

        curr = next

nodeFive = nodes[16]
print(nodeFive.child.value)

parentz =  nodeFive.parents
print("real shit")
for x in parentz:
    print(x.value)
