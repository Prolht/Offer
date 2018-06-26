class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
pNode = TreeNode(pNode)
pTemp = TreeNode(pTemp)
def MirrorRecursively(pNode):
    if pNode ==None:
        return 
    if pNode.left == None & pNode.right == None:
        return
    pTemp = pNode.left
    pNode.left = pNode.right
    pNode.right = pTemp
    if pNode.left:
        MirrorRecursively(pNode.left)
    if pNode.right:
        MirrorRecursively(pNode.right) 