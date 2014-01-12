#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MenuItem:

	def __init__(self, name, action):
		self.name = name
		self.action = action

	def get_text(self):
		return self.name

	def get_action(self):
		return self.action

	def set_lcd(self, lcd):
		self.lcd = lcd

class Menu(MenuItem):

	ITEM_PREFIX = "\x7e"

	def __init__(self, lcd, name):
		self.lcd = lcd
		self.name = name
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def _open_menu(self):
		lcd = self.lcd
		items = self.items
		lcd.clear()
		lcd.cursor()
		lcd.blink()

		curpos = 0
		item_count = len(items)
		
		if curpos % 2 == 0:
				firstitem = items[curpos]

				if curpos < (item_count - 1):
						seconditem = items[curpos + 1]
				else:
						seconditem = ""
		else:
				firstitem = items[curpos - 1]
				seconditem = items[curpos]

		lcd.clear()
		lcd.message(self.ITEM_PREFIX)
		lcd.message(firstitem.get_text())
		lcd.message("\n")
		lcd.message(self.ITEM_PREFIX)
		lcd.message(seconditem.get_text())
		lcd.setCursor(len(ITEM_PREFIX) - 1, curpos % 2)

		nothingHappened = 0
		btnWait = True
		while btnWait:
				if nothingHappened == 100:
						lcd.backlight(lcd.OFF)
						print ("Turning backlight off!")

				if lcd.buttonPressed(lcd.DOWN):
						lcd.backlight(lcd.ON)
						nothingHappened = 0
						curpos = (curpos + 1) % item_count
						btnWait = False
						sleep(0.1)

				if lcd.buttonPressed(lcd.UP):
						lcd.backlight(lcd.ON)
						nothingHappened = 0
						curpos = (curpos - 1) % item_count
						btnWait = False
						sleep(0.1)
				sleep(0.1)
				nothingHappened = nothingHappened + 1

	def get_action(self):
		return self._open_menu
