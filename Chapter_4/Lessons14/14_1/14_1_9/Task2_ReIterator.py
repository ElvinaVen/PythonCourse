class ReIterator:
    def __init__(self, list_num):
        self.list_num = list_num

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self.list_num):
            self.current_value += 1
            return self.list_num[len(self.list_num) - self.current_value - 1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.list_num)


list_num = [1, 2, 3, 4, 5, 7]
x = ReIterator(list_num)
print(len(x))
