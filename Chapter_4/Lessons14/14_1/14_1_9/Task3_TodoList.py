class TodoList:
    def __init__(self, tasks_list):
        self.tasks = tasks_list

    def __repr__(self):
        return f"{self.__class__.__name__}(list[str])"

    def __str__(self):
        return '\n'.join(self.tasks)

    def __add__(self, other):
        # return self.tasks + other.tasks
        result_list = [*self.tasks, *other.tasks]
        return TodoList(result_list)

    def __len__(self):
        return len(self.tasks)

list1 = TodoList(['task1', 'task2'])
list2 = TodoList(['task3', 'task4'])
list3 = list1 + list2
print(list3)  # task1, task2, task3, task4
print(len(list3))
