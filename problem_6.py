class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    uniList = set()
    node = llist_1.head
    while node:
        uniList.add(node)
        node = node.next

    node = llist_2.head
    while node:
        uniList.add(node)
        node = node.next
    return uniList

def intersection(llist_1, llist_2):
    intersectList = set()
    newSecond  = LinkedList()

    node = llist_1.head
    while node:
        innode = llist_2.head
        previous = None
        while innode:
            #print(node.value, innode.value, node.value==innode.value)
            if node.value == innode.value: 
                intersectList.add(node)
                #print(node.value, innode.value,intersectList)
                if previous:
                    previous.next = innode.next
                else:
                    llist_2.head = innode.next
                #print(llist_2)
            previous = innode 
            innode = innode.next
        node = node.next
    return intersectList


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print()
print(linked_list_1)
print(linked_list_2)
print()
print ('union', union(linked_list_1,linked_list_2))
print ('intersection', intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print()
print(linked_list_3)
print(linked_list_4)
print()
print ('union', union(linked_list_3,linked_list_4))
print ('intersection', intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_6 = LinkedList()
linked_list_7 = LinkedList()

element_1 = [1,1,1,1,1,1,1,1]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_6.append(i)

for i in element_2:
    linked_list_7.append(i)

print()
print(linked_list_6)
print(linked_list_7)
print()
print ('union', union(linked_list_6,linked_list_7))
print ('intersection', intersection(linked_list_6,linked_list_7))
