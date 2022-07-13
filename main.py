k = {'(': ')',
     '[': ']',
     '{': '}'}
# Варианты скобочных последовательностей
t_list = ['[([])((([[[]]])))]{()}', '(((([{}]))))', '(((([{}]))])', '{{[()]}}', '}{}',
          '{{[(])]}}', '[[{())}]', '{{{{{}', '((((((()))', '({}([{}]{}))', '()[]{}']


class Stack:
    def __init__(self):
        self.stack = []

    @property
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        deleted = self.stack.pop()
        return deleted

    def peek(self):
        top_element = self.stack[-1]
        return top_element

    def size(self):
        if self.isEmpty:
            return None
        stack_len = len(self.stack)
        return stack_len


def get_balanced(t: str):
    is_balanced = True
    s.stack = []
    for smbl in t:
        if smbl in k:
            s.push(smbl)
        else:
            if not s.isEmpty:
                if smbl == k[s.peek()]:
                    s.pop()
                else:
                    is_balanced = False
                    break
            else:
                is_balanced = False
                break
    if not s.isEmpty:
        is_balanced = False
    return is_balanced


if __name__ == '__main__':
    s = Stack()
    for tl in t_list:
        if get_balanced(tl):
            print('Balanced')
        else:
            print('Not balanced')
