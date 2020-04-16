import sys
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Node(object):
        
    def __init__(self,value = None,p=0):
        self.value = value
        self.priority = p
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
    def get_priority(self):
        return self.priority
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()}:{self.get_priority()})"
    
    def __str__(self):
        return f"Node({self.get_value()}:{self.get_priority()})"
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
    def get_root(self):
        return self.root
    def set_root(self,node):
        self.root = node
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level
        return s

def huffman_tree(data):
    freq = dict()
    for c in data:
        freq[c] = freq.get(c,0)+1    
    queue = Queue()
    for f in sorted(freq, key=freq.get):
       queue.enq(Node(f,freq[f]))
    while len(queue)>1:
        node_left = queue.deq()
        node_right = queue.deq()
        new = Node(None,node_left.priority+node_right.priority)
        new.set_left_child(node_left)
        new.set_right_child(node_right)
        queue.enq(new)
    huffTree = Tree()
    huffTree.set_root(queue.deq())
    return huffTree

def huffman_encoding(data):
    tree = huffman_tree(data)
    str = ''
    huffmanCode = dict()
    huffman_encoder(tree.get_root(),str,huffmanCode)
    encoded_data = ''
    for c in data:
        encoded_data = encoded_data + huffmanCode[c]
    # print(huffmanCode)
    return encoded_data, tree

def huffman_encoder(root, str, huffmanCode):
    if (root is None):
        return
    if (root.get_left_child() is None and root.get_right_child() is None):
        huffmanCode[root.value] = str
    huffman_encoder(root.get_left_child(),str+'0',huffmanCode)
    huffman_encoder(root.get_right_child(),str+'1',huffmanCode)

def huffman_decoder(root,str,index):
    if (root is None):
        return '', index
    if (root.get_left_child() is None and root.get_right_child() is None):
        return root.get_value(), index
    index = index+1
    if(str[index]=='0'):
        return huffman_decoder(root.get_left_child(),str,index)
    elif(str[index]=='1'):
        return huffman_decoder(root.get_right_child(),str,index)

def huffman_decoding(data,tree):
    decoded_data = ''
    index = -1
    while (index < len(data)-1):
        root = tree.get_root()
        d,index = huffman_decoder(root,data,index)

        decoded_data = decoded_data+d
    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "abcdefghijklmnopqrstuvyz"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))