


def to_command(current_line):
    '''
    Turns a line into command by eliminating whitespace and comments
    as written in hack machine language

    Parameters
    ----------
    first: string
        The string for the current line of program to be parsed into command
    
    Returns
    -------
        The string for the command part of the current line
    '''


    comment_ch = "//"
    # Ignore the next line character and comments
    before_comment, _, _= current_line.rstrip('\n').partition("//")
    
    # Eliminate whitespaces
    before_comment = before_comment.replace(" ", "")

    return before_comment



def binary_format(bin_str, length):
    '''
    Adds necessary number of 0s at the beginning of bin_str so that 
    binary number bin_str has length many digits
    length > len(bin_str)

    Parameters
    ----------
    first: string
        The string of a binary number 
    
    second: int
        The desired length of output string of binary number

    Returns
        the ensuing string of binary number of addition of 0s

    '''

    zero_num = length - len(bin_str)

    if zero_num < 0:
        ValueError("The requested length should be higher than the lenght of binary number")

    else:
        result_bin = "0"*zero_num + bin_str
        return result_bin