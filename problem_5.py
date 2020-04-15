import hashlib
from datetime import datetime

class Block:

      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash(data)
            self.next = None
      def calc_hash(self,data):
            sha = hashlib.sha256()
            hash_str = str(data).encode('utf-8')
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
            now = datetime.now()
            timestamp = datetime.timestamp(now)

            if self.head is None:
                  self.head = Block(timestamp,data,0)
                  return

            block = self.head
            previous_hash = None
            while block.next:
                  block = block.next

            block.next = Block(timestamp,data,block.hash)

bc = Blockchain()

bc.append("selam")
bc.append("hi")
bc.append("hola")

print(bc)