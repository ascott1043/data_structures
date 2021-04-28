

class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get_len(self):
        if not self.head:
            return 0

        length = 0
        n = self.head
        while n:
            length += 1
            n = n.next
        return length

    def __check_index__(self, position):
        if position > self.get_len() or position < 0:
            raise Exception("Index Out of Range")   

    def add_beg(self, data):
        self.head = Node(data, self.head)

    def add_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return

        n = self.head
        while n.next:
            n = n.next
        n.next = Node(data, None)

    def remove_last(self):
        if not self.head:
            raise Exception("List is empty")

        n = self.head
        while n.next.next:
            n = n.next
        n.next = None

    def remove_beg(self):
        if not self.head:
            return("List is empty")

        if not self.head.next:
            self.head = None
            return 

        self.head = Node(self.head.next.data, self.head.next.next)

    def remove_at(self, position):
        if not self.head:
            raise Exception("List is empty")
        
        self.__check_index__(position)

        if self.get_len() == position:
            self.remove_last()
            return

        counter = 0
        n = self.head
        while position - 1 > counter:
            n = n.next
            counter += 1

        n.data = n.next.data
        n.next = n.next.next
        return
 
    def add_at(self, data, position):
        self.__check_index__(position)

        if position == 1:
            self.add_beg(Node(data, self.head))

        if position == self.get_len():
            self.add_end(Node(data, None))

        n = self.head
        count = 0

        while position - 1 < count:
            n = n.next
            count += 1

        n.next = Node(data, n.next)

    def add_after(self, data, value):

        n = self.head
        while n:
            if n.data == value:
                node = Node(data, n.next)
                n.next = node
                return
            n = n.next
        print(f'No value {value} in list')
        return 

    def remove_value(self, data):

        n = self.head
        while n:
            if n.data == data:
                if n.next:
                    n.data = n.next.data
                    n.next = n.next.next
                    return
                else:
                    self.remove_last()
            n = n.next
        print(f"{data} does not exist in list")

    def show(self):
        if not self.head:
            return("Empty List")

        liststr = ''
        n = self.head
        while n:
            if n.next:
                liststr += str(n.data) + " > "
                n = n.next
            else:
                liststr += str(n.data)
                break
        return liststr



if __name__ == '__main__':

    ll = LinkedList()

    ll.add_end(10)
    ll.add_beg(5)
    ll.add_end(15)
    ll.add_beg(2)
    ll.add_beg(1)
    ll.add_after(6, 15)
    ll.remove_value(15)
    # ll.add_at(20, 6)


    print("length: ", ll.get_len())
    print(ll.show())
