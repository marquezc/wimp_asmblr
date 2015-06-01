#!/usr/bin/python3 -i

import sys

class Program:

    '''
    Note:
      errno:   system defined error number.  Check man errno for a 
               complete list of error numbers
      strerr:  is the error message string defined or a given errno.  
               Check man strerror for more info
    '''

    def __init__ (self, source_filename, out_filename="wimp.bin"):
        self.source_filename = source_filename
        self.out_filename = out_filename
        try:
            self.source_f = open(source_filename, 'r') # Input file handler
            self.out_f    = open(out_filename, 'w')    # Output file handler

        except IOError as e:
            print ("Error ({0}): '{1}': {2}".format(e.errno, \
                                                    self.source_filename, \
                                                    e.strerror))
            
        self.source_code = [] # Container to hold "assembly" source code
        self.instr = [] #Container to hold instructions
        self.prog_size = self.get_prog_size()
        
    def __str__ (self):
        return "Assemble \'" + self.source_filename + "\'; Output: \'" + \
               self.out_filename + "\'"

    # Rich Comparison - Comparison based on number of instructions
    def __lt__ (self, other):
        pass

    def __le__ (self, other):
        pass
    
    def __eq__ (self, other):
        pass
    
    def __ne__ (self, other):
        pass
        
    def __gt__ (self, other):
        pass

    def __ge__ (self, other):
        pass

    # Get program size in bytes
    def get_prog_size (self):
        pass

class Instruction:

    def __init__ (self):
        pass

def main():

    p = Program("a.out")
    print (p)
