import unittest

from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):
    """
    These tests ensure that we can construct instances of
    SortedSet in the way what we would expect of any Python
    collection including an empty list.

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
        return generators, which are iterators). The goal here is to 
        show that we can successfully construct a sorted set in a way 
        that is typical for python collections. We want to know that 
        we can construct a sorted collection from iterable 
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

    def test_default_empty(self):
        s = SortedSet()
    
class TestContainerProtocol(unittest.TestCase):
    """A container should support 'in' and 'not in'
    operations.

    Arguments:
        unittest {[type]} -- unittest base class
    """
    
    def setUp(self):
        self.s = SortedSet([6,7,3,9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)
    def test_negative_contained(self):
        self.assertFalse(2 in self.s)
    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)
    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

class TestSizeProtocol(unittest.TestCase):
    """Should support the len() operation.

    Arguments:
        unittest {[type]} -- unittest base class
    """

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)
        
    def test_one(self):
        s = SortedSet([42])
        self.assertEqual(len(s), 1)
    
    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)
        
    def test_with_duplicates(self):
        s = SortedSet([1,1,1])
        self.assertEqual(len(s), 1)

class TestIterableProtocol(unittest.TestCase):
    """Should support iterating on the sequence.

    Arguments:
        unittest {[type]} -- unittest base clase
    """
    
    def setUp(self):
        self.s = SortedSet([7,2,1,1,9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration,lambda: next(i))
    
    def test_for_loop(self):
        index = 0
        expected = [1,2,7,9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

class TestSequenceProtocol(unittest.TestCase):
    """All the mess of access that is included
    for python sequences.

    Arguments:
        unittest {[type]} -- unittest base class
    """

    def setUp(self):
        self.s = SortedSet([1,4,9,13,15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_end(self):
        with self.assertRaises(IndexError):
            self.s[5]
            
    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_four(self):
        self.assertEqual(self.s[-4], 4)

    def test_index_one_before_beginning(self):
        self.assertRaises(IndexError, lambda: self.s[-6])

    # Note that slicing a sorted set should return a 
    # sorted set.
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1,4,9]))

    def test_slice_from_end(self):
        self.assertEqual(self.s[3:], SortedSet([13,15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbituary(self):
        self.assertEqual(self.s[2:4], SortedSet([9,13]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)
    



    
            

    
        
        
if __name__ == "__main__":
    unittest.main()

