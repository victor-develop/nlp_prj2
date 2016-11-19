# -*- coding: utf-8; -*-
# this piece is just for labeling correct samples
# it expect a text file of well-sepereated lines as argv[1]

import sys
import codecs
import re
from pipe import *

# source: http://disq.us/p/xxvxpq
def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), reversed(funcs), x)
    
def sequence(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs, x)

sentence_punc = re.compile(ur'([\.?!。？！]+)(\s*[^\"\.?!。？！]?)')

get_last_word = lambda wlist: wlist[-1:][0]
get_last_char = lambda w: w[-1:]

def is_punc(c):
    if sentence_punc.search(c):
        return 1
    return 0
        


if __name__ == "__main__":
	s = " i have a say on my presi"
	compose(is_punc,get_last_char,get_last_word)(s.split()) | lineout
	sequence(get_last_word,get_last_char,is_punc)(s.split())|lineout
