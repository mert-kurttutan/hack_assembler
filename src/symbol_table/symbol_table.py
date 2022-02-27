
'''
SymbolTable module:
Parses the given file


Followed pep-8 style

'''

from ..utils import to_command, binary_format
from ..code import Code


class SymbolTable():
    '''
    A parser to reprsent parser for a hack program file

    NOTE: This module might seem a bit redundant since it is almost the same 
            as a dictionary object. But, I want make the modularity language-indepent
            i.e. without relying on python's dicitonary structur, as much as possible.
            See, for instance C++ implementation of this project
    ...

    Attributes
    ----------
    symbol_table

    Methods
    -------
    __init__()

    addEntry()

    contains()

    GetAddress()

    
    '''

    # Predefined symbols according to Hack Assembly Language
    predefined_RAM = {
        'SP': '0',
        'LCL': '1',
        'ARG': '2',
        'THIS': '3',
        'THAT': '4',
        'SCREEN': '16384',
        'KBD': '24576',
    }

    for i in range(16):
        predefined_RAM['R'+str(i)] = str(i)




    def __init__(self, predefined=predefined_RAM):
        '''

        Constructur for the SymbolTable object
        Creates a new empty project for this table

        '''
        if predefined is None:
            self.symbol_table = {}
        else:
            self.symbol_table = predefined

    
    def addEntry(self, symbol, address):
        '''
        
        Adds the pair (symbol, address) to the table

        Parameters
        ----------
        second: string
                Name of the symbol (label or variable in the Hack Assembly Language)
        
        third: int
                Address of the symbol in the memory

        '''

        self.symbol_table[symbol] = address


    def contains(self, symbol):
        '''
        Does the symbol table contain
        the given symbol?
        
        Parameters
        ----------
        second: string
                The name of symbol to be searched for
        Returns
                True if symbol is self.symbol_table
                False otherwise
        '''

        return symbol in self.symbol_table.keys()


    def GetAddress(self, symbol):
        '''
         Returns the address associated
         with the symbol.
        
        Parameters
        ----------
        second: string
                The name of symbol to be searched for
        Returns
                The address of symbol
        '''

        return self.symbol_table[symbol]