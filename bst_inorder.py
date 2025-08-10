class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Treenode(val)
            return
        
        current = self.root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = Treenode(val)
                    break
            elif val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = Treenode(val)
                    break
            else:
                break  # No duplicates
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val,end=" ")
            self.inorder(node.right)

nums = [30,60,70,40,10,46]
mytree = BST()

for i in nums:
    mytree.insert(i)

mytree.inorder(mytree.root)

