#!usr/bin/python

import os
import vocabulary
from datetime import datetime
from thread import start_new_thread
import time

reminder_sound = "instrument14.wav"

def execute_command(command):
	if command == "time":
		time_hour = datetime.now().strftime('%H')
		if time_hour[0] == "0":
			time_hour= time_hour[1]
		time_minutes = datetime.now().strftime('%M')
		if time_minutes[0] == "0":
			time_minutes = time_minutes[1]
		if time_minutes == "0":
			time_minutes = ""
		time =  time_hour + " uhr " + time_minutes
		vocabulary.speak(time, "de")
	if command == "date":
		months = [
			"januar", "februar", "maerz", "april",
			"mai", "juni", "juli", "august",
			"september", "oktober", "november", "dezember"
		]
		date_day = datetime.now().strftime('%der')
		date_month_index = int(datetime.now().strftime('%m')) - 1
		date_year = datetime.now().strftime('%Y')
		date_month = months[date_month_index]
		date = date_day + date_month + date_year
		vocabulary.speak(date, "de")
	if command == "new_note":
		path = os.getcwd()
		path = path + "/data/notes/notes"
		vocabulary.speak("I am listening")
		new_note = raw_input("> ")
		new_note = new_note + "\n"
		os.system("clear")
		notes_file = open(path, "r+")
		for line in notes_file:
			notes_file.write(line)
		notes_file.write(new_note)
		notes_file.close()
		vocabulary.speak("saved note")
	if command == "read_notes":
		path = os.getcwd()
		path = path + "/data/notes/notes"
		notes_file = open(path, "r+")
		notes = []
		count = 1
		for line in notes_file:
			notes.append(str(count) + "..." + line)
			print(str(count) + " : " + line)
			count = count + 1
		for note in notes:
			vocabulary.speak(note, "de")
			vocabulary.speak("...")
		notes_file.close()
	if command == "delete_notes":
		path = os.getcwd()
		path = path + "/data/notes/notes"
		notes_file = open(path, "w")
		notes_file.truncate()
		notes_file.close()
		vocabulary.speak("deleted notes")


def _reminder_(command):
	hours_in = "0"
	minutes_in = "0"
	index_hours = command.find("our", 0, len(command))
	index_minutes = command.find("min", 0, len(command))
	if not index_hours == -1:
		while not command[index_hours] == " ":
			index_hours = index_hours - 1
		index_start = index_hours - 1
		while not command[index_start] == " ":
			index_start = index_start - 1
		hours_in = command[index_start + 1:index_hours]
	if not index_minutes == -1:
		while not command[index_minutes] == " ":
			index_minutes = index_minutes - 1
		index_start = index_minutes - 1
		while not command[index_start] == " ":
			index_start = index_start - 1
		minutes_in = command[index_start + 1:index_minutes]
	if (hours_in.isdigit() == True) and (minutes_in.isdigit() == True):
		vocabulary.speak("reminder safed")
		start_new_thread(_reminder_waiting, (int(hours_in), int(minutes_in)))
	else:
		vocabulary.speak("the hours and minutes have to be digits!")


# reminder Thread #
def _reminder_waiting(hours, minutes):
	time_hour = datetime.now().strftime('%H')
	if time_hour[0] == "0":
		time_hour= time_hour[1]
	time_minutes = datetime.now().strftime('%M')
	if time_minutes[0] == "0":
		time_minutes = time_minutes[1]

	time_hour_wait = int(time_hour)
	time_minutes_wait = int(time_minutes)
	time_minutes_wait = time_minutes_wait + minutes
	if time_minutes_wait >= 60:
		time_minutes_wait = time_minutes_wait % 60
		time_hour_wait = time_hour_wait + 1
	time_hour_wait = time_hour_wait + hours
	if time_hour_wait >= 24:
		time_hour_wait = time_hour_wait % 24

	while not((str(time_hour_wait) == time_hour) and (str(time_minutes_wait) == time_minutes)):
		time.sleep(60)
		time_hour = datetime.now().strftime('%H')
		if time_hour[0] == "0":
			time_hour= time_hour[1]
		time_minutes = datetime.now().strftime('%M')
		if time_minutes[0] == "0":
			time_minutes = time_minutes[1]
	# REMINDER #
	path = os.getcwd()
	path = path + "/data/sound/" + reminder_sound
	command = "aplay " + path
	for i in range(4):
		os.system(command)
		os.system("clear")







