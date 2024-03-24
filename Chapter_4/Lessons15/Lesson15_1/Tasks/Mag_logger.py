class MyList(list):
    
    def __init__(self, *args, **kwargs):
        print("Работает магический метод")
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        print("Работает магический метод")
        return super().__add__(other)

    def __str__(self):
        print("Работает магический метод")
        return super().__str__()

    def __len__(self):
        print("Работает магический метод")
        return super().__len__()


lst = MyList(['Jone', 'Snow', 'Java'])
lst_2 = ["C++", "C#"]
lst + lst_2
lst_3 = lst + lst_2

print(lst_3)
print(lst)
print(len(lst))
