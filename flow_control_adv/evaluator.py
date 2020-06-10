
# The while-else clause. Most used, if used at all, for search failures.

def is_comment(item):
    return isinstance(item, str) and item.startswith('#')

def execute(program):
    """ Execute a stack program.

    Args:
        program: Any stack-like container where each item in the stack
        is a callable operators or non-callable operands. The top-most
        items on teh stack may be strings beginning with '#' for
        the purposes of documentation. Staack-like means support for:
        
        item = stack.pop()  # Remove and return the top item
        stack.append(item)  # Push an item to the top
        if stack:           # False in a boolean context when empty
    """
    
    # First, find the start of the 'program' by skipping
    # any item that is a comment.
    # Note: The evaluation of a list as an experession evaluates as True
    # if the list is non-empty. 
    while program:
        item = program.pop()
        if not is_comment(item):

            # If item is not a comment, push it back onto the
            # stack.
            program.append(item)

            # Break from the loop here because we assume comments are
            # ONLY appear at the start of the 'program'.
            break
    else: # nobreak
        print("Empty program!")
        return
    
    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        print("Item=", item)
        print("Program=", program)
        print("Pending=", pending)
        
        # determine if item is a fn or not, i.e. operator.add, 
        # operator.sub, etc...
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:   #nobreak
        print ("Program successful")

        # Print all non-callable values left on the stack.
        print ("Result: ", pending)
    print ("Finished")
        
                  
        

    

if __name__ == '__main__':
    import operator
    
    # Note: that since we're using python Lists for the stack; the top
    # of the stack is the end of the list. So, we'll need to reverse it.
    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constats",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    print(program)

    execute(program)

