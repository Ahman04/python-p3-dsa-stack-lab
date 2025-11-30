class Stack:

    def __init__(self, items = None, limit = 100):
        self.items = items[:] if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        # If full, DO NOT push the new_item (test requires this).
        if len(self.items) >= self.limit:
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        
        top_index = len(self.items) - 1
        target_index = self.items.index(target)

        return top_index - target_index
