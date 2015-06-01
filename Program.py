#!/usr/bin/python3 -i

import sys

class Program:

    def __init__ (self, source_filename, out_filename="wimp.bin"):

        self.source_filename = source_filename # Input File
        self.out_filename = out_filename       # Output File

        # Open Input and Output file handlers
        try:
            self.source_f = open(self.source_filename, 'r') # Input file handler
            self.out_f    = open(self.out_filename, 'w')    # Output file handler
        except IOError as e:
            print ("Error ({0}): '{1}': {2}".format(e.errno, \
                                                    self.source_filename, \
                                                    e.strerror))

        self.source_code = self.get_source_code()
        self.instr = []
        self.comments = []

        # Program Information
        self.prog_size = self.get_prog_size 
        self.num_comments = len(self.comments)
        self.num_instructions = len(self.instr)
        self.num_source_lines = len(self.source_code) # Number of Non-blank lines

        # Close Input and Output file handlers
        try:
            self.source_f.close()
            self.out_f.close()

        except IOError as e:
            print ("Error ({0}): '{1}': {2}".format(e.errno, \
                                                    self.out_f, \
                                                    e.strerror))

    def get_source_code (self):
        # One-liner to do the same thing
        # return list(filter(lambda x: x, [line.rstrip() for line in self.source_f]))
        
        lines = [line.rstrip() for line in self.source_f]
        return [line for line in lines if line]

    def get_instr (self):
        pass

    def get_comments(self):
        pass
    
    # Get program size in bytes
    def get_prog_size (self):
        pass

    # String Representation of Program
    def __str__ (self):
        return "Assemble \'" + self.source_filename + "\'; Output: \'" + \
               self.out_filename + "\'"

    # Comparison based on program size (bytes)
    def __lt__ (self, other):
        return self.prog_size < other.prog_size

    def __le__ (self, other):
        return self.prog_size <= other.prog_size
    
    def __eq__ (self, other):
        return self.prog_size == other.prog_size
    
    def __ne__ (self, other):
        return self.prog_size != other.prog_size
        
    def __gt__ (self, other):
        return self.prog_size > other.prog_size

    def __ge__ (self, other):
        return self.prog_size >= other.prog_size

class Instruction:

    INSTR_SET = ['MOV', 'ADDC', 'ORL', 'ANL', 'XRL', \
                 'SWAP', 'CLR', 'SETB', 'SJMP', 'JZ', 'LCD']

    def __init__ (self,):
        pass


def main():

    p = Program('in.wimp')
    print (p.source_code)
    print (p.num_source_lines)
