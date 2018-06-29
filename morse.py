#!/usr/local/bin/python3
import sys
import argparse
import shlex
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
"\n":['\n'],
}

def pause():
# Because readability. Fight me.
	sleep(pause_speed)

def playSymbol( symbol ):
	if symbol == '-':
		length = dah_speed
	elif symbol == '.':
		length = dit_speed
	else:
		return
	call(["play", "-q", "-n", "synth", str( length ), "sin", "450"])

def printTranslation( translation ):
# Determine when to print which characters. Also it plays a tone for the dits and dahs because I can't
# think of a way to separate that out of these fruit-loops
	global morse, blind, alpha
	for tuple in translation:
		m_code = tuple[1]
		letter = tuple[0]

		for symbol in m_code:
			if not blind and morse:
				print( symbol, end='', flush=True )
			playSymbol( symbol )

		if not blind and alpha and not (letter==" " or letter=="\t" or letter=="\n"):
			print( '[' + letter + '] ', end='', flush=True )
		pause()

	if blind or morse or alpha:
		print( "" )	

def translate( input_text ):
	translation = []
	input_text = input_text.lower()
	for letter in input_text:
		if letter in lookup:
			translation.append( [letter,lookup[letter]] )
	return translation

def tryAsFile(input):
# Just to make things more readable
	try:
		with open( str( input ) ) as file:
			input = file.read()
	except OSError:
		pass
	return input

def updateArgs():
# Flags can be toggled on and off by entering the same flag in again (for use in REPL). Not super kosher.
	global alpha, blind, morse, dah_speed, dit_speed, pause_speed
	if args.reset:
		alpha = False
		blind = False
		morse = True
		dit_speed 	= .1
		dah_speed 	= .25
		pause_speed = .3
		return

	if args.reset_print:
		alpha = False
		blind = False
		morse = True

	if args.reset_speed:
		dit_speed 	= .1
		dah_speed 	= .25
		pause_speed = .3

	if args.alpha:
		alpha = ~alpha

	if args.blind:
		blind = ~blind

	if args.no_morse:
		if morse:	morse = False
		else:			morse = True
	
	if args.faster != None:
		dah_speed	= .25-.01*args.faster
		dit_speed	= .1-.01*args.faster
		pause_speed	= .3-.01*args.faster

	if args.slower:
		dah_speed	= .25+.01*args.slower
		dit_speed	= .1+.01*args.slower
		pause_speed	= .3+.01*args.slower
	
#### E N T R Y ####
alpha = False
blind = False
morse = True
dah_speed	= .25
dit_speed	= .1
pause_speed	= .3
parser = argparse.ArgumentParser()
parser.add_argument( "text", nargs="?", 		help="Text or File to be translated, quotes are okay" )
parser.add_argument( "-b", "--blind", 			help="Go Blind; disable printing out any text", action="store_true" )
parser.add_argument( "-nm", "--no_morse", 	help="Disable printing out morse code", 			action="store_true" )
parser.add_argument( "-a", "--alpha", 			help="Print alphanumeric text",						action="store_true" )
parser.add_argument( "-r", "--reset", 			help="Set all arguments back to default",			action="store_true" )
parser.add_argument( "-rp", "--reset-print", help="Reset print arguments to default",			action="store_true" )
parser.add_argument( "-rs", "--reset-speed", help="Reset speed arguments to default",			action="store_true" )
parser.add_argument( "-f", "--faster", 	type=int, choices=[0,1,2,3,4,5],
														help="Multiplicatively increase speed .05xN"	)
parser.add_argument( "-s", "--slower", 	type=int, choices=[0,1,2,3,4,5],
														help="Multiplicatively decrease speed .05xN"	)
args = parser.parse_args()
updateArgs()

if args.text != None:
	text = tryAsFile( args.text )
	printTranslation( translate( text ) )

else:
	print("Exit loop mode with ctrl+d")
	while(True):
		try:
			input_text = input( "> " )
			args = parser.parse_args( shlex.split( input_text ) )
			updateArgs()
			if args.text != None:
				text = tryAsFile( args.text )
				printTranslation( translate( text ) )

		except EOFError:
			print( "-...-.--." )
			exit()
		
		except:
			print("Remember to surround text in quotes if using spaces")

