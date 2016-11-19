# -*- coding: utf-8; -*-
# this piece is just for labeling correct samples
# it expect a text file of well-sepereated lines as argv[1]

import sys
import codecs
import re
from pipe import *
from nltk import MaxentClassifier
from fp_tools import *
import pickle
import fs_extractor
from labeling import *


if __name__ == "__main__":
    '''
    init the program, prepare input, output
    '''
    out_file =  codecs.open(sys.argv[1],encoding='utf-8',mode='w')
    cout = Pipe(lambda x: out_file.write((x)))
    
    '''
    load up classifier
    '''
    mx_file = open('mx_classifier.pkl', 'rb')
    mx_classifier = pickle.load(mx_file)
    mx_file.close()
    mx_classifier = load_classifier('mx_classifier.pkl')
    '''
    convert test data into features set
    '''
    testfile = 'data/test.txt'
    test_stream = codecs.open(testfile,encoding='utf-8',mode='r')
    lines = test_stream.readlines()
    
    def process_line(line, classifier, output):
        line = line.strip()
        if len(line) == 0:
            return

        features = fs_extractor.get_features(line)
        
        if len(features) != len(line):
            raise Exception('not match!')
        
        is_sentence_end = lambda f: classifier.classify(f) == 'y'
        
        results = map(is_sentence_end, features)
        
        last_index = len(line)-1
        for index, char in enumerate(line):
            char | output
            if results[index] or index == last_index:
                '\n' | output
        return
    
    def process_lines(lines,classifer, output):
        for l in lines:
            process_line(l, classifer, output)
    
    process_lines(lines, mx_classifier, cout)
    
    out_file.close()
    test_stream.close()