import sys
import os

possible_topdir = os.path.join(os.path.abspath(sys.argv[0]),
					os.pardir,
					os.pardir)
print os.path.abspath(sys.argv[0])
print possible_topdir
