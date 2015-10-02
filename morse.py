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
	6: ".....",
	7: "--...",
	8: "---..",
	9: "----.",
	0: "-----"
}

def morseChar(c):
	result = ""
	# if c is a key in the dictionary, return its value
	if c in morseDict.keys():
		return morseDict[c]

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

#main program here

#remember argv always has at least the name of the program, check for more
#if more than default param, assign remainder of argv as string to phrase variable
if (len(sys.argv) > 1):
	#assign uppercase version of args to phrase
	phrase = str(sys.argv[1:]).upper()
#else, get a phrase from the user
else:
	# otherwise there are no args, so get a string from user
	phrase = input("Enter a phrase: ").upper()

#print the end result of calling morseString on phrase
print(morseString(phrase))