# -*- coding: utf-8; -*-

import re

sentence_punc = re.compile(ur'([\.?!。？！]+)(\s*[^\"\.?!。？！]?)')

def is_punc(c):
    if sentence_punc.search(c):
        return 1
    return 0

'''
This converts a string into a processable dataset for get_fs()
@param string 'abcd'
@return [['','a','b'], ['a', 'b', 'c',], ['b','c','d'],['c','d','']
'''
def make_data_set(string):
    string = string.strip('\n') 
    length = len(string)
    if length==0:
        raise Exception("empty string is not accepted for features generation")
    def scope_access_check(index):
        if index < 0 or index >= length:
            raise Exception('out of index scope')
    def get_prev(index,string):
        scope_access_check(index)
        if index == 0:
            return ''
        return string[index-1]
    def get_next(index,string):
        scope_access_check(index)
        if index == (length-1):
            return ''
        return string[index+1]
    def get_current(index,string):
        scope_access_check(index)
        return string[index]
        
    out_list = []
    prev_char = ''
    current_char = ''
    next_char = ''
    for index, char in enumerate(string):
        prev_char = get_prev(index,string)
        current_char = get_current(index, string)
        next_char = get_next(index, string)
        out_list.append([prev_char,current_char,next_char]) 

    return out_list
    
'''
It process a list with 3 items: previous char, current char, next char
@param list, e.g. ['a','b','c']
@return just look at the code
'''
def get_fs(item):
    prev_char = item[0]
    current_char = item[1]
    next_char = item[2]

    return {'is_punctuation':is_punc(current_char),
            'is_previous_char_punctuation':is_punc(prev_char),
            'is_next_char_punctuation':is_punc(next_char),
            'this_char':current_char
    }    

    '''
    return {'is_punctuation':is_punc(current_char),
            'is_previous_char_punctuation':is_punc(prev_char),
            'is_next_char_punctuation':is_punc(next_char),
    }
    '''

    '''
    return {'is_punctuation':is_punc(current_char),
            'is_previous_char_punctuation':is_punc(prev_char),
            'is_next_char_punctuation':is_punc(next_char),
            'prev_char':prev_char,
            'this_char':current_char,
            'next_char':next_char
    }
    '''

'''
this basically converts a string into a list of features
@param chars: string, e.g. "ab.d"
@return e.g. [{  'is_punctuation':0,
            'is_previous_char_punctuation':0,
            'is_next_char_punctuation':0,
            'this_char':'a'
        },{'is_punctuation':0,
            'is_previous_char_punctuation':a,
            'is_next_char_punctuation':b,
            'this_char':'b'
        },{'is_punctuation':1,
            'is_previous_char_punctuation':0,
            'is_next_char_punctuation':0,
            'this_char':'.'
        },{'is_punctuation':0,
            'is_previous_char_punctuation':1,
            'is_next_char_punctuation':0,
            'this_char':'d'
        }]
'''
def get_features(chars):
    data_set = make_data_set(chars)
    return map(get_fs,data_set)