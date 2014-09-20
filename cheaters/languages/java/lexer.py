__author__ = 'Merishka Lalla'
import plyj.parser as plyj

def java_strip_variables(code):
    ''' Function that imports plyj which has tokens and keywords set up and then manipulated in order to parse the correct
    values to the AST
    '''
    parser = plyj.Parser()
    parser.lexer.input(code)
    value = ""
    line = 1
    for token in parser.lexer:
        while token.lineno >= line:
            value = value + "\n"
            line += 1
        value += token.type + " "


    return value
