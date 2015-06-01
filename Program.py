#!/usr/bin/python3 -i

import sys

class Program:

    def __init__ (self, src_filename, out_filename="wimp.bin"):

        self.src_filename = src_filename 
        self.out_filename = out_filename 

        # Open Input and Output file handlers
        try:
            self.src_f = open(self.src_filename, 'r') 
            self.out_f    = open(self.out_filename, 'w')
        except IOError as e:
            print ("Error ({0}): '{1}': {2}".format(e.errno, \
                                                    self.src_filename, \
                                                    e.strerror))

        self.src_code = self.get_src_code()
        self.instr = []
        self.comments = []
        self.get_instr()

        
        # Program Information
        self.prog_size = self.get_prog_size 
        #self.num_comments = len(self.comments)
        #self.num_instructions = len(self.instr)
        #self.num_src_lines = len(self.src_code) # Number of Non-blank lines

        # Close Input and Output file handlers
        try:
            self.src_f.close()
            self.out_f.close()

        except IOError as e:
            print ("Error ({0}): '{1}': {2}".format(e.errno, \
                                                    self.out_f, \
                                                    e.strerror))

    # Return list of non-empty lines in source code
    def get_src_code (self):
        
        lines = [line.rstrip() for line in self.src_f] 
        return [line for line in lines if line] 

    # Return list of (split) lines with valid commands
    def get_instr (self):
        for line in self.src_code:
            i = Instruction(line)
            if i.valid_cmd():
                i.src_line = [x.rstrip(',') for x in i.src_line]
                self.instr.append(i)

    def get_comments (self):
        pass

    # Get program size in bytes
    def get_prog_size (self):
        pass

    # String Representation of Program
    def __str__ (self):
        return "Assemble \'" + self.src_filename + "\'; Output: \'" + \
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

    REGISTERS = ['R0', 'R1', 'R2', 'R3', 'R4', \
                 'R5', 'R6', 'R7', 'R8', 'R9']
    
    def __init__ (self, src_line):
        self.src_line = src_line.split()

    def valid_cmd (self):
        return True if self.src_line[0] in Instruction.INSTR_SET else False
        
def main():

    p = Program('in.wimp')
    
    for i in p.instr:
        print (i.src_line)

