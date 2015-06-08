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
        
        # I assume there's a better way of accomplishing this check without the
        # redundant open/close of files... It's on the todo list.
        # Note: Originally used os.path.isfile(filename) but that doesn't check read 
        # permissions for existing files and won't be useful for checking user's ability to 
        # create new files.
        try:
            # Open Filehandlers for Error-checking
            # (i.e. don't create object unless correct file permissions)
            i_fh = open (args[0], 'r')
            o_fh = open (args[1], 'w')
        except IOError as e:
            fail = 1
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 args[0],
                                                                 e.strerror)

        if not fail:
            # Close Error-check Filehandlers
            # Tried to pass the open handlers to __init__, but wasn't able to modify *args[]...
            i_fh.close()
            o_fh.close()

            # Create Instance
            return object.__new__(cls, *args, **kwargs)

    # Program Class Constructor
    def __init__ (self, input_file, output_file):

        # IO Filenames
        self.input_file = input_file
        self.output_file = output_file
        
        # IO Filehandlers
        self.input_fh = None
        self.output_fh = None

        # Program Handlers
        self.src = []
        self.instructions = []
        self.err = []

        # Initialize Program Handlers
        self.init_files()
        self.init_src()
        self.init_instructions()

        # Program Stats
        self.num_src_lines = None
        self.num_instructions = None
        self.byte_size = self.get_byte_size()
        
        ####
        # Close Input Filehandler after initializing the instance of Program
        ####
        
    # Instance Representative String
    def __str__ (self):
        return "Assemble: Program"

    # Initialize Files
    def init_files (self):

        try:
            self.input_fh = open (self.input_file, 'r')
        except IOError as e:
            fail = 1
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 self.input_file,
                                                                 e.strerror)

        try:
            self.output_fh = open (self.output_file, 'w')
        except IOError as e:
            fail = 1
            print ("Error ({0}). Couln't Open {1}...{2}").format(e.errno,
                                                                 self.output_file,
                                                                 e.strerror)

    # Preliminary Line Formatting
    def init_src (self):
        self.src = map(lambda x: x.rstrip(), self.input_fh)
        self.src = filter(lambda x: x != '', self.src)

    def init_instructions (self):
        self.instructions = [Instr(line) for line in self.src]
        self.instructions = filter (lambda i: i.valid, self.instructions)
        
    # Get program source
    def get_src (self):
        return self.src

    # Populate Program.instructions
    def get_instructions (self):
        return self.instructions

    # Get Program byte_size
    def get_byte_size (self):

        byte_cnt = 0
        for i in self.instructions:
            byte_cnt += i.byte_size

        return byte_cnt

    # Rich Comparison based on program size (in bytes) [... .etc]
    # Note: There are better methods of accomplishing this.  These are placeholder
    # functions for now; consider it an exercise in exception handling
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


# Temporary Test Function
def main ():

    prog = Program ("input", "output")

    if prog:
        for i in prog.instructions:
            print ("Valid: {0}; Byte Size: {1}").format(i.args, i.byte_size)

        print ("Program Size: " + str(prog.byte_size))
        
