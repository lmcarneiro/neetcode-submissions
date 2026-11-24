import random

class RandomizedSet:

    def __init__(self):
        self.val_map = {}
        self.val_list = []

    def insert(self, val: int) -> bool:
        if val not in self.val_map:
            self.val_list.append(val)
            self.val_map[val] = len(self.val_list) - 1
            # self.val_list.append(val)
            return True
            
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_map:
            idx = self.val_map[val]
            last = self.val_list[-1]
            self.val_list[idx] = last
            self.val_map[last] = idx
            self.val_list.pop()
            del self.val_map[val]
            return True

        return False

    def getRandom(self) -> int:
        n = random.randint(0, len(self.val_list) - 1)
        return self.val_list[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()