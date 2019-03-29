class TreeNode:
	val = None
	left = None
	right = None
	def __init__(self, value, left, right):
		self.val = value
		self.left = left
		self.right = right

def printNode(inp):
	print(inp.val)

def inOrderTraversal(inp):
	#left,root,right
	if inp:
		inOrderTraversal(inp.left)
		printNode(inp)
		inOrderTraversal(inp.right)

def preOrderTraversal(inp):
	#root,left,right
	if inp:
		printNode(inp)
		preOrderTraversal(inp.left)
		preOrderTraversal(inp.right)

def postOrderTraversal(inp):
	#left,right,root
	if inp:
		postOrderTraversal(inp.left)
		postOrderTraversal(inp.right)
		printNode(inp)
	

def main():
	#Tree structure like below
	# 10 -> 5,20
	# 5 -> 3,7
	# 20 -> 30

	root = TreeNode(10,TreeNode(5,TreeNode(3,None,None),TreeNode(7,None,None)),TreeNode(20,None,TreeNode(30,None,None)))
	postOrderTraversal(root)
	

main()