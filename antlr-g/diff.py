#!/bin/sh
""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""
import difflib, optparse, sys
from time import ctime
from os import stat

'''def diff(from_file_path, to_file_path, out_file_path):
	with open(from_file_path, 'U') as f:
		fromlines = f.readlines()
	with open(to_file_path, 'U') as f:
		tolines = f.readlines()
	fromdate = ctime(stat(from_file_path).st_mtime)
	todate = ctime(stat(to_file_path).st_mtime)
	
	r = difflib.unified_diff(fromlines, tolines, from_file_path, to_file_path, fromdate, todate)
	with open(out_file_path, 'w') as f:
		f.writelines(r)'''

def main():
	# Configure the option parser
	usage = "usage: %prog [options] fromfile tofile"
	parser = optparse.OptionParser(usage)
	parser.add_option("-c", action="store_true", default=False,
	                  help='Produce a context format diff')
	parser.add_option("-u", action="store_true", default=False,
	                  help='Produce a unified format diff (default)')
	parser.add_option("-m", action="store_true", default=False,
	                  help='Produce HTML side by side diff (can use -c and -l in conjunction)')
	parser.add_option("-n", action="store_true", default=False,
	                  help='Produce a ndiff format diff')
	parser.add_option("-l", "--lines", type="int", default=3,
	                  help='Set number of context lines (default 3)')
	(options, args) = parser.parse_args()
	if len(args) == 0:
		parser.print_help()
		sys.exit(1)
	if len(args) != 2:
		parser.error("need to specify both a fromfile and tofile")
	
	fromfile, tofile = args # as specified in the usage string
	with open(fromfile, 'U') as f:
		fromlines = f.readlines()
	with open(tofile, 'U') as f:
		tolines = f.readlines()
	fromdate = ctime(stat(fromfile).st_mtime)
	todate = ctime(stat(tofile).st_mtime)
	
	n = options.lines
	if options.c:
		diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=options.lines)
	elif options.n:
		diff = difflib.ndiff(fromlines, tolines)
	elif options.m:
		diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile, context=options.c, numlines=options.lines)
	else:
		diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=options.lines)
	sys.stdout.writelines(diff)
	
if __name__ == '__main__':
	main()
