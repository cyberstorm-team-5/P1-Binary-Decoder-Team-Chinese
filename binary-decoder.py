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

#################################################################

def eightBit(BinaryInput):
	print("Im 8 bit")
	return

def sevenBit(BinaryInput):
	print("Im 7 bit")
	return

curr = 0


def backspace(BinaryInput, curr):
        curr -= 1
        BinaryList[curr] = ""
        return BinaryList

def tab(BinaryInput, curr):
        curr += 4
        return BinaryList

def cReturn(BinaryList, curr):
        curr += 120
        return BinaryList

def space(BinaryList, curr):
        curr += 1
        return BinaryList

file = sys.stdin.read()

#Gets rid of any blank lines from the standard input
list = file.split('\n')
BinaryInput = list[0]
Int_BinaryInput = int(BinaryInput)
Binary_Length = len(BinaryInput)

#Our dictionary that holds all of our keys
ASKIIdict = {
"0001000": "backspace", "0001001": "tab", "0001101": "cReturn", "0100000": "space", "0100001": "!",
"0100010": '"'}
test1 = ASKIIdict.get("0100010")
test2 = ASKIIdict.get("0100010")
test3 = ASKIIdict.get("0001000")
print(test1+test2)

eightASKIIdict = {"00001000": "backspace", "00001001": "tab", "00001101": "cReturn", "00100000": "space",
                  "00100001": "!","00100010": '"', "00100100" : "$", "00100101" : "%", "00100110" : "&",
                  "00100111" : "'", "00101000" : "(", "00101001": ")", "00101010": "*", "00101011" : "+",
                  "00101100": ",", "00101101" : "-", "00101110" : ".", "00101111" : "/", "00110000" : "0",
                  "00110001" : "1", "00110011" : "3", "00110100" : "4", "00110101" : "5", "00110110" : "6",
                  "00110111" : "7", "00111000" : "8", "00111001" : "9", "00111010" : ":", "00111011" : ";",
                  "00111100": "<", "00111101" : "=", "00111110" : ">", "00111111" : "?", "01000000" : "@",
                  "01000001" : "A", "01000010" : "B", "01000011" : "C", "01000100" : "D", "01000101" : "E",
                  "01000110" : "F", "01000111" : "G", "01001000" : "H", "01001010" : "J", "01001011" : "K",
                  "01001100" : "L", "01001101" : "M", "01001110" : "N", "01001111" : "O", "01010000" : "P",
                  "01010001" : "Q", "01010010" : "R", "01010011" : "S", "01010100" : "T", "01010101" : "U",
                  "01010110" : "V", "01010111" : "W", "01011000" : "X", "01011001" : "Y", "01011010" : "Z",}

BinaryList=[]
BinaryList.append(test1)
print(BinaryList)
curr+=1
BinaryList.append(test2)
print(BinaryList)
curr+=1
BinaryList = backspace(BinaryList, curr)
print BinaryList

#Checks to see if it is 7 bit or 8 bit

if (Binary_Length % 8 == 0):
	eightBit(Int_BinaryInput)
if (Binary_Length % 7 == 0):
	sevenBit(Int_BinaryInput)

print(BinaryInput)
