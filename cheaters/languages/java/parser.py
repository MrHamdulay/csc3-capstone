'''Authors: Jarred De Beer, Yaseen Hamdulay & Merishka Lalla
Date: 22/9/2014
Parser class
'''
from programsubmission import ProgramSubmission
import plyj.parser as plyj

'''The parser will accept a .java file and using the plyj library, parse the .java file into out system. The parser will
strip the file down into input types, join the stripped type and thereafter return the value of all tokens.'''

parser = plyj.Parser()
class JavaLanguageHandler(ProgramSubmission):
    file_types = ['java']

    def strip_unstable_atrributes(self, submission):
        ''' Function that imports plyj which has tokens and keywords set up and then manipulated in order to parse the correct
        values to the AST
        '''
        parser.lexer.input(submission)
        value = ""
        line = 1
        for token in parser.lexer:
            while token.lineno >= line:
                value = value + "\n"
                line += 1
            value += token.type[:3]


        return value