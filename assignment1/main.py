class Stack:
    """
    Class implementation of a stack utilizing Linked-Lists

    Attributes:
        front (Node): Head of the stack
        size (Int): Number of elements in the Stack
    """

    def __init__(self):
        self.front = None
        self.size = 0

    class Node:
        """
        Models a node within the Linked-List / Stack

        Attributes:
            item (Any): Data element of the Node
            next (Node): Pointer to next Node
        """

        def __init__(self, item_param):
            self.item = item_param
            self.next = None

    def isEmpty(self):
        """
        Determines if the stack is empty or not

        Returns:
            (bool): True or False

        """
        return self.front is None

    def push(self, data):
        """
        Pushes an item onto the Stack

        Args:
            data: data element to initialize node with

        Returns:
            None
        """

        if self.front is None:
            self.front = self.Node(data)
            self.size += 1
        else:
            self.size += 1
            temp_node = self.Node(data)
            temp_node.next = self.front
            self.front = temp_node

    def pop(self):
        """
        Removes the last in element from the stack

        Returns:
            (Node): The node that was popped off the stack

        """
        if self.isEmpty():
            return None
        else:
            self.size -= 1
            temp_node = self.front
            self.front = self.front.next
            temp_node.next = None
            return temp_node.item

    def __len__(self):
        """
        Class implementation of length

        Returns:
            (int): Size of the stack

        """
        return self.size

    def __str__(self) -> str:
        """
        String implementation of class that prints the Linked-List / Stack contents.

        Returns:
            output_str (String): A string representation of the Stack

        """
        output_str = "["
        self.__iter_node = self.front
        while True:
            if self.__iter_node is not None:
                output_str += f'{self.__iter_node.item}'
                self.__iter_node = self.__iter_node.next
            if self.__iter_node is not None:
                output_str += ','
            else:
                break
        output_str += ']'
        return output_str


def evaluate(exp: str) -> float:
    math_problem = exp.split(' ')
    stack_operator = Stack()
    stack_operand = Stack()

    lam_operator_mapping = {"+": (lambda x, y: x + y),
                            "-": (lambda x, y: x - y),
                            "/": (lambda x, y: x / y),
                            "*": (lambda x, y: x * y)
                            }

    for item in math_problem:
        if item in "+-*/":
            stack_operator.push(item)
        elif item not in "()":
            stack_operand.push(item)
        elif item == ")":
            value1 = stack_operand.pop()
            value2 = stack_operand.pop()
            temp_oper = stack_operator.pop()
            value = lam_operator_mapping[temp_oper](float(value2), float(value1))
            stack_operand.push(value)

    return stack_operand.pop()


if __name__ == "__main__":
    assert (evaluate("( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )") == 101.0)
    assert (evaluate("( ( 9 * 7 ) + ( 8 / ( 10 + 6 ) ) )") == 63.5)