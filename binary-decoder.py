################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	       Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	         Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 3-29-2019
# Github repo: https://github.com/cyberstorm-team-5/P1-Binary-Decoder-Team-Chinese
# Description: Program 1: Binary Decoder
#              The Python code will be able to take in binary
#	             input files (7- or 8-bit ASCII) containing only
#	             printable charactersthrough stdin and send the
#	             decoded message to stdout.
################################################################

import sys
import re
################################################################
def eightBit(BinaryInput):
	print("Im 8 bit")
	return

def sevenBit(BinaryInput):
	print("Im 7 bit")
	return



























file = sys.stdin.read()
#Gets rid of any blank lines from the standard input
list = file.split('\n')
BinaryInput = list[0]
Int_BinaryInput = int(BinaryInput)
Binary_Length = len(BinaryInput)
#Our dictionary that holds all of our keys
ASKIIdict = {
"0001000": "backspace", "0001001": "tab", "0001101": "carriage return", "0100000": "space", "0100001": "!",
"0100010": '"'




























}
test = ASKIIdict.get("0100010")
print(test)

#Checks to see if it is 7 bit or 8 bit

if (Binary_Length % 8 == 0):
	eightBit(Int_BinaryInput)
if (Binary_Length % 7 == 0):
	sevenBit(Int_BinaryInput)

print(BinaryInput)
