It was quite fun to quickly sketch the grammar in 
`http://lab.antlr.org/` 

Once happy, dump the lexer and parser rules into a single file advent_5.g4. 

To generate the parser, issue command: 

antlr4 -v 4.13.0 -Dlanguage=Python3 -visitor advent_5.g4

Based on some examples with calculator, finally arrived at the VisitorInterp.py. 

On Ubuntu, quite easy to install prerequisities, as described in https://www.antlr.org/download.html as: 

pip install antlr4-python3-runtime

