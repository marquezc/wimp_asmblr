'''
instr.py

Instr class to handle wimp51 instruction validation and associated tasks
'''

#!/usr/bin/python -i

class Instr:

    INSTR_SET = ('ADDC', 'ANL', 'CLR', 'END',
                 'JZ',  'MOV','ORL', 'SETB',
                 'SJMP', 'START', 'SWAP', 'XRL')

    VALID_CHARS = ('A', 'B', 'C', 'D', 'E', 'F', 'R',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    def __init__ (self, cmd):
        
        self.cmd = self.format_instr(cmd)

        self.args = self.cmd[1:]
        self.num_args = len(self.args)
        
    def __str__ (self):
        return "Instr Object: " + " ".join(self.cmd)

    # Format instruction line and return list
    def format_instr (self, cmd):
        return map (lambda x: x.strip(","), cmd.split(" "))

    '''
    Validate Instruction
    (This should all be done with regexes eventually...)

    '''
    def valid_instr (self):
        
        cmd = self.cmd
        cmd_length = len(self.cmd)


        '''
        Start Basic Syntax Checking
        '''
        
        if (cmd_length == 1 and cmd[0] not in ["START", "END"]):
            return False

        # Return False if not 1 or 2 arguments
        if (cmd_length < 1 or cmd_length > 3):
            return False

        # Return False if Function not in WIMP51 instruction set
        if (cmd_length != 1 and cmd[0] not in Instr.INSTR_SET):
            return False

        # Validate function arguments
        if (cmd_length > 1):

            for arg in cmd[1:]:
                arg = list(arg)

                # Return False if wrong argument size
                if len(arg) < 1 or len(arg) > 2:
                    return False

                # Validate one char arguments
                if len(arg) == 1 and arg[0] != 'A':
                    return False

                # Validate argument chars
                if len(arg) == 2:
                    for c in arg:
                        if c not in Instr.VALID_CHARS:
                            return False
                
                # Validate register arguments (Note: Wimp51 has 8 registers [R0 - R7])            
                if arg[0] == 'R':
                    try:
                        if int("".join(arg[1:])) not in range(0,8):
                            return False
                    except ValueError:
                        return False
        '''
        End Basic Syntax Checking
        '''

        '''
        Start Command-Specific Checking
        '''



        '''
        End Command-Specific Checking
        '''
        
        return True
    
    # Get Arguments
    def get_args (self):
        return self.args
        
def main ():

    prog = [Instr('START'),
            Instr('MOV A, 00'),
            Instr('ADDC, A, 02'),
            Instr('MOV, R4, A'),
            Instr('MOV, A, 08'),
            Instr('ADDC A, R4'),
            Instr('ADDC A0, X'),
            Instr('ADDC A, R'),
            Instr('ADDC A, R-'),
            Instr('ADDC A, R9'),
            Instr('ADDC A, R8'),
            Instr('ADDC A, R10'),
            Instr('END')]

    prog = filter(lambda i: i.valid_instr(), prog)
    
    for i in prog:
        print (i)
