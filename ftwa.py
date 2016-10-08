#!/usr/bin/python3

import sys
import time
import os.path
import argparse
import re
import locale

from datetime import date

class Person(object):
	@staticmethod
	def is_date(*args):
  		return all(isinstance(arg, date) for arg in args) 

	def __init__(self, name=None, surname=None, gender=None, birthdate: date=None, deathdate: date=None, father=None, mother=None, *children):

		#if not isinstance(deathdate, date) or not isinstance(birthdate, date):
		#	raise TypeError
		
		if not Person.is_date(deathdate, birthdate):
  			raise TypeError


		#var_is_good = any(isinstance(var, t) for t in [type1, type2, type3])

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
	def get_age(self):
		return

	

	def str(self):
		temp = "name={}, surn={}, g={}, bd={}, dd={}, f={}, m={}, p={}".format(self.name, self.surname, self.gender, self.birthdate, self.deathdate, self.father, self.mother, self.is_placeholder)
		temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp + temp2



def main():
	print ("test")
	Veli = Person("veli", "deli", "male", date.today(), date.today(), None, None)
	Veli2 = Person("veli2", "deli", "male", date.today(), date.today(), None, None)
	Ali = Person("ali", "deli", "male", date.today(), date.today(), None, None, Veli, Veli2)
	Fitnat = Person("fitnat", "deli", "female", date.today(), date.today(), None, None, Veli, Veli2)

	asda = Person(name="veledizina", deathdate="", birthdate=date.today())

	print(asda.str())
	print(asda.gender == True)

	#print(Veli.mother.gender)
	print(Fitnat.str())
	#print(type(Fitnat.children))
	Fitnat.add_child(asda)
	print(Fitnat.str())

if __name__ == '__main__':
	main()
