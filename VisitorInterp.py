from antlr4 import *
from advent_5Parser import advent_5Parser
from advent_5Visitor import advent_5Visitor
import map_class



class VisitorInterp(advent_5Visitor):

    def __init__(self):
        self.seeds = []
        self.maps = []


    # Visit a parse tree produced by advent_5Parser#seeds_statement.
    def visitSeeds_statement(self, ctx:advent_5Parser.Seeds_statementContext):
        ints = ctx.INT()
        for i in ints: 
            self.seeds.append( int(i.getText()) )

        return None


    # Visit a parse tree produced by advent_5Parser#map_id.
    def visitMap_id(self, ctx:advent_5Parser.Map_idContext):
        self.maps.append( map_class.Map(ctx.getText()))
        return None


    # Visit a parse tree produced by advent_5Parser#map_line.
    def visitMap_line(self, ctx:advent_5Parser.Map_lineContext):
        i = map_class.MapItem( dest=int(ctx.children[0].getText()), start=int(ctx.children[1].getText()), length=int(ctx.children[2].getText()))
        self.maps[-1].items.append(i)
        return None
    
    def getMaps(self):
        return self.maps

    def getSeeds(self): 
        return self.seeds 
        