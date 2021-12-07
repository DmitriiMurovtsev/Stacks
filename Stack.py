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
    stacks = Stack(brackets)
    # (
    stack_1 = Stack()
    # [
    stack_2 = Stack()
    # {
    stack_3 = Stack()
    if stacks.size() % 2 == 1:
        return 'Несбалансированно'
    if stacks.isEmpty():
        return 'Пустой стек'
    while stacks.isEmpty() == False:
        el = stacks.pop()
        if el == '(':
            stack_1.push(el)
        elif el == '[':
            stack_2.push(el)
        elif el == '{':
            stack_3.push(el)
        elif el == ')':
            if stack_1.isEmpty():
                return 'Несбалансированно'
            else:
                stack_1.pop()
        elif el == ']':
            if stack_2.isEmpty():
                return 'Несбалансированно'
            else:
                stack_2.pop()
        elif el == '}':
            if stack_3.isEmpty():
                return 'Несбалансированно'
            else:
                stack_3.pop()
    if stack_1.isEmpty() and stack_2.isEmpty() and stack_3.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


# brackets = input('Введите строку со скобками: ')
brackets = input('Введите строку со скобками: ')
print(get_pairs(brackets))
