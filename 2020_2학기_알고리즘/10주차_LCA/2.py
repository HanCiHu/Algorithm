def preorder(node):
	if node == '.':
		return
	print(node, end = " ")
	preorder(tree[node][0])
	preorder(tree[node][1])

def inorder(node):
	if node == '.':
		return
	inorder(tree[node][0])
	print(node, end = " ")
	inorder(tree[node][1])

def postorder(node):
	if node == '.':
		return
	postorder(tree[node][0])
	postorder(tree[node][1])
	print(node, end = " ")

n = int(input())
tree = {}
visit = {}
for _ in range(n):
	root, left, right = input().split(' ')
	tree[root] = (left, right)
	visit[root] = 0

for i in tree.keys():
	if tree[i][0] != '.':
		visit[tree[i][0]] = 1
	if tree[i][1] != '.':
		visit[tree[i][1]] = 1

tree_root = 0

for i in visit.keys():
	if visit[i] == 0:
		tree_root = i
preorder(tree_root)
print()
inorder(tree_root)
print()
postorder(tree_root)
