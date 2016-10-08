#!/usr/bin/python3

import sys
import time
import os.path
import argparse
import re
import locale


class Person(object):
	
	def __init__(self, name=None, surname=None, gender=None, birthdate=None, deathdate=None, father=None, mother=None, *children):
		self.gender = gender
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.deathdate = deathdate
		self.father = father
		self.mother = mother
		self.children = children
		self.set_is_placeholder()

	def add_child(self, person):
		temp_tuple = (person, )
		self.children = self.children + temp_tuple

	def add_father(self, person):
		self.father = person
	def add_mother(self, person):
		self.mother = person
	def set_is_placeholder(self):
		if self.gender:
			self.is_placeholder = False
		else:
			self.is_placeholder = True

	def str(self):
		temp = "name={}, surn={}, g={}, bd={}, dd={}, f={}, m={}, p={}".format(self.gender, self.name, self.surname, self.birthdate, self.deathdate, self.father, self.mother, self.is_placeholder)
		temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp + temp2



def main():
	print ("test")
	Veli = Person("veli", "deli", "male", "1.1.1020", "1.1.1121", None, None)
	Veli2 = Person("veli2", "deli", "male", "1.12.1020", "1.12.1121", None, None)
	Ali = Person("ali", "deli", "1.1.1001", "male", "1.1.1101", None, None, Veli, Veli2)
	Fitnat = Person("fitnat", "deli", "1.2.1001", "female", "1.3.1111", None, None, Veli, Veli2)

	asda = Person(name="veledizina")

	print(asda.str())
	print(asda.gender == True)

	#print(Veli.mother.gender)
	print(Fitnat.str())
	print(type(Fitnat.children))
	Fitnat.add_child(asda)
	print(Fitnat.str())

if __name__ == '__main__':
	main()
