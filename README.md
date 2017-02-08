Made this to help learn morse code
Converts text to morse code

Requires sox. Install via 1) or 2)
1) apt-get install sox
2) brew install sox

Also you need python. I used python3.
Python2 would probably work if you change the print statements

First argument is either a user entered string or filename, quotes are stripped.
It first checks if the string is a file.
If it is, it converts the file contents. Otherwise, it will just convert the string you typed.

Second argument is an option 'noreadout' where it will not printout the text at all.
