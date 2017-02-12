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

Flags can be used now. In REPL mode they 'stick' so that they toggle.

Use --no-morse (-nm) will disable morse code printout (type again to enable in REPL)

Use --alpha (-a) to enable alphanumeric printout (type again to disable in REPL)

Use --blind (-b) to go blind. (Disables printout of both morse and alpha regardless of their states)

Use --faster[N] (-f[N]) to increase the speed of playback

Use --slower[N] (-s[N]) to decrease the speed of playback

Use --reset (-r) to reset all flags to default

Use --reset-print to reset print flags only (-a -nm -b)

Use --reset-speed to reset speed flags only (-s -f)

e.g. 

./morse.py -nm -a "hello world"
[h] [e] [l] [l] [o] [w] [o] [r] [l] [d]

./morse.py -a 'hello world'
....[h] .[e] .-..[l] .-..[l] ---[o]  | .--[w] ---[o] .-.[r] .-..[l] -..[d]

And press Ctrl+d to exit when you want

