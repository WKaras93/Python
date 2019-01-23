import unittest

class Node:
    """Class represents a node for a one-way linked list."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleList:
    """Class represents a one-way linked list."""
    def __init__(self, *args):
        self.length = 0
        self.head = None
        self.tail = None
        for item in args:
            self.insert_head(item)
        
    def insert_head(self, data):
        node = Node(data)
        if(self.is_empty()):
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
    
    def insert_tail(self, data):
        node = Node(data)
        if(self.is_empty()):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def insert_middle(self, data, data2):
        node = Node(data)
        if(self.is_empty()):
            self.head = self.tail = node
        else:
            tmp = self.head
            while(tmp.data != data2):
                tmp = tmp.next
                if(tmp == None):
                    raise IndexError()
            tmp.next, node.next = node, tmp.next
        self.length += 1

    def is_empty(self):
        return (self.length == 0)
    
    def count(self):
        return self.length

    def __str__(self):
        if(self.is_empty()):
            return "List is empty"
        else:
            tmp = self.head
            container = str(tmp.data)
            while(tmp.next):
                tmp = tmp.next
                container += ","
                container += str(tmp.data)
            return container
    
    def __eq__(self, other):
        if(isinstance(other, SingleList)):
            tmp1 = self.head
            tmp2 = other.head
            while(tmp1 != None and tmp2 != None and tmp1.data == tmp2.data):
                tmp1 = tmp1.next
                tmp2 = tmp2.next
            return tmp1 == tmp2

    def remove_head(self):
        if(self.is_empty()):
            raise ValueError("List is empty")
        else:
            tmp, self.head = self.head, self.head.next
            self.length -= 1
            return tmp
    
    def remove_tail(self):
        if(self.is_empty()):
            raise ValueError("List is empty")
        elif(self.head == self.tail):
            tmp = self.head
            self.head = self.tail = None
            self.length -= 1
            return tmp
        else:
            tmp = self.head
            while(tmp.next != self.tail):
                tmp = tmp.next
            tmp2 = tmp.next
            self.tail, tmp.next = tmp, None
            self.length -= 1
            return tmp2
    
    def remove_middle(self, value):
        if(self.is_empty()):
            raise ValueError("List is empty")
        elif(self.head.data == value):
            return self.remove_head()
        else:
            tmp = self.head
            while(tmp.next.data != value):
                tmp = tmp.next
                if(tmp == self.tail):
                    raise ValueError("There is no such value on the list.")
            tmp.next, tmp2= tmp.next.next, tmp.next
            self.length -= 1
            return tmp2
    
    def merge(self, new_List):
        if(self.is_empty() and new_List.is_empty()):
            raise ValueError("Both lists are empty.")
        elif(self.is_empty()):
            self.head = new_List.head
        else:
            self.tail.next = new_List.head
    
    def find_max(self):
        if(self.is_empty()):
            raise ValueError("List are empty.")
        else:
            max_V = self.head
            tmp = self.head
            while(tmp.next != None):
                tmp = tmp.next
                if(tmp.data > max_V.data):
                    max_V = tmp
            return max_V

    def find_min(self):
        if(self.is_empty()):
            raise ValueError("List are empty.")
        else:
            min_V = self.head
            tmp = self.head
            while(tmp.next != None):
                tmp = tmp.next
                if(tmp.data < min_V.data):
                    min_V = tmp
            return min_V

class TestMySingleList(unittest.TestCase):
    def setUp(self):
        self.l1 = SingleList(1, 2, 3, 4, 7)
        self.l2 = SingleList()
    
    def test_is_empty(self):
        self.assertTrue(self.l2.is_empty())
        self.assertFalse(self.l1.is_empty())
    
    def test_insert(self):
        self.l2.insert_head(10)
        self.l1.insert_tail(9)
        self.assertEqual(str(self.l2), "10")
        self.assertEqual(self.l1, SingleList(9, 1, 2, 3, 4, 7))
        self.l1.insert_middle(10, 3)
        self.assertEqual(self.l1, SingleList(9, 1, 2, 10, 3, 4, 7))
    
    def test_remove(self):
        #self.assertEqual(self.l2.remove_head(), ValueError("List is empty"))
        self.assertEqual(self.l1.remove_tail().data, Node(1).data)
        self.assertEqual(self.l1.remove_middle(2).data, Node(2).data)
    
    def test_merge(self):
        self.l2.insert_head(10)
        self.l1.merge(self.l2)
        self.assertEqual(self.l1, SingleList(10, 1, 2, 3, 4, 7))
    
    def test_find_max(self):
        self.assertEqual(self.l1.find_max().data, Node(7).data)
    
    def test_find_min(self):
        self.assertEqual(self.l1.find_min().data, Node(1).data)

if __name__ == "__main__":
    unittest.main()