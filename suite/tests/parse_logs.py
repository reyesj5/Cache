import sys
import os.path
import argparse

def parse(filename, d, r, n):


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", type=int, help="Which test to run, default runs all tests available")
	parser.add_argument("-d", "--delimeter", type=int, help="The number of cores to use, default c=Number of available CPUs in architecture")
	parser.add_argument("-r", "--remove", type=str, help="The name of the architecture being benchmarked, for log purposes [REQUIRED]")
	parser.add_argument("-n", "--remove", type=str, help="The name of the architecture being benchmarked, for log purposes [REQUIRED]")
	args = parser.parse_args()

	architecture = ''
	struct = 'lists'
	test = None
	cores = multiprocessing.cpu_count()
	iterations = None
	size = None
	
	if not(args.architecture == None):
		architecture = args.architecture
	else:
		raise ValueError("Need to specify which architecture is being used.")
	if not(args.struct == None):
		struct = args.struct
	if not(args.test == None):
		n_test = args.test
	if not(args.cores == None):
		cores = args.cores
	if not(args.iterations == None):
		iterations = args.iterations
	if not(args.size == None):
		size = args.size