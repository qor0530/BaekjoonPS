n = int(input())
nodes = {}
for i in range(n):
    node, leftnode, rightnode = input().split()
    nodes[node] = (leftnode, rightnode)

def preorder(node):
    print(node, end="")
    if nodes[node][0] != ".":
        preorder(nodes[node][0])
    if nodes[node][1] != ".":
        preorder(nodes[node][1])

def inorder(node):
    if nodes[node][0] != ".":
        inorder(nodes[node][0])
    print(node, end="")
    if nodes[node][1] != ".":
        inorder(nodes[node][1])

def postorder(node):
    if nodes[node][0] != ".":
        postorder(nodes[node][0])
    if nodes[node][1] != ".":
        postorder(nodes[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")