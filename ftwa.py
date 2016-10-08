#!/usr/bin/python3

import sys
import time
import os.path
import argparse
import re
import locale

class Person(object):
	
	def __init__(self, gender, name, surname, birthdate, deathdate, father, mother, *children):
		self.gender = gender
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.deathdate = deathdate
		self.father = father
		self.mother = mother
		self.children = children

	def add_child(self, Person):
		print ()

	def add_father(self, Person):
		print ()
	def add_mother(self, Person):
		print ()
	def set_is_placeholder(self):
		if self.gender:
			self.placeholder = False


def main():
	print ("test")
	Veli = Person("male", "veli", "deli", "1.1.1020", "1.1.1121", None, None)
	Veli2 = Person("male", "veli2", "deli", "1.12.1020", "1.12.1121", None, None)
	Ali = Person("male", "ali", "deli", "1.1.1001", "1.1.1101", None, None, Veli, Veli2)
	Fitnat = Person("female", "fitnat", "deli", "1.2.1001", "1.3.1111", None, None, Veli, Veli2)



	#print(Veli.mother.gender)
	print(Ali.children[1].name)

if __name__ == '__main__':
	main()
