# ===== Tree Node =====
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ===== BST Insert =====
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    return root


# ===== Traversals =====
def inorder(root):  # LNR
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):  # NLR
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):  # LRN
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Level Order (BFS)
from collections import deque
def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# ===== Search in BST =====
def search_bst(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)


# ===== Min / Max in BST =====
def find_min(root):
    while root and root.left:
        root = root.left
    return root

def find_max(root):
    while root and root.right:
        root = root.right
    return root


# ===== Delete Node in BST =====
def delete_bst(root, val):
    if not root:
        return None
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Case 1: no child
        if not root.left and not root.right:
            return None
        # Case 2: one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Case 3: two children
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_bst(root.right, successor.val)
    return root


# ===== Height / Depth =====
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ===== Check Balanced Tree =====
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check(root) != -1


# ===== Lowest Common Ancestor =====
def lca_bst(root, p, q):
    if not root:
        return None
    if p < root.val and q < root.val:
        return lca_bst(root.left, p, q)
    if p > root.val and q > root.val:
        return lca_bst(root.right, p, q)
    return root


# ===== Diameter of Tree =====
def diameter_of_binary_tree(root):
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    depth(root)
    return diameter


# ===== Path Sum =====
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)


# ===== Invert / Mirror Tree =====
def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ===== Flatten Tree to Linked List =====
def flatten_tree(root):
    if not root:
        return
    flatten_tree(root.left)
    flatten_tree(root.right)
    if root.left:
        temp = root.right
        root.right = root.left
        root.left = None
        cur = root.right
        while cur.right:
            cur = cur.right
        cur.right = temp


# ===== Example usage =====
if __name__ == "__main__":
    nums = [30, 60, 70, 40, 10, 46]
    root = None
    for n in nums:
        root = insert_bst(root, n)

    print("Inorder Traversal (Sorted):")
    inorder(root)
    print("\nMax Depth:", max_depth(root))
    print("Diameter:", diameter_of_binary_tree(root))
