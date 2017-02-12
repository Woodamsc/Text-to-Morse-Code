Made this to help learn morse code

Converts text to morse code

Requires sox & Python 3. 

Install via (1) or (2)

(1) apt-get install sox

(2) brew install sox

Not sure about Windows, sorry.

Usage:

No arguments puts you in a REPL interface. Anything you type there will get translated to Morse Code.

First argument is either text you type in or filename, quotes are stripped so don't worry about them.

If the string is a file, it will load that in and translate it, otherwise it just translates the text.

You can append '--noreadout' to the end of any command to disable printing out the code beneath it.
While in REPL, appending '--noreadout' will toggle this option On/Off

Press Ctrl+d to exit

