from _baseLib.commands._commands import _cmds
from _baseLib.commands._data import *

pen = open('code.pen')
penroot = 'none'
error = ''
blk = ""

for line in pen.readlines():
    line = line.strip()
    commands = line.rsplit(" ")
    command = commands[0]
    command = command.replace(" ", "")
    args = commands[1:]
    strings = []
    bools = []
    for arg in args:
      if (arg.startswith("%") and arg.endswith("%")):
        n = arg.replace("%", "")
        args[args.index(arg)] = data.data[n][0]
      if (arg.startswith("\"")):
        args[args.index(arg)] = args[args.index(arg)].replace("\"", "", -1)
        strings.append(arg)
      if (arg.lower() == "true") or (arg.lower() == "false"):
        bools.append(bool(arg))

    if (data.codeRunEnabled):
      if (command.lower() == 'penout'):
          _cmds['penout'](args)
      elif (command.lower() == 'penin'):
          _cmds['penin'](args)
      elif (command.lower() == 'penroot'):
          penroot = _cmds['penroot'](args)
          if not (penroot[1]):
              penroot = penroot[0]
          else:
              error = penroot[1]
              break
      elif (command.lower() == 'efunc'):
          _cmds['efunc'](args)
      elif (command.lower() == 'set'):
          _cmds['set'](args)
      elif (command.lower() == 'nline'):
          _cmds['nline']()
      elif (command.lower() == 'ecall'):
          _cmds['ecall'](args)

      if (penroot == 'pen'):
        if (command.lower() == 'call'):
          _cmds['ecall'](args)
        elif (command.lower() == 'nline'):
          _cmds['nline']()
        elif (command.lower() == 'set'):
          _cmds['set'](args)
        elif (command.lower() == 'out'):
          _cmds['out'](args)
        elif (command.lower() == 'in'):
          _cmds['in'](args)
        elif (command.lower() == 'root'):
          penroot = _cmds['penroot'](args)
          if not (penroot[1]):
            penroot = penroot[0]
          else:
            break
        elif (command.lower() == 'func'):
          _cmds['efunc'](args)

    else:
      if (command.lower() == 'func'):
        _cmds['efunc'](args)
        if (args[2].lower() == 'true'):
          data.addBlock(args[0], blk)
      elif (command.lower() == 'pfunc'):
        _cmds['efunc'](args)
      else:
        blk = blk + "\n" + line

if (error):
  print("Program Has Died.")

#this is the parser file
#here the file is read