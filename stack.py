from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
        
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0

def rev(data):
    """Reverses a string"""
    s = Stack()
    reversed_string = ''
    for char in data:
        s.push(char)
    while s.size() > 0:
        reversed_string += s.pop()
    return reversed_string

def is_matched(ch1,ch2):
    match_table = {
    ')':'(',
    ']':'[',
    '}':'{'
    }
    return match_table[ch1] == ch2
    

def is_balanced(data):
    s = Stack()
    for char in data:
        if char == '(' or char == '[' or char == '{':
            s.push(char)
        if char == ')' or char == ']' or char == '}':
            if s.is_empty():
                return False
            if not is_matched(char,s.pop()):
                return False
    return s.is_empty()

    

        

if __name__ == '__main__':
   
    code = "[bracketbalanced(test{is it working?})]"
    invalid = "][testing)("

    print("Should be True:")
    print(is_balanced(code))

    print("Should be False")
    print(is_balanced(invalid))


    # stack = deque()
    
    # stack.append('https://www.cnn.com/')
    # stack.append('https://www.cnn.com/world')
    # stack.append('https://www.cnn.com/india')
    # stack.append('https://www.cnn.com/china')

    # # view and then pop the final entry in stack
    # print(stack[-1])
    # print(stack.pop())
    # print(type('hey'))
    # print(stack)

    # print(rev('checking for reversal'))