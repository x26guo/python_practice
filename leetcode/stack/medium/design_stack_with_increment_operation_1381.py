class CustomStack:
    def __init__(self, maxSize: int):
        self.list = []
        self.max_length = maxSize

    def push(self, x: int) -> None:
        if len(self.list) < self.max_length:
            self.list.append(x)

    def pop(self) -> int:
        if not self.list:
            return -1
        result = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return result

    def increment(self, k: int, val: int) -> None:
        new_k = min(k, len(self.list))
        for i in range(new_k):
            self.list[i] = self.list[i] + val