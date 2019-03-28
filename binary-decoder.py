#!/usr/bin/env python2.7
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

#process input as a sequence of 7- or 8-bit ascii code to convert to a readable string
def convertASCII(binaryInput, binaryLength, numBits):
        
        finalString = ""
        
        #loop through indexes such that i = the 0th bit in every sequence of numBits
        #(7 or 8) bits in the binaryInput
        for i in range(0, binaryLength-(numBits-1), numBits):

                #get the ASCII number for the bits
                num = int(binaryInput[i:i+numBits], 2)

                #check if the num will produce a backspace (ASCII 8)
                if(num == 8):
                        #remove the trailing character from the string
                        finalString = finalString[:-1]
                   
                else:
                        #convert the 7 or 8 bits into an integer form base 2, then use chr
                        #to convert the integer into the equivalent ASCII character
                        finalString += chr(num)
                
        print(finalString)
        return


########################MAIN#####################################

file = sys.stdin.read()

#Gets rid of any blank lines from the standard input
list = file.split('\n')
binaryInput = list[0]

binaryLength = len(binaryInput)


#Check if input is 7- or 8-bit bianry seperately, 
#outputting the message with both if both are applicable
if (binaryLength % 8 == 0):
	convertASCII(binaryInput, binaryLength, 8)
	
if (binaryLength % 7 == 0):
	convertASCII(binaryInput, binaryLength, 7)




