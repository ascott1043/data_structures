# O(log n)
#
#

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
                return
            self.left = BinaryTreeNode(data)
            return

        if data > self.data:
            if self.right:
                self.right.add_child(data)
                return
            self.right = BinaryTreeNode(data)
            return

    def in_order_traversal(self):
        elements = []

        #traverse left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #traverse to base node
        elements.append(self.data)

        #traverse to right tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                 return self.left.search(val)
            else:
                return False


        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def min(self):
        if self.left:
            return self.left.min()
        return self.data



    def max(self):
        if self.right:
            return self.right.max()
        return self.data

    def sum(self):
        sum = 0
        for nbr in self.in_order_traversal():
            sum += nbr
        return sum

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)


        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):

    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root





if __name__ == '__main__':
    numbers = [15, 12, 7, 14, 27, 20, 88, 23]
    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())

    print("max: ", numbers_tree.max())
    print("min: ", numbers_tree.min())
    print("sum: ", numbers_tree.sum())
    print('post_order:')
    print(numbers_tree.post_order_traversal())
    print('pre_order')
    print(numbers_tree.pre_order_traversal())

    numbers_tree = numbers_tree.delete(27)
    print(numbers_tree.pre_order_traversal())
