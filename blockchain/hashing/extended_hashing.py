#extended_hashing

class Hashtable:
    def __init__(self):
        self.table = [None for _ in range(139)]
       
    def simple_hash(self, name):
        ord_sum=0
        for letter in name:
            ord_sum += ord(letter)
        return ord_sum % len(self.table)
        # return sum(map(ord, name)) % len(len.table)

    def put(self, name, num):
        self.table[self.better_hash(name)] = num

    def show(self):
        for idx, value in enumerate(self.table):
            if value:  # is not None
                print(idx, value)

    def find(self, name):
        return self.table[self.better_hash(name)]

    def better_hash(self, name):
        honer = 37
        ord_sum = 0
        for letter in name:
            ord_sum += ord_sum * honer + ord(letter)
        return ord_sum % len(self.table)

