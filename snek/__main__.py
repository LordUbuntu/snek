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
#
# goal is a simple metaprogrammable (concatenative?) stack based language
#   that implements a small set of composable operations that can
#   be built upon. May implement a type system if it's not too much
#   effort an provides benefits over typeless. This isn't meant to be
#   a massive programming language or anything, simplicity is the goal
# design decisions:
# - binary operators?
#
# Would deal and hypothesis be overkill? Should I make this a full project? Should I use tox?

class StackMachine:
    def __init__(self):
        self.stack = []

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

    def ADD(self):
        a = self.POP()
        b = self.POP()
        self.PUSH(a + b)

    def SUB(self):
        a = self.POP()
        b = self.POP()
        self.PUSH(a - b)

    def parse(self):
        # need to setup basic keywords like what Haskell does,
        #   keywords maybe as a dict and a way to add keywords
        #   (but not remove or change base ones)
        # basic version is just (...if '+', 'ADD", ..., etc)
        # how would a + b - c + d look in RPN?
        pass

    def run(self, instructions):
        # assuming stack is already full of literals and symbols like
        #   ADD 2 3 SUB 4
        for instruction in instructions:
            if type(instruction) == int:
                continue
            else:
                method = getattr(self, instruction)
                method()





# potential instruction set
# + - * / // %
sm = StackMachine()
sm.PEEK(10)
sm.PUSH(1)
sm.PUSH("ADD")
sm.PUSH(2)
sm.PUSH(3)
sm.PUSH("ADD")
sm.PEEK(10)
sm.run(reversed(sm.stack))
