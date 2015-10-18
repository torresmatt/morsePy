#imports:
import sys

# dictionary for matching valid morse characters to dot-dash strings
morseDict = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",

	1: ".----",
	2: "..---",
	3: "...--",
	4: "....-",
	5: ".....",
	6: "-....",
	7: "--...",
	8: "---..",
	9: "----.",
	0: "-----"
}

def morseChar(c):
	# if c is a key in the dictionary, return its value
	if c in morseDict.keys():
		return morseDict[c]
	else:
		return '*'

def morseString(original):
	# result string to be built and returned
	result = ""
	#iterate through each character in original
	for c in original:
		#if space, add as space to result string
		if c.isspace():
			result += "_"		
		#if it's a digit or a letter, add the morse code dot sequence then a divider "|"
		elif c.isdigit() or c.isalpha():
			result += morseChar(c) + "|"
	return result

def fileMode():
	if (len(sys.argv) < 4):
		print "Not enough arguments!"
		print helpMenu()

def inputMode():
	print(morseString(raw_input("Enter phrase: ").upper()))


#generates a help menu for when program is launched wrong
def helpMenu():
	result = "";
	#build it line by line
	result += "Usage:\n"
	result += "------\n"
	result += "USER INPUT PHRASE:\n"
	result += "python morse.py (no arguments)\n"
	result += "Prompts user for phrase and outputs morse version of phrase to screen.\n"
	result += "\n"
	result += "PARAMETER PHRASE:\n"
	result += "python morse.py <some phrase>\n"
	result += "All parameters are treated as a single phrase and output to screen in morse.\n"
	result += "\n"
	result += "FILE MODE:\n"
	result += "python morse.py -f <input filename> <output filename>\n"
	result += "Input file is opened, translated to morse and output to output file.\n"
	return result
#main program here

#if argv length is 1 no params were passed. Do phrase mode.
if (len(sys.argv) == 1):
	inputMode()
#if argv length is more than 1, they either want file mode or param phrase mode.
elif (len(sys.argv) > 1):
	# if first param is -f do file mode
	if (sys.argv[1] == "-f"):
		fileMode()
	# if first param is not -f, just do the rest as a phrase
	else:
		phrase = ' '.join(sys.argv[1:]).upper()
		print morseString(phrase)
else:
	print(helpMenu())

#todo
#add file mode "-f" option.
