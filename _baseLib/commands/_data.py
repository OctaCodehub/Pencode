class Data:
    def __init__(self):
        self.codeRunEnabled = True
        self.funcs = []
        self.blocks = {}
        self.data = {}
        self.servers = {}
    def setCRE(self, set):
        '''set codeRunEnabled to {set}
        true - run code
        false - stop code
        '''
        self.codeRunEnabled = set
    def addFunc(self, func):
        self.funcs.append(func)
    def addBlock(self, id, block):
        self.blocks[id] = block
    def addData(self, id, dat):
        self.data[id] = dat
    def joinMultiple(self, strAr):
      s = ""
      for st in strAr:
        s = s + st
      return s

data = Data()

#this is where data for the language is stored and handled