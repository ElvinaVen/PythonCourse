import time


class MyOpen:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.filename, self.mode)
        self.start_time = time.time()
        print("Файл успешно открыт")
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.time() - self.start_time
        print(f'Файл был открыт {self.elapsed_time} секунд и теперь успешно закрыт.')


with MyOpen('countries.txt', 'r') as fp:
    content = fp.read()
    print('Чтение данных 2 секунды...')
    time.sleep(2)

print('Продолжение кода...')
