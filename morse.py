#!/usr/local/bin/python3
import sys
from subprocess import call
from time import sleep

readout = True
dot = .1
dash = .3

beep_dictionary = {
"a":[dot, dash], 
"b":[dash, dot, dot, dot], 
"c":[dash, dot, dash, dot], 
"d":[dash, dot, dot], 
"e":[dot], 
"f":[dot, dot, dash, dot], 
"g":[dash, dash, dot], 
"h":[dot, dot, dot, dot], 
"i":[dot, dot], 
"j":[dot, dash, dash, dash], 
"k":[dash, dot, dash], 
"l":[dot, dash, dot, dot], 
"m":[dash, dash], 
"n":[dash, dot], 
"o":[dash, dash, dash], 
"p":[dot, dash, dash, dot], 
"q":[dash, dash, dot, dash], 
"r":[dot, dash, dot], 
"s":[dot, dot, dot], 
"t":[dash], 
"u":[dot, dot, dash], 
"v":[dot, dot, dot, dash],
"w":[dot, dash, dash],
"x":[dash, dot, dot, dash],
"y":[dash, dot, dash, dash],
"z":[dash, dash, dot, dot],
"1":[dot, dash, dash, dash, dash],
"2":[dot, dot, dash, dash, dash],
"3":[dot, dot, dot, dash, dash],
"4":[dot, dot, dot, dot, dash],
"5":[dot, dot, dot, dot, dot],
"6":[dash, dot, dot, dot, dot],
"7":[dash, dash, dot, dot, dot],
"8":[dash, dash, dash, dot, dot],
"9":[dash, dash, dash, dash, dot],
"0":[dash, dash, dash, dash, dash],
".":[dot, dash, dot, dash, dot, dash],
",":[dash, dash, dot, dot, dash, dash],
"?":[dot, dot, dash, dash, dot, dot],
}

def beep(length):
	call(["play", "-q", "-n", "synth", str(length), "sin", "450"])
	return

def pause():
	sleep(.15)
	

if len(sys.argv) < 2:
	print("Give text as input")
	exit()
elif len(sys.argv) == 3:
	if str(sys.argv[2]) == noreadout:
		readout = False

input_text = str(sys.argv[1])
try:
	with open(str(sys.argv[1])) as file:
		input_text = file.read()
except OSError:
	input_text+='\n'

input_text = input_text.lower()

for letter in input_text:
	if(readout):
		print( letter, end='', flush=True)
	if letter in beep_dictionary:
		for dotdash in beep_dictionary[letter]:
			beep(dotdash)
	pause()

