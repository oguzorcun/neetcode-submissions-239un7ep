





class Node:
    def __init__(self, key: int, val: int, prev = None, nxt= None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.cache.nxt = self.tail
        self.tail.prev = self.cache
        self.nodes = {}

    def move_to_head(self, node: Node):
        # remove the node
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        self.insert_head(node)
    
    def insert_head(self, node: Node):
        old_head = self.cache.nxt
        self.cache.nxt = node
        node.nxt = old_head
        node.prev = self.cache
        old_head.prev = node

    def get(self, key: int) -> int:
        node = self.nodes.get(key, None)

        if not node: return -1
        if node == self.cache.nxt: return node.val

        self.move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key, None)
        if node:
            node.val = value
            self.move_to_head(node)
            return
        if len(self.nodes) == self.cap:
            tail = self.tail.prev
            del self.nodes[tail.key]
            tail.prev.nxt = self.tail
            self.tail.prev = tail.prev
        
        new_node = Node(key, value)
        self.insert_head(new_node)
        self.nodes[key] = new_node


    


















