
class DoubleNode:
    def __init__(self, key,value):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
            
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    def remove(self,node):
        if(node.next != None):
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        if(node.previous!=None):
            node.previous.next = node.next
        else:
            self.head = node.next
        
    def pushTop(self,node):
        node.previous = None
        node.next = self.head
        if(self.head != None):
            self.head.previous = node
        self.head = node
        if( self.tail == None):
            self.tail = self.head

class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)         # we can use our put() method to rehash
                head = head.next
                
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_memory = HashMap(capacity)
        self.leastRecent = DoublyLinkedList()
        self.num_entries = 0
        self.capacity = capacity

    def get(self, key):
        returnNode = self.cache_memory.get(key)
        if(returnNode != None):
            self.leastRecent.remove(returnNode)
            self.leastRecent.pushTop(returnNode)
            return returnNode.value
        return -1
    def set(self,key,value):
        newNode = self.cache_memory.get(key)
        if(newNode == None):
            newNode = DoubleNode(key,value)
        
        # print("capacity ",self.capacity)
        if(self.num_entries < self.capacity):
            self.leastRecent.pushTop(newNode)
            # print(self.leastRecent.tail.key)
        else:
            # print('delete')
            # print(self.leastRecent.tail.key)
            self.cache_memory.delete(self.leastRecent.tail.key)
            self.num_entries-=1
            self.leastRecent.remove(self.leastRecent.tail)
            self.leastRecent.pushTop(newNode)
        self.cache_memory.put(key,newNode)
        self.num_entries+=1
        # print("num_entries",self.num_entries);

## First test case
our_cache = LRU_Cache(5)

# print("num_entries",our_cache.num_entries);
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2) )      # returns 2
print(our_cache.get(9) )     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Second test case
second_cache = LRU_Cache(1000)
# print("num_entries",our_cache.num_entries);
for i in range(1000):
    second_cache.set(i, i)


print(second_cache.get(1))       # returns 1
print(second_cache.get(202) )      # returns 2
print(second_cache.get(1002) )     # returns -1 because 9 is not present in the cache

second_cache.set(123, 523) 
second_cache.set(1001, 123)

print(second_cache.get(2))      # returns -1 because the cache reached it's capacity and 2 was the least recently used entry

## Third test case
third_cache = LRU_Cache(10000)
# print("num_entries",our_cache.num_entries);
for i in range(10000):
    third_cache.set(i, i)

print(third_cache.get(1))       # returns 1
print(third_cache.get(2022) )      # returns 2
print(third_cache.get(10002) )     # returns -1 because 9 is not present in the cache

third_cache.set(123, 5233) 
third_cache.set(10001, 1231)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 2 was the least recently used entry
