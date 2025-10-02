# %%
class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.storage.get(key) == None:
            return -1
        else:
            result = self.storage.pop(key)
            self.storage[key] = result
            return result

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage.pop(key)
        else:
            if len(self.storage) == self.capacity:
                remove_key = list(self.storage.keys())[0]
                self.storage.pop(remove_key)
        self.storage[key] = value
