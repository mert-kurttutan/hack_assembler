'''
Parser module:
Parses the given file


Followed pep-8 style

'''



class Code():
    '''
    A code Module to contain functions that translates
    Hack assemble language into binary code

    Methods
    -------

    dest(mnemonic):
        Returns the binary code of the dest mnemonic.

    comp(mnemonic):
        Returns the binary code of the comp mnemonic.
    
    jump(mnemonic):
        Returns the binary code of the jump mnemonic.

    '''

    # binary code for dest mnemonic, based on Hack Asembly Language
    dest_dict = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111',
    }

    # binary code for jump mnemonic, based on Hack Asembly Language
    jump_dict = {
        'null': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111',
    }


    # binary code for comp mnemonic, based on Hack Asembly Language
    comp_dict = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000', 'M': '1110000',
        '!D': '0001101',
        '!A': '0110001', '!M': '1110001',
        '-D': '0001111',
        '-A': '0110011', '-M': '1110011',
        'D+1': '0011111',
        'A+1': '0110111', 'M+1': '1110111',
        'D-1': '0001110',
        'A-1': '0110010', 'M-1': '1110010',
        'D+A': '0000010', 'D+M': '1000010',
        'D-A': '0010011', 'D-M': '1010011',
        'A-D': '0000111', 'M-D': '1000111',
        'D&A': '0000000', 'D&M': '1000000',
        'D|A': '0010101', 'D|M': '1010101',
    }
    

    @staticmethod
    def dest(mnemonic, map_dict=dest_dict):
        '''
        Returns the binary code of the dest mnemonic.

        Parameters
        ----------
        first: str
            the mnemonic of dest to be translate into binary code
        
        second: dict
            the dictionary that contains mapping from mnemonic
                to binary code

        Returns
        -------
            String representing the binary code
        '''

        return map_dict[mnemonic]


    @staticmethod
    def jump(mnemonic, map_dict=jump_dict):
        '''
        Returns the binary code of the dest mnemonic.

        Parameters
        ----------
        first: str
            the mnemonic of dest to be translate into binary code
        
        second: dict
            the dictionary that contains mapping from mnemonic
                to binary code

        Returns
        -------
            String representing the binary code
        '''

        return map_dict[mnemonic]



    @staticmethod
    def comp(mnemonic, map_dict=comp_dict):
        '''
        Returns the binary code of the dest mnemonic.

        Parameters
        ----------
        first: str
            the mnemonic of dest to be translate into binary code
        
        second: dict
            the dictionary that contains mapping from mnemonic
                to binary code

        Returns
        -------
            String representing the binary code
        '''

        return map_dict[mnemonic]
