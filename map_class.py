import unittest
from dataclasses import dataclass

@dataclass
class MapItem:
    """Store map item"""
    dest: int
    start: int
    length: int


class Map(object): 
    def __init__( self, id ): 
        self.id = id
        self.items = []

    def map_integer(self, n: int ) -> int: 

        for item in self.items: 
            if n>=item.start and n<item.start+item.length: 
                return n-item.start+item.dest
        return n
    
 
class TestMapMethods(unittest.TestCase):

    def test_1(self):

        a = Map('testing_id')
        a.items.append( MapItem( dest=50, start=98, length=2) )
        a.items.append( MapItem( dest=52, start=50, length=48) )
        
        for i in range(50):
            self.assertEqual(a.map_integer(i), i)
        for i in range( 50, 98, 1):
            self.assertEqual(a.map_integer(i), i+2)
        self.assertEqual(a.map_integer(98), 50)
        self.assertEqual(a.map_integer(99), 51)


if __name__ == '__main__':
    unittest.main()
