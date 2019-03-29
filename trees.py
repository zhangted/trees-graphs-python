class TreeNode:
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

def invertIOT(inp):
	#inverted in order traversal
	#right,root,left
	if inp:
		invertIOT(inp.right)
		printNode(inp)
		invertIOT(inp.left)

def invertPREOT(inp):
	#invert pre order traversal
	#right,left,root
	if inp:
		invertPREOT(inp.right)
		invertPREOT(inp.left)
		printNode(inp)

def invertPOSTOT(inp):
	#invert post order traversal
	#root,right,left
	if inp:
		printNode(inp)
		invertPOSTOT(inp.right)
		invertPOSTOT(inp.left)
	

def main():
	#Tree structure like below
	# 10 -> 5,20
	# 5 -> 3,7
	# 20 -> 30

	root = TreeNode(10,TreeNode(5,TreeNode(3,None,None),TreeNode(7,None,None)),TreeNode(20,None,TreeNode(30,None,None)))
	postOrderTraversal(root)
	print(";;;;;\n")
	invertPOSTOT(root)
	

main()