# -*- coding: utf-8; -*-
# this piece is just for labeling correct samples
# it expect a text file of well-sepereated lines as argv[1]

import sys
import codecs
import re
from pipe import *
from labeling import *
from nltk import MaxentClassifier
from fp_tools import *
import pickle


if __name__ == "__main__":
    '''
    init the program, prepare input, output
    '''
    in_file =  codecs.open(sys.argv[1],encoding='utf-8',mode='r')

    
    '''
    label our train data
    '''
    lines = in_file.readlines()
    labeled_entries = flat_list(map(get_labeled, lines))
    
    '''
    train a classifier
    '''
    mx_classifier = MaxentClassifier.train(labeled_entries);
    
    '''
    save the classifier to the disk
    '''
    mx_file = open('mx_classifier.pkl', 'wb')
    pickle.dump(mx_classifier, mx_file)
    mx_file.close()

    in_file.close()

    mx_classifier.show_most_informative_features(5) | stdout