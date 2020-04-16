import hashlib
from datetime import datetime

class Block:

      def __init__(self,data):
            self.timestamp = datetime.timestamp(datetime.now())
            self.data = data
            self.previous_hash = 0
            self.hash = self.calc_hash(data)
            self.next = None
      def calc_hash(self,data):
            sha = hashlib.sha256()
            hash_str = (str(self.previous_hash)+str(data)+str(self.timestamp)).encode('utf-8')
            sha.update(hash_str)
            return sha.hexdigest()
class Blockchain:
      def __init__(self):
            self.head = None
      def __str__(self):
            cur_head = self.head
            out_string = ""
            while cur_head:
                  out_string += str(cur_head.hash)+":"+str(cur_head.data) + " -> "
                  cur_head = cur_head.next
            return out_string
      def size(self):
            size = 0
            node = self.head
            while node:
                  size += 1
                  node = node.next
            return size
      def append(self, data):
            if self.head is None:
                  self.head = Block(data)
                  return

            block = Block(data)
            block.previous_hash = self.head.hash
            block.next = self.head
            self.head = block

bc = Blockchain()

bc.append("selam")
bc.append("hi")
bc.append("hola")

print(bc)


bc1 = Blockchain()

bc1.append("wonder")
bc1.append("land")
bc1.append("never")

print(bc1)


bc2 = Blockchain()

bc2.append("covid")
bc2.append("hide")
bc2.append("blood")

print(bc2)