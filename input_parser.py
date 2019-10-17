#!usr/bin/python

import executor

def parse_input(input):
	if not input.find("time", 0, len(input)) == -1:
		return "time"
	if not input.find("date", 0, len(input)) == -1:
		return "date"
	if ((not input.find("new", 0, len(input)) == -1) or (not input.find("add", 0, len(input)) == -1) or (not input.find("take", 0, len(input)) == -1))and (not input.find("note", 0, len(input)) == -1):
		return "new_note"
	if (not input.find("delete", 0, len(input)) == -1) and (not input.find("note", 0, len(input)) == -1):
		return "delete_notes"
	if not input.find("note", 0, len(input)) == -1:
		return "read_notes"
	if (not input.find("re", 0, len(input)) == -1) and (not input.find("in", 0, len(input)) == -1) and ((not input.find("our", 0, len(input)) == -1) or (not input.find("min", 0, len(input)) == -1)):
		executor._reminder_(input)

	return "nothing detected"