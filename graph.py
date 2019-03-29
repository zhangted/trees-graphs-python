class TreeNode:
	def __init__(self, value):
		self.val = value
		self.children = []
		self.visited = False

	def addChild(self, child):
		self.children.append(child)

def printNode(inp):
	print(inp.val)

def dfs(root):
	#"rabbit hole" searching
	if not root: 
		return []
	printNode(root)
	root.visited = True
	for i in root.children:
		if i.visited == False:
			dfs(i)

def bfs(root):
	#nucleus to outer rings
	from collections import deque
	q = deque([root])
	res = [[]]
	thisLevel = []
	while len(q) > 0:
		thisLevel = []
		for i in xrange(len(q)):
			curNode = q.popleft()
			thisLevel.append(curNode.val)
			for j in curNode.children:
				q.append(j)
		print(thisLevel)


def main():
	#Tree structure like below
	# 10 -> 5,20
	# 5 -> 3,7
	# 20 -> 30

	root = TreeNode(10)
	left = TreeNode(5)
	right = TreeNode(20)
	root.addChild(left)
	root.addChild(right)
	left.addChild(TreeNode(3))
	left.addChild(TreeNode(7))
	right.addChild(TreeNode(30))

	bfs(root)
	print("\n")
	dfs(root)
	

main()