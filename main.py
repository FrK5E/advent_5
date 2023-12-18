import sys
from antlr4 import *
from advent_5Lexer import advent_5Lexer
from advent_5Parser import advent_5Parser
from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = advent_5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = advent_5Parser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)

    seeds = vinterp.getSeeds()
    maps = vinterp.getMaps()
    pass 

if __name__ == '__main__':
    main(sys.argv)
