class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        pre_order_list = []
        def traverse(root):
            if not root:
                return
            pre_order_list.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return pre_order_list

    def __len__(self):
        return len(self.pre_order())

    def __getitem__(self, position):
        return self.pre_order()[position]

    def __iter__(self):
        return self

    def __next__(self):
        return self.root.value


if __name__ == "__main__":
    print('working')
    b = BinaryTree()
    b.root = Node(1)
    b.root.right = Node(3)
    b.root.left = Node(2)
    lengthIs = len(b)
    position = b[1]
    print('the length of this tree is:', lengthIs)
    print('the node in the second position is:', position)
    for item in b:
        print(item)