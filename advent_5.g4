grammar advent_5;


program
    : seeds_statement map_statement+ EOF
    ;

seeds_statement: SEEDS_KEYWORD INT ( INT+ )?
    ;
    
map_statement:  map_id + (map_line+);

map_id: ID TO_KEYWORD ID MAP_KEYWORD; 

map_line: INT INT INT ;

INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;

SEEDS_KEYWORD : 'seeds:';

TO_KEYWORD : '-to-';

MAP_KEYWORD : 'map:';

MAP_ID: ID  TO_KEYWORD  ID  MAP_KEYWORD;