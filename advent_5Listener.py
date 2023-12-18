# Generated from advent_5.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .advent_5Parser import advent_5Parser
else:
    from advent_5Parser import advent_5Parser

# This class defines a complete listener for a parse tree produced by advent_5Parser.
class advent_5Listener(ParseTreeListener):

    # Enter a parse tree produced by advent_5Parser#program.
    def enterProgram(self, ctx:advent_5Parser.ProgramContext):
        pass

    # Exit a parse tree produced by advent_5Parser#program.
    def exitProgram(self, ctx:advent_5Parser.ProgramContext):
        pass


    # Enter a parse tree produced by advent_5Parser#seeds_statement.
    def enterSeeds_statement(self, ctx:advent_5Parser.Seeds_statementContext):
        pass

    # Exit a parse tree produced by advent_5Parser#seeds_statement.
    def exitSeeds_statement(self, ctx:advent_5Parser.Seeds_statementContext):
        pass


    # Enter a parse tree produced by advent_5Parser#map_statement.
    def enterMap_statement(self, ctx:advent_5Parser.Map_statementContext):
        pass

    # Exit a parse tree produced by advent_5Parser#map_statement.
    def exitMap_statement(self, ctx:advent_5Parser.Map_statementContext):
        pass


    # Enter a parse tree produced by advent_5Parser#map_id.
    def enterMap_id(self, ctx:advent_5Parser.Map_idContext):
        pass

    # Exit a parse tree produced by advent_5Parser#map_id.
    def exitMap_id(self, ctx:advent_5Parser.Map_idContext):
        pass


    # Enter a parse tree produced by advent_5Parser#map_line.
    def enterMap_line(self, ctx:advent_5Parser.Map_lineContext):
        pass

    # Exit a parse tree produced by advent_5Parser#map_line.
    def exitMap_line(self, ctx:advent_5Parser.Map_lineContext):
        pass



del advent_5Parser