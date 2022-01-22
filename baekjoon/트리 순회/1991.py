N = int(input())
tree = dict()

def preorder(root):
	print(root, end='')
	if tree[root][0] != '.':
		preorder(tree[root][0])
	if tree[root][1] != '.':
		preorder(tree[root][1])

def inorder(root):
	if tree[root][0] != '.':
		inorder(tree[root][0])
	print(root, end='')
	if tree[root][1] != '.':
		inorder(tree[root][1])

def postorder(root):
	if tree[root][0] != '.':
		postorder(tree[root][0])
	if tree[root][1] != '.':
		postorder(tree[root][1])
	print(root, end='')
	

for _ in range(N):
	node, left, right = input().split(' ')
	tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
