# -*- coding: utf-8; -*-

'''
edited from source: http://disq.us/p/xxvxpq
@param variable numbers of functions
@return a function which accepts an argument, and executes a sequence of functions in order
'''
def sequence(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs, x)


"""
This function takes a lists which may contain multiple lists and makes it flat,
e.g. [['Hap','Ho'],['second','list']] will become ['Hap','Ho','second','list']
@param list_of_lists: a list of lists
@type list_of_lists: list
"""
def flat_list(list_of_lists):
    return [y for x in list_of_lists for y in x]