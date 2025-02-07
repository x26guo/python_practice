from functools import lru_cache

from leetcode.DoubleSidedListNode import DoubleSidedListNode

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.head = DoubleSidedListNode()
        self.tail = DoubleSidedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.store:
            self.move_to_front(self.store[key], True)
            return self.store[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].val = value
            self.move_to_front(self.store[key], True)
        else:
            if len(self.store) == self.capacity:
                removed = self.tail.prev
                removed.prev.next = self.tail
                self.tail.prev = removed.prev
                del self.store[removed.key]

            cur = DoubleSidedListNode(key, value)
            self.move_to_front(cur, False)
            self.store[key] = cur


    def move_to_front(self, node: DoubleSidedListNode, existing: bool):
        if existing:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

cache = LRUCache(2)
cache.get(2)
cache.put(2,6)
cache.get(1)
cache.put(1,5)
cache.put(1,2)
cache.get(1)
cache.get(2)
