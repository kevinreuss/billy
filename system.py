#!usr/bin/python

import vocabulary
import os
import input_parser
import executor

def work():
	while True:
		input = raw_input("> ")
		input.lower()
		os.system("clear")
		command = input_parser.parse_input(input)
		if command == "nothing detected":
			continue
		executor.execute_command(command)
		os.system("clear")
