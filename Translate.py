'''
Translate.py

Translate wimp51 'assembly' instructions to binary instructions
'''

#!/usr/bin/python -i

class Translate:

    # "Static" instruction bytes don't change
    STATIC_INSTR = {
        'ADDC'   : '00110100',
        'CLR'    : '11000011',
        'JZ'     : '01100000',
        'MOV'    : '01110100',
        'SETB'   : '11010011',
        'SJMP'   : '10000000',
        'SWAP'   : '11000100'
    }

    # Register instructions are suffixed with appropriate 3bit segments specific
    # to the argument.  Underscore followed by a letter represents the second
    # argument to the instruction
    REG_INSTR = {
        'ADDC'   : '00111',
        'ANL'    : '01011',
        'MOV_A'  : '11111',
        'MOV_R'  : '11101',
        'ORL'    : '01001',
        'XRL'    : '01101'
    }


    # Initialize instance of Translate
    def __init__ (self):
        pass

    def __str__ (self):
        return "Translation Object - Wimp51 Assembly to Binary"

    def reg_decode (self, i):

        func = i[0]
        arg1 = i[1]
        arg2 = i[2]

        if func == 'MOV':

            if arg2 == 'A':
                prefix = Translate.REG_INSTR['MOV_A']
                reg = list(arg1)[1]
            else:
                Translate.REG_INSTR['MOV_R']
                reg = list(arg2)[1]

        else:
            prefix = Translate.REG_INSTR[i[0]]
            reg = list(arg2)[1]

        return prefix + reg




















        

        

            
