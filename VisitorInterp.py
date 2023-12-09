import sys
from antlr4 import *
from advent_5Parser import advent_5Parser
from advent_5Visitor import advent_5Visitor

class VisitorInterp(advent_5Visitor):

     # Visit a parse tree produced by advent_5Parser#program.
    def visitProgram(self, ctx:advent_5Parser.ProgramContext):
        return None

    # Visit a parse tree produced by advent_5Parser#seeds_statement.
    def visitSeeds_statement(self, ctx:advent_5Parser.Seeds_statementContext):
        return None


    # Visit a parse tree produced by advent_5Parser#map_statement.
    def visitMap_statement(self, ctx:advent_5Parser.Map_statementContext):
        return None


    # Visit a parse tree produced by advent_5Parser#map_id.
    def visitMap_id(self, ctx:advent_5Parser.Map_idContext):
        return None


    # Visit a parse tree produced by advent_5Parser#map_line.
    def visitMap_line(self, ctx:advent_5Parser.Map_lineContext):
        return None
    