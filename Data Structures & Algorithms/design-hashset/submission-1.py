class MyHashSet:

    def __init__(self):
        self.set_obj = []

    def add(self, key: int) -> None:
        if key not in self.set_obj:
            self.set_obj.append(key)

    def remove(self, key: int) -> None:
        for i, n in enumerate(self.set_obj):
            if n == key:
                del self.set_obj[i]
                break

    def contains(self, key: int) -> bool:
        for n in self.set_obj:
            if n == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)