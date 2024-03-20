class TodoList:
    def __init__(self, tasks_list):
        self.tasks = tasks_list

    def __repr__(self):
        return f"{self.__class__.__name__}(list[str])"

    def __str__(self):
        # result = ''
        # for item in self.tasks:
        #     result += f"{item}\n"
        # return result
        return '\n'.join(self.tasks)


tasks = ['task1', 'task2']
list1 = TodoList(tasks)
print(repr(list1))  # TodoList(list[str])

print(list1)  # task1, task2
