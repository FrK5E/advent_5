# Generated from advent_5.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,4,0,13,
        8,0,11,0,12,0,14,1,0,1,0,1,1,1,1,1,1,4,1,22,8,1,11,1,12,1,23,3,1,
        26,8,1,1,2,4,2,29,8,2,11,2,12,2,30,1,2,4,2,34,8,2,11,2,12,2,35,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,46,0,10,
        1,0,0,0,2,18,1,0,0,0,4,28,1,0,0,0,6,37,1,0,0,0,8,42,1,0,0,0,10,12,
        3,2,1,0,11,13,3,4,2,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,
        14,15,1,0,0,0,15,16,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,5,4,
        0,0,19,25,5,1,0,0,20,22,5,1,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,
        1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,21,1,0,0,0,25,26,1,0,0,0,
        26,3,1,0,0,0,27,29,3,6,3,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,
        0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,34,3,8,4,0,33,32,1,0,0,0,34,35,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,38,5,2,0,0,38,
        39,5,5,0,0,39,40,5,2,0,0,40,41,5,6,0,0,41,7,1,0,0,0,42,43,5,1,0,
        0,43,44,5,1,0,0,44,45,5,1,0,0,45,9,1,0,0,0,5,14,23,25,30,35
    ]

class advent_5Parser ( Parser ):

    grammarFileName = "advent_5.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'seeds:'", "'-to-'", "'map:'" ]

    symbolicNames = [ "<INVALID>", "INT", "ID", "WS", "SEEDS_KEYWORD", "TO_KEYWORD", 
                      "MAP_KEYWORD", "MAP_ID" ]

    RULE_program = 0
    RULE_seeds_statement = 1
    RULE_map_statement = 2
    RULE_map_id = 3
    RULE_map_line = 4

    ruleNames =  [ "program", "seeds_statement", "map_statement", "map_id", 
                   "map_line" ]

    EOF = Token.EOF
    INT=1
    ID=2
    WS=3
    SEEDS_KEYWORD=4
    TO_KEYWORD=5
    MAP_KEYWORD=6
    MAP_ID=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seeds_statement(self):
            return self.getTypedRuleContext(advent_5Parser.Seeds_statementContext,0)


        def EOF(self):
            return self.getToken(advent_5Parser.EOF, 0)

        def map_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(advent_5Parser.Map_statementContext)
            else:
                return self.getTypedRuleContext(advent_5Parser.Map_statementContext,i)


        def getRuleIndex(self):
            return advent_5Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = advent_5Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.seeds_statement()
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.map_statement()
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 16
            self.match(advent_5Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seeds_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEEDS_KEYWORD(self):
            return self.getToken(advent_5Parser.SEEDS_KEYWORD, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(advent_5Parser.INT)
            else:
                return self.getToken(advent_5Parser.INT, i)

        def getRuleIndex(self):
            return advent_5Parser.RULE_seeds_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeeds_statement" ):
                listener.enterSeeds_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeeds_statement" ):
                listener.exitSeeds_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeeds_statement" ):
                return visitor.visitSeeds_statement(self)
            else:
                return visitor.visitChildren(self)




    def seeds_statement(self):

        localctx = advent_5Parser.Seeds_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_seeds_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(advent_5Parser.SEEDS_KEYWORD)
            self.state = 19
            self.match(advent_5Parser.INT)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 20
                    self.match(advent_5Parser.INT)
                    self.state = 23 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def map_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(advent_5Parser.Map_idContext)
            else:
                return self.getTypedRuleContext(advent_5Parser.Map_idContext,i)


        def map_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(advent_5Parser.Map_lineContext)
            else:
                return self.getTypedRuleContext(advent_5Parser.Map_lineContext,i)


        def getRuleIndex(self):
            return advent_5Parser.RULE_map_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_statement" ):
                listener.enterMap_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_statement" ):
                listener.exitMap_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_statement" ):
                return visitor.visitMap_statement(self)
            else:
                return visitor.visitChildren(self)




    def map_statement(self):

        localctx = advent_5Parser.Map_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_map_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.map_id()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.map_line()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(advent_5Parser.ID)
            else:
                return self.getToken(advent_5Parser.ID, i)

        def TO_KEYWORD(self):
            return self.getToken(advent_5Parser.TO_KEYWORD, 0)

        def MAP_KEYWORD(self):
            return self.getToken(advent_5Parser.MAP_KEYWORD, 0)

        def getRuleIndex(self):
            return advent_5Parser.RULE_map_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_id" ):
                listener.enterMap_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_id" ):
                listener.exitMap_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_id" ):
                return visitor.visitMap_id(self)
            else:
                return visitor.visitChildren(self)




    def map_id(self):

        localctx = advent_5Parser.Map_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_map_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(advent_5Parser.ID)
            self.state = 38
            self.match(advent_5Parser.TO_KEYWORD)
            self.state = 39
            self.match(advent_5Parser.ID)
            self.state = 40
            self.match(advent_5Parser.MAP_KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(advent_5Parser.INT)
            else:
                return self.getToken(advent_5Parser.INT, i)

        def getRuleIndex(self):
            return advent_5Parser.RULE_map_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_line" ):
                listener.enterMap_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_line" ):
                listener.exitMap_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_line" ):
                return visitor.visitMap_line(self)
            else:
                return visitor.visitChildren(self)




    def map_line(self):

        localctx = advent_5Parser.Map_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_map_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(advent_5Parser.INT)
            self.state = 43
            self.match(advent_5Parser.INT)
            self.state = 44
            self.match(advent_5Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





