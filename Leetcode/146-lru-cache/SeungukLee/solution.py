class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # double linkedlist + hashmap
    def __init__(self, capacity: 'int'):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.node_dict = {} # key: int, value: Node
        
    def get(self, key: 'int') -> 'int':
        if key not in self.node_dict:
            return -1
        
        cur = self.node_dict[key]
        if cur != self.head:
            if cur != self.tail:
                # head -> node <-> node2 <-> node3
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self._insert_after_head(cur)
            else:
                cur.prev.next = None
                self.tail = cur.prev
                self._insert_after_head(cur)
                
        return self.node_dict[key].value
    
    def put(self, key: 'int', value: 'int') -> 'None':
        if self.get(key) != -1:
            # print("key in self.node_dict")
            self.node_dict[key].value = value
        else:
            node = Node(key, value)
            self.node_dict[key] = node
            self._insert_after_head(node)
        if self._is_spill_over():
            self._pop_node(self.tail.key)
        
    def _insert_after_head(self, node: Node) -> None:
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
            
    def _is_spill_over(self) -> None:
        return len(self.node_dict) > self.cap
    
    def _pop_node(self, key) -> None:
        cur = self.tail
        self.tail = cur.prev
        cur.prev.next = None
        cur.prev = None
        self.node_dict.pop(key)
   
    def _print(self):
        cur = self.head;
        res = []
        while cur != None:
            res.append(str((cur.key, cur.value)))
            cur = cur.next
        print("->".join(res))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

