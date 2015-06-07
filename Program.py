'''
Program.py

Program class to handle wimp51 'assembly' source code and convert it to binary
and/or hex output files for easy input into the Altera Cyclone II.
'''

#!/usr/bin/python3 -i

from Instruction import Instr

class Program (object):

    # Don't create the Program object if input file doesn't exist
    def __new__(cls, *args, **kwargs):

        fail = 0

        try:
            input_fh = open (args[0], 'r')
        except IOError as e:
            fail = 1
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 args[0],
                                                                 e.strerror)

        try:
            output_fh = open (args[1], 'w')
        except IOError as e:
            fail = 1
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 args[1],
                                                                 e.strerror)

        if not fail:
            return object.__new__(cls, (input_fh, output_fh), **kwargs)

    # Program Class Constructor
    def __init__ (self, input_fh, output_fh):

        self.src = []
        self.instructions = []
        self.err = []
        
        # IO Filehandlers
        self.input_fh = input_fh
        self.output_fh = output_fh

        # Program Stats
        self.num_src_lines = None
        self.num_instructions = None
        self.byte_size = None

        self.init_src()
        self.init_instructions()

    # Instance Representative String
    def __str__ (self):
        return "Assemble: Program"
        
    # Preliminary Line Formatting
    def init_src (self):
        self.src = map(lambda x: x.rstrip(), self.input_fh)
        self.src = filter(lambda x: x != '', self.src)

    def init_instructions (self):
        self.instructions = [Instr(line) for line in self.src]
        self.instructions = filter (lambda i: i.valid_instr(), self.instructions)
        
    # Get program source
    def get_src (self):
        return self.src

    # Populate Program.instructions
    def get_instructions (self):
        return self.instructions


    # Rich Comparison based on program size (in bytes) [... .etc]
    def __lt__ (self, prog2):

        try:
            return self.byte_size < prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __eq__ (self, prog2):

        try:
            return self.byte_size == prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __gt__ (self, prog2):

        try:
            return self.byte_size > prog2.byte_size
        except (AttributeError, TypeError):
            return False

def main ():

    prog = Program ("inpu", "output")

    if prog:
        print (prog)
