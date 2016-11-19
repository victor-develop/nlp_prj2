# -*- coding: utf-8; -*-
# this piece is just for labeling  samples


import re
from fs_extractor import *
import pickle

'''
It label a sentence's every char-feature as 'n' but the last char is 'y'
@param line: string
@return [({features},'n'),({features},'n'),({features},'y')]
'''
def get_labeled(line):
    label_yes = lambda x:(get_fs(x),'y')
    label_no = lambda x:(get_fs(x),'n')
    data_set = make_data_set(line)
    
    yes_features = map(label_yes,[data_set.pop()])
    no_features = map(label_no,data_set)
    
    out_list = []
    out_list.extend(yes_features)
    out_list.extend(no_features)
    
    return out_list
    
def load_classifier(filepath):
    f = open(filepath, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier


    
