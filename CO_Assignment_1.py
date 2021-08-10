def bin(value, noOfDigits = 32 ):      # returns the binary value of the number

    i = 1 << noOfDigits - 1            # Also takes the no of digitd to be displayed for representation
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


#x = str(input())
#lst = x.split(' ')

#if lst[0] == 'add':
    #r1 += r0
#elif lst[1] == 'sub':
    #1 = r2 - r3

#for i in functionOpcode.keys():
    #print(bin(int(i), 5))

#print(bin(int(registerValue('r3')), 3))

#a = True
lst= []
#try:
#    while a:
#        y = str(input())
#        lst.append(y)
#except ValueError:
#    print("11001")


#for i in lst:
#    print(i)

while True:
    line = input()
    if(line == "hlt"):
        break
    elif(line == ""):
        continue
    else:
        lst = line.split(" ")
        if lst[0] == 'mov' and  lst[2][0] == 'r':
            p = 'moveregister'

        print(registerValue(lst[1]) + registerValue(lst[2]))



