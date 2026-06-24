class Node:
    def __init__(self, key = 0, next = None):
        self.key = key
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.cur = None
        self.limit = 0

    def get(self, key: int) -> int:
        
        if key in self.cache:   
            self.cur.next = Node(key)
            self.cur = self.cur.next

            # check head is the key
            if self.head.key == key:
                self.head = self.head.next

            else:
                temp = self.head

                while temp.next and temp.next != self.cur:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                
            # Final
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            
            if self.limit == self.capacity:
                del self.cache[self.head.key]
                self.limit -= 1
                self.head = self.head.next

            self.cache[key] = value

            if self.head is None:
                self.head = Node(key)
                self.cur = self.head

            else:
                self.cur.next = Node(key)
                self.cur = self.cur.next
            self.limit += 1

        else:
            self.cache[key] = value
            self.cur.next = Node(key)
            self.cur = self.cur.next
            self.limit += 1

            if self.head.key == key:
                self.head = self.head.next
                self.limit -= 1

            else:
                temp = self.head

                while temp.next and temp.next != self.cur:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        self.limit -= 1
                        break
                    temp = temp.next

                
