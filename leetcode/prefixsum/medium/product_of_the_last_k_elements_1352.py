class ProductOfNumbers:

    def __init__(self):
        self.prefix = []
        self.last_zero_index = -1
        self.length = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix.append(num)
            self.last_zero_index = self.length
        elif len(self.prefix) == 0:
            self.prefix.append(num)
        else:
            pre = self.prefix[len(self.prefix) - 1]
            if pre == 0:
                self.prefix.append(num)
            else:
                self.prefix.append(pre * num)
        self.length += 1


    def getProduct(self, k: int) -> int:
        first_index = self.length - k - 1
        if self.last_zero_index > first_index:
            return 0
        if first_index < 0:
            return self.prefix[self.length - 1]
        first = self.prefix[first_index]
        if first == 0:
            return self.prefix[self.length - 1]

        last = self.prefix[self.length - 1]
        return last // first

product = ProductOfNumbers()
product.add(0)
product.add(5)
product.add(6)
product.add(8)
product.getProduct(3)
product.getProduct(4)