#1th approach:
# Time:
# Space:
#2th approach:
# Time:
# Space:

#Hashset bouwen met arrays. Alleen letten op Key. Niet op Value want het is geen Hashmap
#Mod
# Hash Collision, Open adressing etc.

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)] #List comprehension. 10^4=9999

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

# Voorbeeldgebruik
hash_set = MyHashSet()
hash_set.add(1)
hash_set.add(2)
print(hash_set.contains(1))  # True
print(hash_set.contains(3))  # False
hash_set.add(2)
print(hash_set.contains(2))  # True
hash_set.remove(2)
print(hash_set.contains(2))  # False