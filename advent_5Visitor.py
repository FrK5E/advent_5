# Generated from advent_5.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .advent_5Parser import advent_5Parser
else:
    from advent_5Parser import advent_5Parser

# This class defines a complete generic visitor for a parse tree produced by advent_5Parser.

class advent_5Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by advent_5Parser#program.
    def visitProgram(self, ctx:advent_5Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by advent_5Parser#seeds_statement.
    def visitSeeds_statement(self, ctx:advent_5Parser.Seeds_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by advent_5Parser#map_statement.
    def visitMap_statement(self, ctx:advent_5Parser.Map_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by advent_5Parser#map_id.
    def visitMap_id(self, ctx:advent_5Parser.Map_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by advent_5Parser#map_line.
    def visitMap_line(self, ctx:advent_5Parser.Map_lineContext):
        return self.visitChildren(ctx)



del advent_5Parser