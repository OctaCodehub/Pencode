class ArgumentIndexError:
    def __init__(self, args):
        self.argn = len(args)

    def call(self):
        print("ArgumentIndexError: " + str(self.argn) + " is Too Many Arguments.")

class InvalidArgumentError:
    def __init__(self, arg):
        self.arg = arg

    def call(self):
        print("InvalidArgumentError: " + str(self.arg) + " is not valid.")

#two other errors for func command