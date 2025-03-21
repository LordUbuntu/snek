# This could be improved
# I should rework this into a simplified Python 3 subset parser and
#   interpreter inferface.
# I'll make this a stack machine interpreter to calculate maths in
#   polish (prefix) notation. (remember shunting yard to show as infix)
# This should be built upon and given it's own repo. I will make a very
#   simple stack based programming language as a subset of some Python
#   with a couple of neat features. Name to be decided. Serpet? Egg?
#   something to indicate the snakishness and a beginning.
# I'll share this project once I've gotten it to a stable basic state
# This initial version is made based on "500 Lines or Less: A Python
#   Interpreter in Python"
#   https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html
# I think among egg, drake, serpent, and snek that I'll settle of snek
#   as the name and .snk as the file extension because the name evokes
#   tinyness/cuteness and simplicity which is the ethos of this language

class StackMachine:
    def __init__(self):
        self.stack = []

    def ADD(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a + b)

    def SUB(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a - b)

    def PUSH(self, value):
        self.stack.append(value)

    def POP(self):
        if self.stack:
            return self.stack.pop()
        return None

    def PEEK(self, depth=1):
        print("peek: {}".format(self.stack[-depth:]))

    def CLEAR(self):
        self.stack.clear()

    # NOTE:
    # - minimal basic instruction set
    # - easy metaprogramming to build upon and modify instructions
    # - written very simply
    # - probably best to start by implementing a RPN calculator
    # TODO:
    # - write a list of (mutable) instructions
    # - write a parser for the basic starting instructions
    # - write a runner (sort of done now)

    def parse(self):
        # basic version is just (...if '+', 'ADD", ..., etc)
        # how would a + b - c + d look in RPN?
        pass

    def run(self, instructions):
        for instruction in instructions:
            # fine for now
            op, *args = instruction.split()
            method = getattr(self, op)
            if args:
                method(*[int(arg) for arg in args])
            else:
                method()





# potential instruction set
# + - * / // %
sm = StackMachine()
#  sm.PUSH(6)
#  sm.PUSH(7)
#  sm.PUSH('+')
#  while sm.stack:
#      sm.DEBUG()
#      input()
#      symbol = sm.POP()
#      if symbol == '+':
#          sm.ADD()
#      else:
#          print(symbol)
#  sm.DEBUG()
