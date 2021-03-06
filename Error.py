xs'''
Error.py

Error class to provide facilites for error handling and logging error messages
'''

#!/usr/bin/python -i

class Error:

    type = {
        'file_io' : '',                  # File read/write error
        'invalid_func' : '',             # Invalid function name
        'invalid_args' : '',             # Improper number # of arguments
        'invalid_chars' : ''             # Improper hex characters
    }
        
    def __init__ (self):
        pass

    def __str__ (self):
        pass

    def throw_err (self):
        pass
