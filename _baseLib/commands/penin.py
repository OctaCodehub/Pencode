from ._data import data

def penin(args):
    s = ''
    argn = args[1:]
    for arg in argn:
        s += arg + " "
    sin = input(s)

    data.data[args[0]][0] = sin

#input command