#! /usr/bin/env python
try:
	import sys
	import math
	import os
	from subprocess import call
	from mPTP import *
except ImportError:
	print("Please install the scipy and other dependent package first.")
	print("If your OS is ubuntu or has apt installed, you can try the following:") 
	print(" sudo apt-get install python-setuptools python-numpy python-qt4 python-scipy python-mysqldb python-lxml python-matplotlib")
	sys.exit()

def print_options():
	print("usage: python merge.py example/p1.sum example/p2.sum example/p12.sum")
	print("Options: merge p2.sum to p1.sum, keep p.sum taxa order, and output to p12.sum")


if __name__ == "__main__":
	if len(sys.argv) < 3: 
		print_options()
		sys.exit()
	
	fp1 = sys.argv[1]
	fp2 = sys.argv[2]
	fout = sys.argv[3]
	
	p1 = partitionparser(fin = fp1)
	p2 = partitionparser(fin = fp2)
	p2.translate_to(p1, fout+".tmp")
	p3 = partitionparser(fout+".tmp")
	p3.summary(fout)