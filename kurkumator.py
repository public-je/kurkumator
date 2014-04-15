#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import choice
import re
import os
import readline
import sys

def kurkum(msg, file):
	result = ''
	variation = 1
	strlst = regex.findall(msg)
	for each in strlst:
		if len(each)<3:
			result += each + ' '
		else:
			patt = each[-3:]
			pattern = ur'(?m)^[А-Яа-яё]*' + patt + ur'$'
			list = re.findall(pattern, file)
			if (list):
				variation *= len(list)
				result += choice(list) + ' '
			else:
				result += each + ' '
	return result + u'1/' + str(variation)

if __name__ == "__main__":
	f = open(os.getcwd() + os.sep + '100kwords.txt', 'r')
	words = f.read().decode('utf-8')
	regex = re.compile(ur'[а-яёА-Яa-zA-Z]+')
	while True:
		try:
			msg = unicode(raw_input(),'utf-8')
			print (kurkum(msg, words))
		except(EOFError):
			print ('quiting')
			sys.exit()

