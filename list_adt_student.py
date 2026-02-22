def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """
    return {
        'size': size,    
        'data': [None] * size,   
        'n': 0,    
        'i': 0    
    }

def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    return listADT['n']==0

def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    return listADT['n']==listADT['size']

def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    i = listADT [ " i " ] 
    s = listADT [ " size " ] 
    n = listADT["n"] 
    l = (i +1)%s 
    return listADT [ " data " ][ l ]

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    if i < 0 or i >= listADT['n']:  
        return
    actual_index = (listADT['i'] + i) % listADT['size']
    listADT['data'][actual_index] = e


def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT['n']

def add(i,e,listADT):
    """
    Adds an element at the specific index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.

    """
    if is_full(listADT):
        return("List is full")
    
    if i < 0 or i > listADT["n"]:
        return ("Invalid index")
    
    last_index = listADT["n"]
    
    for j in range(last_index, i, -1): 
        listADT["data"][j] = listADT["data"][j-1] 

    listADT["data"][i] = e
    listADT["n"] += 1

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        return 
    if i < 0 or i >= listADT["n"]:
        return ("Invalid index")
    elem = listADT["data"][i]
    last_index = listADT["n"] - 1
    for j in range(i, last_index):
        listADT["data"][j] = listADT["data"][j+1]
    listADT["data"][last_index] = None
    listADT["n"] -= 1
    return elem

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full ( listADT ):
        return
    i = listADT ["i"] 
    n = listADT ["n"] 
    s = listADT ["size"] 
    listADT ["data"][( i + n ) % s ] = e 
    listADT ["n"] = ( n + 1)

def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        return None
    last_index = (listADT['i'] + listADT['n'] - 1) % listADT['size']
    k=listADT['data'][last_index]
    listADT['data'][last_index] = None
    listADT['n'] -= 1
    return k

def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full ( listADT ) :
        return 
    i = listADT [ "i" ] 
    n = listADT [ " n " ] 
    s = listADT [ " size " ] 
    listADT [ " data " ][ i ] = e
    listADT [ " i " ] = (s -1) if (i -1) < 0 else (i -1) 
    listADT [ " n " ] = n + 1

def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty ( listADT ) :
        return 
    i = listADT [ " i " ] 
    n = listADT [ " n " ] 
    s = listADT [ " size " ] 
    e = listADT [ " data " ][( i +1) % s ] 
    listADT [ " i " ] = ( i + 1) % s 
    listADT [ " n " ] = n - 1

def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    return listADT["data"]['i']

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    i=listADT['i'] 
    n=listADT['n'] 
    s=listADT['size']
    return get ((i+n)%s,listADT)
    
