from ..errors.root import *
roots = ['pen', 'none']

def penroot(args):
    global error
    error = False
    if not (args[0] in roots):
        error = RootIndetifierInvalid(args[0])
        error.call()
        error = True
    else:
        penroot = args[0]
    return [penroot, error]

#creates a root where commands are gotten from
#most comamnds are gotten from the _baseLib root
#but the pen root is also there