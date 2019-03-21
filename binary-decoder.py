
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

def sevenBit(BinaryInput, curr, Binary_Length):
	print("Im 7 bit")
	BinaryList = []
	FinalList = []
	leen = Binary_Length / 7
	for x in range(leen):
		temp = BinaryInput[x*7:(x+1)*7]
		BinaryList.append(temp)
	for i in range(leen):
		temp0 = BinaryList[i]
		temp = sevenASKIIdict.get(temp0)
		print(temp)
	return


def printOutput(array):
	return

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


sevenASKIIdict = {
"0001000": "backspace", "0001001": "tab", "0001101": "carriage return", "0100000": "space", "0100001": "!",
"0100010": '"', "0100011": '#', "0100100": "$", "0100101":"%", "0100110":"&", "0100111":'"', "0101000":"(",
"0101001":")", "0101010":"*", "0101011":"+", "0101100":",", "0101101":"-", "0101110":".", "0101111":"/", 
"0110000":"0", "0110001":"1", "0110010":"2", "0110011":"3", "0110100":"4", "0110101":"5", "0110110":"7",
"0111000":"8", "0111001":"9", "0111010":":", "0111011":";", "0111100":"<", "0111101":"=", "0111110":">",
"0111111":"?", "1000000":"@", "1000001":"A", "1000010":"B", "1000011":"C", "1000100":"D", "1000101":"E",
"1000110":"F", "1000111":"G", "1001000":"H", "1001001":"I", "1001010":"J", "1001011":"K", "1001100":"L",
"1001101":"M", "1001110":"N", "1001111":"O", "1010000":"P", "1010001":"Q", "1010010":"R", "1010011":"S",
"1010100":"T", "1010101":"U", "1010110":"V", "1010111":"W", "1011000":"X", "1011001":"Y", "1011010":"Z",
"1011011":"[", "1011100": r'\ ', "1011101":"]", "1011110":"^", "1011111":"_", "1100000":'`', "1100001":"a",
"1100010":"b", "1100011":"c", "1100100":"d", "1100101":"e", "1100110":"f", "1100111":"g", "1101000":"h",
"1101001":"i", "1101010":"j", "1101011":"k", "1101100":"l", "1101101":"m", "1101110":"n", "1101111":"o",
"1110000":"p", "1110001":"q", "1110010":"r", "1110011":"s", "1110100":"t", "1110101":"u", "1110110":"v",
"1110111":"w", "1111000":"x", "1111001":"y", "1111010":"z", "1111011":"{", "1111100":"|", "1111101":"}",
"1111110":"~", "1111111":"delete"}

#temp = sevenASKIIdict.get("1010101")
#test = sevenASKIIdict.get("0100010")
#temp2 = sevenASKIIdict.get("1011100")
#print(test)

BinaryList = []

#BinaryList.append(temp)
#BinaryList.append(temp2)
#temp3 = BinaryList[1]
#temp3[0:1]
#BinaryList[1] = temp3[:0]

print(BinaryList)


curr = 0
#Checks to see if it is 7 bit or 8 bit
if (Binary_Length % 8 == 0):
	eightBit(Int_BinaryInput)
if (Binary_Length % 7 == 0):
	sevenBit(BinaryInput, curr, Binary_Length)

print(BinaryInput)
