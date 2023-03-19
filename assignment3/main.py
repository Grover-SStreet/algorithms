import json

with open('content/data.json') as json_file:
    data = json.load(json_file)


class Node:
    def __init__(self, key: int = None, value: str = None, N: int = 0):
        self.key = key  # key
        self.value = value  # associated values
        self.left = None  # link to left subtree
        self.right = None  # link to right subtree
        self.N = N  # number of nodes in subtree rooted here


from typing import List


# class definition of binary search tree
# noinspection DuplicatedCode
class BST:
    def __init__(self, keys: List, vals: List):
        self.__root = None
        for (key, val) in zip(keys, vals):
            self.insert(key, val)

    # find the number of nodes in the tree
    def size(self) -> int:
        return self.__size(self.__root)

    # find the number of nodes in the subtree whose root is node
    def __size(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            return node.N

    # insert a new pair of key and associated value to the tree
    def insert(self, key: int, val: str) -> None:
        self.__root = self.__insert(self.__root, key, val)

    def __insert(self, node: Node, key: int, val: str) -> Node:
        # if the node does not exist, add new node
        if node is None: return Node(key, val, 1)
        if key < node.key:
            node.left = self.__insert(node.left, key, val)
        elif key > node.key:
            node.right = self.__insert(node.right, key, val)
        else:
            node.val = val
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node

    # print the tree horizontally
    def printTree(self) -> None:
        self.__printTree(self.__root)

    # recursively print the nodes from right to left
    def __printTree(self, node: Node, level: int = 0) -> None:
        if node is not None:
            self.__printTree(node.right, level + 1)
            print(' ' * 6 * level + '-> ' + str(node.key))
            self.__printTree(node.left, level + 1)

    # find the height of a node with given key
    def height(self, key: int) -> int:
        def internal_height(node):
            if node is None:
                return 0
            leftAns = internal_height(node.left)
            rightAns = internal_height(node.right)
            return max(leftAns, rightAns) + 1

        def internal_traverse(node):
            if node is None:
                return None
            if node.key == key:
                return node
            else:
                if key < node.key:
                    temp_one = internal_traverse(node.left)
                elif key > node.key:
                    temp_one = internal_traverse(node.right)
                else:
                    temp_one = None
                return temp_one

        node_found = internal_traverse(self.__root)
        if node_found is not None:
            left_height = internal_height(node_found.left)
            right_height = internal_height(node_found.right)
            return max(left_height, right_height)
        else:
            return -1

    # get the value at a node with a given key
    def getValue(self, key: int) -> str:
        return self.__getValue(self.__root, key)

    def __getValue(self, node: Node, key: int) -> str:
        if node is None: return None
        if key < node.key:
            return self.__getValue(node.left, key)
        elif key > node.key:
            return self.__getValue(node.right, key)
        else:
            return node.value

    def min(self) -> int:
        left_side = self.__root
        while left_side.left is not None:
            left_side = left_side.left
        return left_side.key

    # return the maximum key of the tree
    def max(self) -> int:
        right_side = self.__root
        while right_side.right is not None:
            right_side = right_side.right
        return right_side.key

    def floor(self, key: int):
        if self.__root is None:
            return -1

        if self.__root.key == key:
            return self.__root.key
        elif self.__root.key > key:
            side = self.__root.left
        else:
            side = self.__root.right

        while True:
            if side.left is not None and side.right is not None:
                if side.key < key:
                    side = side.right
                elif side.key > key:
                    side = side.left
            elif side.right is not None:
                if side.key < key:
                    if side.right.key > key:
                        return side.key
                    else:
                        side = side.right
            elif side.left is not None:
                if side.key > key:
                    if side.left.key < key:
                        return side.key
                else:
                    side = side.left
            else:
                if key < side.key:
                    if self.__root.key < key:
                        return self.__root.key
                    else:
                        return None
                elif key == side.key:
                    return key
                else:
                    return side.key

    def ceiling(self, key: int):
        if self.__root is None:
            return -1

        if self.__root.key == key:
            return self.__root.key
        elif self.__root.key > key:
            side = self.__root.left
        else:
            side = self.__root.right

        while True:
            if side.left is not None and side.right is not None:
                if side.key < key:
                    side = side.right
                elif side.key > key:
                    if side.left.key < key < side.key:
                        return side.key
                    else:
                        side = side.left
            elif side.right is not None:
                if side.key > key:
                    if side.right.key > key:
                        return side.key
                    else:
                        side = side.right
                else:
                    side = side.right
            elif side.left is not None:
                if side.key > key:
                    if side.left.key < key:
                        return side.key
                else:
                    side = side.left

            else:
                if key > side.key:
                    if self.__root.key < key:
                        return None
                    else:
                        return self.__root.key
                elif key == side.key:
                    return key
                else:
                    return side.key

    def rank(self, key: int) -> int:
        def find_size(node):
            size = 1
            if node.left is not None and node.key < key:
                size += find_size(node.left)
            if node.right is not None and node.key < key:
                size += find_size(node.right)

            if node.key > key or node.key == key:
                size -= 1
            if node.key > key and node.left is not None:
                size += find_size(node.left)
            return size

        def find_internal_rank(node):
            count = 0
            if key == self.__root.key:
                if node is None:
                    return 0
                else:
                    return find_size(self.__root.left)
            if key > self.__root.key:
                count += 1
                if self.__root.left is not None:
                    count += find_size(self.__root.left)
                if self.__root.right is not None:
                    count += find_size(self.__root.right)
                return count
            if key < self.__root.key:
                if self.__root.left is not None:
                    count += find_size(self.__root.left)
                return count

        return find_internal_rank(self.__root)

    def delete(self, key: int) -> None:
        def min_node(node):
            left_side = node
            while node.left is not None:
                left_side = node.left
            return left_side

        def delete_node(node, temp_key):
            if node is None:
                return node
            if node.key > temp_key:
                node.left = delete_node(node.left, temp_key)
            elif node.key < temp_key:
                node.right = delete_node(node.right, temp_key)
            else:
                if node.left is None:
                    temp = node.right
                    return temp

                elif node.right is None:
                    temp = node.left
                    return temp

                temp_node = min_node(node.right)
                node.key = temp_node.key
                node.right = delete_node(node.right, temp_node.key)
            return node

        self.__root = delete_node(self.__root, key)

    def avlBalance(self) -> None:
        def left_rot(node):

            temp_node = node.right
            temp_left = temp_node.left

            temp_node.left = node
            node.right = temp_left

            if node.left is not None:
                height_one = self.height(node.left.key)
            else:
                height_one = 0
            if node.right is not None:
                height_two = self.height(node.right.key)
            else:
                height_two = 0

            node.N = max(height_one, height_two)

            if temp_node.left is not None:
                height_one = self.height(temp_node.left.key)
            else:
                height_one = 0
            if temp_node.right is not None:
                height_two = self.height(temp_node.right.key)
            else:
                height_two = 0

            temp_node.N = max(height_one, height_two)

            return temp_node

        def right_rot(node):

            temp_node = node.left
            right_temp_node = temp_node.right

            temp_node.right = node
            node.left = right_temp_node

            if node.left is not None:
                height_one = self.height(node.left.key)
            else:
                height_one = 0
            if node.right is not None:
                height_two = self.height(node.right.key)
            else:
                height_two = 0

            node.N = max(height_one , height_two)

            if temp_node.left is not None:
                height_one = self.height(temp_node.left.key)
            else:
                height_one = 0
            if temp_node.right is not None:
                height_two = self.height(temp_node.right.key)
            else:
                height_two = 0

            temp_node.N = max(height_one, height_two)

            return temp_node

        def get_balance(node):
            if self.__root.key != node.key:
                return 0
            return self.height(node.left.key) - self.height(node.right.key)

        def is_balanced(node):
            balance = get_balance(node)

            if balance > 1 and node.key < node.left.key:
                return right_rot(node)

            if balance < -1 and node.key > node.right.key:
                return left_rot(node)

            if balance > 1 and node.key > node.left.key:
                node.left = left_rot(node.left)
                return right_rot(node)

            if balance < -1 and node.key < node.right.key:
                node.right = right_rot(node.right)
                return left_rot(node)

            return node

        self.__root = is_balanced(self.__root)


# test case 1
tc_1 = BST(**data['testcase_1'])
print("The original tree")
tc_1.printTree()

tc_1.insert(5,"Hello")
print("\nThe tree after adding key 5")
tc_1.printTree()

print("\nThe tree after balancing")
tc_1.avlBalance()
tc_1.printTree()