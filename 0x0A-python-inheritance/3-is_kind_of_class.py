#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """ checking if an obj is of type a_class
        or of one of it's super or subclasses
    
    args:
        obj: variable
        a_class: class to be checked
    """
    if isinstance(obj, a_class):
        return True
    return False
