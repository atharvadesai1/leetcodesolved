class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return True
    array = []
    leaf_nodes = []
    height = 1
    array.append((root,height))
    while array:
        current_node, height = array.pop(0)
        if current_node.left:
            array.append((current_node.left, height+1))
        if current_node.right:
            array.append((current_node.right, height+1))
        if not current_node.left and not current_node.right:
            leaf_nodes.append(height)

    for i in range(len(leaf_nodes)-1):
        for j in range(i+1, len(leaf_nodes)):
            leaf1 = leaf_nodes[i]
            leaf2 = leaf_nodes[j]
            diff = abs(leaf1-leaf2)
            if diff>1:
                return False
    return True

tree = [3,9,20,None,None,15,7]
root = TreeNode(tree[0])
root.left = tree[1]
root.right = tree[2]
current_node = root.left

def create_binary_tree_from_list(tree, index=0):
    if index < len(tree):
        if tree[index] is not None:
            node = TreeNode(tree[index])
            node.left = create_binary_tree_from_list(tree, 2 * index + 1)
            node.right = create_binary_tree_from_list(tree, 2 * index + 2)
            return node
    return None

tree_values = [3, 9, 20, None, None, 15, 7]
print(f'Tree: {tree_values}')
root = create_binary_tree_from_list(tree_values)

ans = isBalanced(root)
if ans:
    print('It is a Binary Tree')
else:
    print('It is not a Binary Tree')
