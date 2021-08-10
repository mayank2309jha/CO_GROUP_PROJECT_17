def bin(value, noOfDigits = 32 ):      # returns the binary value of the number

    i = 1 << noOfDigits - 1            # Also takes the no of digit to be displayed for representation and default is 32
    x = ""
    while (i > 0):
        if ((value & i) != 0):
            x += "1"
        else:
            x += "0"
        i = i // 2
    return x

def registerValue(a):
    if a.lower() == 'r0':
        a = '000'
    elif a.lower() == 'r1':
        a = '001'
    elif a.lower() == 'r2':
        a = '010'
    elif a.lower() == 'r3':
        a = '011'
    elif a.lower() == 'r4':
        a = '100'
    elif a.lower() == 'r5':
        a = '101'
    elif a.lower() =='r6':
        a = '110'
    elif a.lower() == 'flags':
        a = '111'

    return a

functionOpcode = {'0': 'addition' ,
                  '1': 'subtraction',
                  '2': 'moveimmediate',
                  '3': 'moveregister',
                  '4': 'load',
                  '5': 'store',
                  '6': 'multiply',
                  '7': 'divide',
                  '8': 'rightshift',
                  '9': 'leftshift',
                  '10': 'exclusiveor',
                  '11': 'or',
                  '12': 'and',
                  '13': 'invert',
                  '14': 'compare',
                  '15': 'unconcditionaljump',
                  '16': 'jumpiflessthan',
                  '17': 'jumpifgreaterthan',
                  '18': 'jumpifequal',
                  '19': 'halt'}



def ADDITION():
    pass

def SUBTRACTION():
    pass

def MOVEIMMEDIATE():
    pass

def MOVEREGISTER():
    pass

def LOAD():
    pass

def STORE():
    pass

def MULTIPLY():
    pass

def DIVIDE():
    pass

def RIGHTSHIFT():
    pass

def LEFTSHIFT():
    pass

def EXCLUSIVEOR():
    pass

def OR():
    pass

def AND():
    pass

def INVERT():
    pass

def COMPARE():
    pass

def UNCONDITIONALJUMP():
    pass

def JUMPIFLESSTHAN():
    pass

def JUMPIFGREATERTHAN():
    pass

def JUMPIFEQUAL():
    pass

def HALT(s):
    return bin(int(return_key(s)), 5) + "00000000000"


def return_key(val):
    for key, value in functionOpcode.items():
        if value == val:
            return key
    return -1

lst = [[]]
x: str
ans = []

while True:
    line = input()
    if(line == "hlt"):
        print(HALT('halt'))
        break
    elif(line == ""):

        continue
    else:
        lst = line.split(" ")
        if lst[0] == 'var':
            x = lst[1]
        if lst[0] == 'st' and lst[2] == x:
            x = lst[1]
        if lst[0] == 'mov':
            if lst[2][0] == 'r':
                p = 'moveregister'
                p = return_key(p)
                ans.append(bin(int(p), 5) + "00000" + registerValue(lst[1]) + registerValue(lst[2]))
            else:
                p = 'moveimmediate'
                if(lst[2][0] == '$'):
                    lst[2].removeprefix('$')

                p = return_key(p)
                ans.append(bin(int(p), 5) + registerValue(lst[1]) + bin(int(lst[2]), 8))



for i in ans:
    print(i)

