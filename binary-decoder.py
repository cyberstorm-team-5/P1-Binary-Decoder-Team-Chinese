################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 3-29-2019
# Description: The Python code will be able to take in binary
#	       input files (7- or 8-bit ASCII) containing only
#	       printable charactersthrough stdin and send the
#	       decoded message to stdout.
################################################################

import sys

file = sys.stdin.read()
print(file)
