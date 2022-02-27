'''
Parser module:
Parses the given file


Followed pep-8 style

'''
import copy

from ..utils import to_command, binary_format
from ..code import Code
from ..symbol_table import SymbolTable



class Parser():
    '''
    A parser to reprsent parser for a hack program file

    ...

    Attributes
    ----------
    assembly_file : _io.TextIOWrapper (file object)
        file object for the hack program to be parsed into binary code
    
    current_line : str
        currently read line of assembly file
    
    command_list: list
        list of commands added with the same order
        as they appear in the program file

    current_command_idx : int
        integer to indicate the current (most recently read) command

    Methods
    -------
    __init__(self, file_name):
        Constructs the parser instance

    close(self):
        Closes the the filestream object (assembly file) of instance    
    
    hasMoreCommands(self):
        Checks if there is more command in hack programming file
            with a few necessary additional operations
    
    advance(self):
        Advances the current command to the next available command from the assembly file
        Retruns True if it can advance one command, False otherwise

    commandType(self):
        Returns the type of current command

    symbol(self):
        Returns the symbol of the current command
    
    dest(self):
        Returns teh dest mnemonic in current C-command.
    
    comp(self):
        Returns the comp mnemonic in current C-command.
    
    jump(self):
        Returns the jump mnemonic in current C-command

    
    Static Method
    -------------
    
    parse_whole(parser, output_file)
        Write binary code version of the code inside parser object
    
    '''

    # Constants of Hack Assembly Language
    global REGISTER_BIT
    REGISTER_BIT = 16


    def __init__(self, file_name):
        '''
        Opens the input file (with name file_name)/stream and
        gets ready to parse it

        Parameters
        ----------
        first : string
            the name of the program file to be processed
        '''
        self.file_name = file_name
        self.assembly_file = open(file_name)
        self.current_line = ""
        self.command_list = []
        self.current_command_idx = -1
    
    def close(self):
        self.assembly_file.close()

    def hasMoreCommands(self):
        '''
        Note: Whitespace and comments are not commands
        First checks if there any command to be added from command_list
        If there is, does nothing
        If there is not, it reads the rest of the file until it finds another command
        If it finds another valid command, it adds the command to command_list, returns True
        If it doesnt find another command, it does nothing and returns False

        Returns
            True if there is more commands in the input file, 
            False otherwise

        Example:
            # Initial values of attributes
            self.command_list=[], self.current_command_idx=-1

            # call the function
            self.hasMoreCommands();    #returns True
            
            # the effect of the call self.hasMoreCommands()
            self.command_list=[] -> ['@2']

        '''

        # there is more command to be added
        if self.current_command_idx < len(self.command_list)-1 and len(self.command_list) > 0:
            return True

        # if the no command is added or there is
        # iterate until arrive at non-empty command line
        Flag1 = False
        Flag2 = False
        while (not Flag1) and (not Flag2):
            self.current_line = self.assembly_file.readline()
            next_command = to_command(self.current_line)

            # Stop at the end of file
            Flag1 = (len(self.current_line)==0)
            
            # Stop if there is a valid command
            Flag2 = (len(next_command) != 0)

        # The end of file -> no more command
        if Flag1:
            return False
        # add the next command if it is non-empty command
        else:
            self.command_list.append(next_command)
            return True


    def advance(self):
        '''
        Note: Whitespace and comments are not commands
        Checks if there is more command via hasMoreCommands
            - If there is, it increases the current_command_idx to the next
                available index
            - If there is not, it prints optional message
                (as there is no more command be parsed)

        Returns
            True, if it is possible to advace one command more
            False, otherwise
        '''

        # If the entire program is parsed, no more parsing is allowed
        if self.hasMoreCommands():
            self.current_command_idx += 1
            return True
        # if no more commands, close the file
        else:
            print('Entire file is parsed into binary code')
            return False



    def commandType(self):
        '''
        Returns: str
            - Returns the type of the current command:m
                - A_COMMAND for @Xxx where Xxx is either a symbol 
                    or a decimal number
                
                - C_COMMAND for dest=comp;jump
                
                - L_COMMAND (actually, pseudocommand) for (Xxx) 
                    where Xxx is a symbol.

            - If no type is matches, it returns 'ERROR'
        
        See:https://www.nand2tetris.org/

        Example:
            # example valid command in hack assembly language
            D;JLE -> 'C_COMMAND'    
        '''
        # current command
        command = self.command_list[self.current_command_idx]

        if command[0] == '@':
            return 'A_COMMAND'
        
        elif ('=' in command) or (';' in command):
            return 'C_COMMAND'

        elif command[0] == '(' and command[-1] == ')':
            return  'L_COMMAND'

        else:
            return 'ERROR'


    def symbol(self):
        ''''
        Returns: 
            The symbol or decimal Xxx of the current command
            @Xxx or (Xxx). Should be called only when commandType() is
            A_COMMAND or L_COMMAND
        
        '''
        command = self.command_list[self.current_command_idx]
        command_type = self.commandType()
        if command_type == 'A_COMMAND':
            return command[1:]
        
        elif command_type == 'L_COMMAND':
            return command[1:-1]
        
        else:
            raise RuntimeError("Symbol method should be called only for A_COMMAND and L_COMMAND")



    def dest(self):
        '''
        Returns:
            Returns the dest mnemonic in the current C-command 
            (8 possibilities). Should be called only 
            when commandType() is C_COMMAND.

        '''
        command = self.command_list[self.current_command_idx]
        command_type = self.commandType()
        if command_type == 'C_COMMAND':
            if '=' in command:
                command, _, _= command.partition("=")
            else:
                command = 'null'

            return command
        else:
            raise RuntimeError("Dest method should be called only for C_COMMAND")




    def jump(self):
        '''
        Returns:
            Returns the jump mnemonic in the current C-command 
            (8 possibilities). Should be called only 
            when commandType() is C_COMMAND.

        '''
        command = self.command_list[self.current_command_idx]
        command_type = self.commandType()
        if command_type == 'C_COMMAND':
            if ';' in command:
                _, _, command= command.partition(";")
            else:
                command = 'null'

            return command
        else:
            raise RuntimeError("Jump method should be called only for C_COMMAND")



    def comp(self):
        '''
        Returns:
            Returns the comp mnemonic in the current C-command 
            (28 possibilities). Should be called only 
            when commandType() is C_COMMAND.

        '''
        command = self.command_list[self.current_command_idx]
        command_type = self.commandType()
        if command_type == 'C_COMMAND':
            if ';' in command:
                command, _, _= command.partition(";")
            if '=' in command:
                _, _, command = command.partition('=')

            return command
        else:
            raise RuntimeError("Comp method should be called only for C_COMMAND")


    @staticmethod
    def parse_whole_first(parser):

        # Define: ROM -> Instruction Memory
        #         RAM -> Instruction and Data Memory
        RAM_ROM_table = SymbolTable()

        parser_copy = Parser(parser.file_name)
        program_counter = 0
        while parser_copy.advance():

            if parser_copy.commandType() in ['A_COMMAND', 'C_COMMAND']:
                program_counter += 1
            
            elif parser_copy.commandType() in ['L_COMMAND']:
                RAM_ROM_table.addEntry(parser_copy.symbol(), str(program_counter))
        
        parser_copy.close()
        return RAM_ROM_table

    @staticmethod
    def parse_whole_second(parser, output_file, memory_table):
        '''
        Starting from current line, parses through the entire program given by parser object. It extracts the
        command line by line and translates into binary code. Then, each binary
        code is written into output file.

        Note: If the current command does not match any of the defined command types
                it wont write anything

        Parameters
        ----------
        
        first: Parser
            Parser object whose program file is to be processed and translated into binary code
        
        second: str
            Then name of the file into which binary code is written

        '''
        
        # next available location in the main memory (RAM)
        next_memory = 16
        with open(output_file, 'a') as file:

            while parser.advance():
                # set to empty string to prevent 
                # repetition of previous command
                final_binary = ''

                if parser.commandType() == 'A_COMMAND':

                    # If symbol is not number, change it with corresponding number
                    if not parser.symbol().isnumeric():

                        if not memory_table.contains(parser.symbol()):
                            # use the next available memory 
                            # to allocate memory of a new variable
                            memory_table.addEntry(parser.symbol(), str(next_memory))
                            next_memory += 1

                        # Change the current command to the value in SymbolTable
                        parser.command_list[parser.current_command_idx] = '@'+memory_table.GetAddress(parser.symbol())

                    # Current command is ready to be processed
                    value_binary = bin(int(parser.symbol()))[2:]
                    value_binary = binary_format(value_binary, REGISTER_BIT)
                    final_binary = value_binary + '\n'

                elif parser.commandType() == 'C_COMMAND':
                    # Parts of C-Commands
                    dest_command = parser.dest()
                    jump_command = parser.jump()
                    comp_command = parser.comp()

                    # Binary versions
                    dest_binary = Code.dest(dest_command)
                    jump_binary = Code.jump(jump_command)
                    comp_binary = Code.comp(comp_command)
                    
                    final_binary = '111'+comp_binary+dest_binary+jump_binary+'\n'
                
                # if it is L_COMMAND, do nothing

                file.write(final_binary)