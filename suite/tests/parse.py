#!/usr/bin/env python
# coding=utf-8

import sys
import os.path
import argparse

# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def parse(filename, out, delimeter=',', r = True, n = -1, ignore = 0):
	print("Parsing...")
	with open(filename) as f:
	    content = f.readlines()
	if r:
		content = [x.strip() for x in content]
	
	parsed = open(out,'w')
	i = ignore
	result = ''
	while i < len(content):
		if n == -1:
			result = content[i]
			i += 1
			for j in range(i,len(content),1):
				result += delimeter + content[j]
				i += 1
		else:
			result += content[i]
			i += 1
			for j in range(i,i+n,1):
				result += delimeter + content[j]
				i += 1
			result += '\n'
	parsed.write(result)
	parsed.close()
	print("Parsed Successfully.")


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", type=str, help="Name of the file to parse")
	parser.add_argument("-o", "--output", type=str, help="Name of the parsed file output")
	parser.add_argument("-d", "--delimeter", type=str, help="Delimeter to parse the output")
	parser.add_argument("-r", "--remove", type=str, help="Remove white spaces, default r=true")
	parser.add_argument("-n", "--lines", type=int, help="The number of lines to combine")
	parser.add_argument("-s", "--skip", type=int, help="The number of initial lines to ignore in the file")
	args = parser.parse_args()

	file = ''
	output = ''
	delimeter = ','
	remove = True
	lines = -1
	skip = 0
	
	if not(args.file == None):
		file = args.file
	else:
		raise ValueError("Need to specify which file is being parsed.")
	if not(args.output == None):
		output = args.output
	else:
		raise ValueError("Need to specify name of file to output.")
	if not(args.delimeter == None):
		delimeter = args.delimeter
	if not(args.remove == None):
		remove = str2bool(args.remove)
	if not(args.lines == None):
		lines = args.lines
	if not(args.skip == None):
		skip = args.skip

	parse(file,output,delimeter,remove,lines,skip)