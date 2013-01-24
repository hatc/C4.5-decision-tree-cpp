#!/usr/bin/python
import sys

if len(sys.argv) < 3:
 raise Exception('path to <input> <output> files required')
with open(sys.argv[1],'rU') as f:
 with open(sys.argv[2],'w') as g:
  for l in f:
   g.write(l)

