#!usr/bin/python

import os

def speak(text, language = "en-us"):
	os.system('espeak -v ' + language +  ' "' + text + '"')
