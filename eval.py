# -*- coding: utf-8; -*-
#
# (c) 2016-2017 NLP2CT Lab, http://nlp2ct.cis.umac.mo
#
# This file is part of Course CISB454.
import sys
import re
import codecs

EOS_PUNCTUATIONS = set([u'。', u'！', u'？', u'.', u'!', u'?'])

# Usage: python eval.py /path/to/your/result.txt ref.txt
if __name__ == "__main__":
	test_file = codecs.open(sys.argv[1], 'r', 'utf-8')
	test_str = test_file.read()
	test_file.close()
	ref_file = codecs.open(sys.argv[2], 'r', 'utf-8')
	ref_str = ref_file.read()
	ref_file.close()
	test_str = test_str.replace('\r\n', '\n')
	test_str = re.sub('\n{2,}', '\n', test_str)
	test_str = re.sub('[\\s\t]+\n', '\n', test_str)
	ref_str = re.sub('\n{2,}', '\n', ref_str)
	true_pos = 0.0
	false_pos = 0.0
	true_neg = 0.0
	false_neg = 0.0
	i = 0
	j = 0
	while i < len(test_str) and j < len(ref_str):
		while i < len(test_str) and test_str[i] not in EOS_PUNCTUATIONS:
			i += 1
		while j < len(ref_str) and ref_str[j] not in EOS_PUNCTUATIONS:
			j += 1
		if i >= len(test_str) - 1 or j >= len(ref_str) - 1:
			break
		if test_str[i + 1] == '\n':
			if ref_str[j + 1] == '\n':
				true_pos += 1
			else:
				false_pos += 1
		else:
			if ref_str[j + 1] == '\n':
				false_neg += 1
			else:
				true_neg += 1
		i += 1
		j += 1
	print 'tp={0} fp={1} tn={2} fn={3}'.format(true_pos, false_pos, true_neg, false_neg)
	precision = true_pos / (true_pos + false_pos)
	recall = true_pos / (true_pos + false_neg)
	print 'precision={0} recall={1}'.format(precision, recall)
	f1_score = (2*precision*recall)/(precision+recall)
	print 'f1_score={0}'.format(f1_score)
