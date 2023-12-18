# Generated from advent_5.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,4,0,17,8,0,11,0,12,0,18,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,2,4,2,29,8,2,11,2,12,2,30,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,4,1,0,48,57,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,12,13,32,32,58,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,1,16,1,0,0,0,3,20,1,0,0,0,5,28,1,0,0,0,7,34,1,
        0,0,0,9,41,1,0,0,0,11,46,1,0,0,0,13,51,1,0,0,0,15,17,7,0,0,0,16,
        15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,2,1,0,0,
        0,20,24,7,1,0,0,21,23,7,2,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,
        1,0,0,0,24,25,1,0,0,0,25,4,1,0,0,0,26,24,1,0,0,0,27,29,7,3,0,0,28,
        27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,
        0,32,33,6,2,0,0,33,6,1,0,0,0,34,35,5,115,0,0,35,36,5,101,0,0,36,
        37,5,101,0,0,37,38,5,100,0,0,38,39,5,115,0,0,39,40,5,58,0,0,40,8,
        1,0,0,0,41,42,5,45,0,0,42,43,5,116,0,0,43,44,5,111,0,0,44,45,5,45,
        0,0,45,10,1,0,0,0,46,47,5,109,0,0,47,48,5,97,0,0,48,49,5,112,0,0,
        49,50,5,58,0,0,50,12,1,0,0,0,51,52,3,3,1,0,52,53,3,9,4,0,53,54,3,
        3,1,0,54,55,3,11,5,0,55,14,1,0,0,0,4,0,18,24,30,1,6,0,0
    ]

class advent_5Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    WS = 3
    SEEDS_KEYWORD = 4
    TO_KEYWORD = 5
    MAP_KEYWORD = 6
    MAP_ID = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'seeds:'", "'-to-'", "'map:'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS", "SEEDS_KEYWORD", "TO_KEYWORD", "MAP_KEYWORD", 
            "MAP_ID" ]

    ruleNames = [ "INT", "ID", "WS", "SEEDS_KEYWORD", "TO_KEYWORD", "MAP_KEYWORD", 
                  "MAP_ID" ]

    grammarFileName = "advent_5.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


