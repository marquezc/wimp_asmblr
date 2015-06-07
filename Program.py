'''
Program.py

Program class to handle wimp51 'assembly' source code and convert it to binary
and/or hex output files for easy input into the Altera Cyclone II.
'''

#!/usr/bin/python -i

from Instruction import Instr

class Program:

    # Program Class Constructor
    def __init__ (self, input_file, output_file):

        self.src = []
        self.instructions = []
        self.num_instructions = len (self.instructions)
        self.byte_size = None
        
        self.input_file = input_file
        self.input_fh = None

        self.output_file = output_file
        self.output_fh = None
        
        self.source_lines = None

    # Open Input and Output files
    def init_files (self):
        fail = 0
        
        try:
            self.input_fh = open (self.input_file, 'r')
        except IOError as e:
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 self.input_file,
                                                                 e.strerror)
            fail = 1

        try:
            self.output_fh = open (self.output_file, 'w')
        except IOError as e:
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 self.output_file,
                                                                 e.strerror)
            fail = 1

        return 1 if not fail else 0

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

    # Instance Representative String
    def __str__ (self):
        return "Assemble: " + self.input_file + " " + self.output_file


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
    prog = Program ("input", "output")

    if not prog.init_files ():
        return 0

    prog.init_src()
    prog.init_instructions()

    for i in prog.instructions:
        print (i)

    print (prog)

