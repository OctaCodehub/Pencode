from .penout import *
from .penin import *
from .penroot import *
from .pfunc import *
from ._data import *
from .nline import *
from .set import * 

def pcall(args):
  if (args[0] in data.funcs):
    blk = data.blocks[args[0]]
    blklines = blk.split('\n')
    for line in blklines:
      line = line.strip()
      commands = line.rsplit(" ")
      command = commands[0]
      command = command.replace(" ", "")
      args = commands[1:]

      for arg in args:
        if (arg.startswith("%") and arg.endswith("%")):
          n = arg.replace("%", "")
          args[args.index(arg)] = data.data[n][0]

      if (command.lower() == 'penout'):
          _cmds['penout'](args)
      elif (command.lower() == 'penin'):
          _cmds['penin'](args)
      elif (command.lower() == 'efunc'):
          _cmds['efunc'](args)
      elif (command.lower() == 'nline'):
          _cmds['nline']()
      elif (command.lower() == 'ecall'):
          _cmds['ecall'](args)

_cmds = {
  'penout': penout,
  'out': penout,
  'penin': penin,
  'in': penin,
  'penroot': penroot,
  'root': penroot,
  'efunc': pfunc,
  'func': pfunc,
  'nline': nline,
  'ecall': pcall,
  'set': pset,
}

#this is where all the commands and data is exported