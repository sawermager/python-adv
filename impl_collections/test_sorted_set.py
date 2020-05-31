import unittest

from impl_collections.sorted_set import SortedSet

class TestConstruction(unittest.TestCase):
    """
    These tests ensure that we can construct instances of
    SortedSet in the way what we would expect of any Python
    collection.

    Arguments:
        unittest {[type]} -- unittest base class
    """
    
    def test_empty(self):
        s = SortedSet([])
        
    def test_from_sequence(self):
        s = SortedSet([7,8,3,1])
        
    def test_with_duplicates(self):
        s = SortedSet([8,8,8])
        
    def test_from_iterable(self):
        """
        Check that we can construct an instance from an
        arbituary iterable.
        Note: In this case, I've used a generator (since generators
        return iterables). The goal here is to show that we can 
        successfully construct a sorted set in a way that is 
        typical for python collections. We want to know that we
        can construct a sorted collection from iterable 
        sequences of various configurations, including being empty.
        We don't want to rely on the argument being passed to the 
        constructor being anything more sophisticated than an 
        iterable. Using a generator for this, is as good a way
        as any to test for that.
        """
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
        g = gen6842()
        s = SortedSet(g)
        
if __name__ == "__main__":
    unittest.main()

