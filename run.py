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
import fs_extractor


if __name__ == "__main__":
    '''
    init the program, prepare input, output
    '''
    trainfile = 'traineasy.pt'
    in_file =  codecs.open(trainfile,encoding='utf-8',mode='r')
    out_file =  codecs.open(sys.argv[1],encoding='utf-8',mode='w')
    cout = Pipe(lambda x: out_file.write(str(x)))

    
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
    
    '''
    convert test data into features set
    '''
    testfile = 'data/test.txt'
    test_stream = codecs.open(testfile,encoding='utf-8',mode='r')
    lines = test_stream.readlines()
    
    '''
    for one line case
    '''
    line = lines[0]
    def process_line(line):
        classfier = mx_classifier
        features = fs_extractor.get_features(line)
        
        if len(features) != len(line):
            raise Exception('not match!')
        
        is_sentence_end = lambda f: classfier.classify(f) == 'y'
        
        results = map(is_sentence_end, features)
        
        for index, char in enumerate(line):
            char | cout
            if results[index]:
                '\n' | cout
        return 
    
    process_line(line)
    
    out_file.close()
    in_file.close()
    test_stream.close()