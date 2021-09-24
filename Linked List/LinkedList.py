class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)

    def length(self):
        total = 0
        current = self.head
        while current.next != None:
            total+=1
            current = current.next
        return total

    def get(self, index):
        if index >= self.length():
            print("Error")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx +=1
    def erase(self,index):
        if index >= self.length():
            print("Error")
            return None
        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                break
            cur_idx +=1




my_list = linked_list()
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()

print(my_list.length())
print(my_list.get(2))
my_list.erase(2)
my_list.display()