class SortedSet:
    """
    Create a Python Set object that also sorts the Set by
    default and support collection protocols for containers,
    sized, iterable, and sequence objects. Note: it's a lot of
    work to implement all required options for a squence.
    """
    
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        """Need to know here if we're being called with
        an index (integer) or a slice (slice object)

        Arguments:
            index {[type]} -- integer

        Returns:
            [type] -- item or slice (as a SortedSet obj) 
        """
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result
    
    def __repr__(self):
        """This is needed to straighten out the mess that
        __getitem__() returns for slices passed to it.
        We need to represent the returned slice in the same
        string format as what the test 'list' slice returns.

        Returns:
            [type] -- [description]
        """
        return "SortedSet({})".format(repr(self._items) if self._items else '')
        
    def __eq__(self, right_hand_side):
        if not isinstance(right_hand_side, SortedSet):
            return NotImplemented
        return self._items == right_hand_side._items

    def __neq__(self, right_hand_side):
        if not isinstance(right_hand_side, SortedSet):
            return NotImplemented
        return self._items != right_hand_side._items