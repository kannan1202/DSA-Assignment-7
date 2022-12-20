#TODO: Question 1:
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#Preorder tree traversal using iterative approach:
def preorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack)>0:
        current = stack.pop()
        print(str(current.data),end=" ")

        if current.right!=None:
            stack.append(current.right)
        if current.left!=None:
            stack.append(current.left)

#Inorder tree traversal using iterative approach:
def inorder(root):
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif len(stack) > 0:
            current = stack.pop()
            print(str(current.data),end=" ")
            current = current.right

        else:
            break

#Postorder tree traversal using iterative approach:
def postorder(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) > 0:
        current = stack1.pop()
        stack2.append(current)

        if current.left != None:
            stack1.append(current.left)
        if current.right != None:
            stack1.append(current.right)

    while len(stack2) > 0:
        popped = stack2.pop()
        print(str(popped.val),end=" ")



root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)

# print("The preorder tree traversal for the binary tree is: ")
# preorder(root)

# print("The inorder tree traversal for the binary tree is: ")
# inorder(root)

print("The postorder tree traversal for the binary tree is: ")
postorder(root)
