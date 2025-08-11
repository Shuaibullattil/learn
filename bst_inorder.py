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

    def  search_bst(self,node,val):
        if not node or node.val == val:
            return node
        if node.val > val:
            return self.search_bst(node.left,val)
        else:
            return self.search_bst(node.right,val)

nums = [30,60,70,40,10,46]
mytree = BST()

for i in nums:
    mytree.insert(i)

print("Inorder Traversal:", end=" ")
mytree.inorder(mytree.root)

result = mytree.search_bst(mytree.root, 100)
if result:
    print("\nFound:", result.val)
else:
    print("\nNot found")
