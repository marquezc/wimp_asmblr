'''
Instruction.py

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
        
        if not self.basic_syntax_check():
            return False

        if not self.cmd_specific_check():
            return False

        return True

    
    '''
    basic_syntax_check ()

    Filter out bogus commands
    Filter out instructions w/too many argument and arguments w/invalid chars
    '''
    
    def basic_syntax_check (self):

        cmd = self.cmd
        cmd_length = len(self.cmd)

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

                # Validate argument chars
                for ch in arg:
                    if ch not in Instr.VALID_CHARS:
                        return False

                # Validate register arguments (Note: Wimp51 has 8 registers [R0 - R7])            
                if arg[0] == 'R':
                    try:
                        if int("".join(arg[1:])) not in range(0,8):
                            return False
                    except ValueError:
                        return False
                    
        return True

    
    '''
    cmd_specific_check ()
    Check arguments for req'd cmd parameters
    '''
    
    def cmd_specific_check (self):

        func = self.cmd[0]
        args = self.cmd[1:]
        num_args = len(args)

        # Validate 0 argument instructions (START, END)
        if func in ['START', 'END'] and args:
            return False

        # Validate 1 argument instructions (CLR, SETB, SWAP)
        if func in ['CLR', 'SETB', 'SWAP']:

            # Only accept 1 argument
            if num_args != 1:
                return False

            # Argument must be acc
            if func == 'SWAP' and args[0] != 'A':
                return False

            # Argument must be Carry Flag
            if func in ('CLR', 'SETB') and args[0] != 'C':
                return False
                
        # Validate 2 argument instrutions (ADDC, ANL, JZ, MOV, ORL, SJMP, XRL)
        if func in ('ADDC', 'ANL', 'JZ', 'MOV', 'ORL', 'SJMP', 'XRL'):

            if num_args != 2:
                return False

            # Validate ADDC instructions
            if func == 'ADDC':

                # First argument must be Acc
                if args[0] != 'A':
                    return False

                # Disallow Acc as second argument
                if args[1] == 'A':
                    return False

            # Validate MOV instructions
            if func == 'MOV':
                
                arg1_chars = list(args[0])
                arg2_chars = list(args[1])

                # Wimp51 can only move data TO acc or register
                if arg1_chars[0] not in ('A', 'R'):
                    return False

                # Check for two char HEX values
                if arg1_chars[0] == 'A' and len(args[0]) != 1:
                    return False

                # Wimp51 can only move to register from acc
                if arg1_chars[0] == 'R' and args[1] != 'A':
                    return False

            # Validate logic instructions (ANL, ORL, XRL)
            if func in ('ANL', 'ORL', 'XRL'):

                # Arguments (A1, A2) must be (A, Rn)
                if args[0] != 'A' and list(args[1])[0] != 'R':
                    return False

        return True
    
    # Get Arguments
    def get_args (self):
        return self.args

