from ..errors.args import *
from ._data import *

def pfunc(args):
    if len(args) != 3:
        error = ArgumentIndexError(args)
        error.call()
    else:
        if (args[2].lower() == "false"):
            data.setCRE(False)
            data.addFunc(args[0])
        elif (args[2].lower() == "true"):
            if (args[0] in data.funcs):
                data.setCRE(True)       

#this is where the func is created
#func = function