class Stack:
    def __init__(self, stack_str=""):
        self.stacks = stack_str

    def isEmpty(self):
        # проверка стека на пустоту. Метод возвращает True или False
        if len(self.stacks) == 0:
            return True
        else:
            return False

    def push(self, new):
        # добавляет новый элемент на вершину стека. Метод ничего не возвращает
        self.stacks = str(new) + self.stacks

    def pop(self):
        # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        element = self.stacks[0]
        self.stacks = self.stacks[1:]
        return element

    def peek(self):
        # возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        return self.stacks[0]

    def size(self):
        # возвращает количество элементов в стеке
        return len(self.stacks)


def get_pairs(brackets):
    stacks = Stack()
    my_dict = {')': '(', '}': '{', ']': '['}
    for el in brackets:
        if el in '({[':
            stacks.push(el)
        elif el in ')}]':
            if stacks.isEmpty():
                return 'Несбалансированно'
            if my_dict[el] == stacks.peek():
                stacks.pop()
            else:
                return 'Несбалансированно'
    if stacks.size() == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


brackets = input('Введите строку со скобками: ')
print(get_pairs(brackets))
