#!/usr/local/bin/python3
import sys
from subprocess import call
from time import sleep

lookup = {
"e":[	'.'											],
"t":[	'-'											],
"i":[	'.', 	'.'									],
"n":[	'-', 	'.'									],
"a":[	'.',	'-'									],
"m":[	'-', 	'-'									],
"g":[	'-', 	'-', 	'.'							],
"o":[	'-', 	'-', 	'-'							],
"k":[	'-', 	'.',  '-'							],
"r":[	'.', 	'-', 	'.'							],
"s":[	'.', 	'.',  '.'							],
"w":[	'.', 	'-', 	'-'							],
"u":[	'.', 	'.',  '-'							],
"d":[	'-', 	'.',  '.'							],
"b":[	'-', 	'.',	'.',  '.'					],
"c":[	'-', 	'.',  '-', 	'.'					],
"f":[	'.', 	'.',  '-', 	'.'					],
"h":[	'.', 	'.',  '.',  '.'					],
"j":[	'.', 	'-', 	'-', 	'-'					],
"l":[	'.', 	'-', 	'.',  '.'					],
"p":[	'.', 	'-', 	'-', 	'.'					],
"q":[	'-', 	'-', 	'.',  '-'					],
"v":[	'.', 	'.',  '.',  '-'					],
"x":[	'-', 	'.',  '.',  '-'					],
"y":[	'-', 	'.',  '-', 	'-'					],
"z":[	'-', 	'-', 	'.',  '.'					],
"1":[	'.', 	'-', 	'-', 	'-',	'-'			],
"2":[	'.', 	'.',  '-', 	'-', 	'-'			],
"3":[	'.', 	'.',  '.',  '-', 	'-'			],
"4":[	'.', 	'.',  '.',  '.',  '-'			],
"5":[	'.', 	'.',  '.',  '.',  '.'			],
"6":[	'-', 	'.',  '.',  '.',  '.'			],
"7":[	'-', 	'-', 	'.',  '.',  '.'			],
"8":[	'-', 	'-', 	'-', 	'.',  '.'			],
"9":[	'-', 	'-', 	'-', 	'-', 	'.'			],
"0":[	'-', 	'-', 	'-', 	'-', 	'-'			],
".":[	'.', 	'-', 	'.',  '-', 	'.', 	'-'	],
",":[	'-', 	'-', 	'.',  '.',  '-',	'-'	],
"?":[	'.', 	'.',  '-', 	'-', 	'.',	'.'	],
" " :[' | '],
"\t":[' | '],
"\n":[' | '],
}

def pause():
# Because readability. Fight me.
	sleep(.3)

def playSymbol( symbol ):
	if symbol == '-':
		length = .3
	elif symbol == '.':
		length = .1
	else:
		return
	call(["play", "-q", "-n", "synth", str( length ), "sin", "450"])
	
def translate( input_text ):
	input_text = input_text.lower()
	for letter in input_text:
		if letter in lookup:
			for symbol in lookup[letter]:
				if readout:
					print( symbol, end='', flush=True )
				playSymbol( symbol )
		pause()
	if readout:
		print( "" )

def tryAsFile(input):
# Just to make things more readable
	try:
		with open( str( input ) ) as file:
			input = file.read()
	except OSError:
		pass
	return input

#### E N T R Y ####
readout = True
num_args = len( sys.argv )
if str( sys.argv[num_args-1] ) == '--noreadout':
	readout = False
	num_args -= 1

if num_args > 1:
	text = str( sys.argv[1] )
	text = tryAsFile( text )
	translate( text )

else:
	while(True):
		try:
			text = input( "> " )
			if text == '--noreadout':
				readout = ~readout
			else:
				translate( text )

		except EOFError:
			print( "-...-.--." )
			exit()

