'''
Program.py

Program class to handle wimp51 'assembly' source code and convert it to binary
and/or hex output files for easy input into the Altera Cyclone II.
'''

#!/usr/bin/python -i

use Instr

class Program:

    # Program Class Constructor
    def __init__ (self, input_file, output_file):

        self.src = []
        self.comments = []
        self.instructions = []
        self.num_comments = len (self.comments)
        self.num_instructions = len (self.instructions)
        self.byte_size = None
        
        self.input_file = input_file
        self.input_fh = None

        self.output_file = output_file
        self.output_fh = None
        
        self.source_lines = None

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

    # Get program source
    def get_src (self):

        # Preliminary Line Formatting
        tmp = map (lambda x: x.rstrip(), self.input_fh)
        tmp = filter (lambda x: x != '', tmp) 

         # Split lines
        tmp = map (lambda x: x.split(' '), tmp)

        # More Formatting
        for line in tmp:
            line = map (lambda x: x.rstrip(','), line)
            self.src.append(line)

    # Instance Representative String
    def __str__ (self):
        pass

    # Rich Comparison based on program size (in bytes)
    def __lt__ (self, prog2):
        try:
            return self.byte_size < prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __le__ (self, prog2):
        try:
            return self.byte_size <= prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __eq__ (self, prog2):
        try:
            return self.byte_size == prog2.byte_size
        except (AttributeError, TypeError):
            return False
        
    def __ne__ (self, prog2):
        try:
            return self.byte_size <= prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __gt__ (self, prog2):
        try:
            return self.byte_size > prog2.byte_size
        except (AttributeError, TypeError):
            return False

    def __ge__ (self, prog2):
        try:
            return self.byte_size >= prog2.byte_size
        except (AttributeErrror, TypeError):
            return False

def main ():
    prog = Program ("input", "output")

    if prog.init_files ():
        prog.get_src ()
    
    print (prog.src)

    print Instr.INSTR_SET
