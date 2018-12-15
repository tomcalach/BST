class Node:

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.l_child = left_child
        self.r_child = right_child


class BST:

    def __init__(self, root=None):
        self.root = root

    def create_root(self, node):
        if not self.root and type(node) == Node:
            self.root = node

    def insert_node(self, node):
        checked_node = self.root
        while 1:
            if node.value < checked_node.value:
                if not checked_node.l_child:
                    checked_node.l_child = node
                    break
                else:
                    checked_node = checked_node.l_child

            if node.value >= checked_node.value:
                if not checked_node.r_child:
                    checked_node.r_child = node
                    break
                else:
                    checked_node = checked_node.r_child

    def min(self):
        node = self.root
        while node.l_child:
            print(node.value)
            node = node.l_child
        return node.value


b_tree = BST(Node(20))
for val in [8, 22, 4, 12, 10, 14]:
    b_tree.insert_node(Node(val))

print(b_tree.min())


