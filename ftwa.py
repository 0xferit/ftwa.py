#!/usr/bin/python3

import sys #sys library is importing
import time
import os.path
import argparse
import re
import locale

from datetime import date

class Person(object): #This is our Person object which creates struct to keep information
	@staticmethod
	def is_date(*args):
  		return all(isinstance(arg, date) for arg in args)

	@staticmethod
	def is_person(*args):
		return all(isinstance(arg, Person) for arg in args)
	
	@staticmethod
	def is_none(*args):
		return all(isinstance(None, (date)) for arg in args) 

	def __init__(self, name=None, surname=None, gender=None, birthdate: date=None, deathdate: date=None, father=None, mother=None, *children):

		#if not isinstance(deathdate, date) or not isinstance(birthdate, date):
		#	raise TypeError
		
		#if not Person.is_date(deathdate, birthdate) and not None in(birthdate, deathdate):
  		#	raise TypeError

		#if not Person.is_person(father, mother, *children):
  		#	raise TypeError
	
		#print("any:{}".format(all(isinstance(var, date) for var in [birthdate, deathdate])))

		self.gender = gender
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.deathdate = deathdate
		self.father = father
		self.mother = mother
		self.children = children


	def add_child(self, person):
		temp_tuple = (person, )
		self.children = self.children + temp_tuple

	def get_children(self):
		return self.children

	def set_father(self, person):
		self.father = person

	def get_father(self):
		return self.father

	def set_mother(self, person):
		self.mother = person

	def get_mother(self):
		return self.mother

	def is_placeholder(self): #We agreed that the missing information as placeholder
		if self.name and self.surname and self.gender and self.birthdate and self.deathdate and ((self.father and self.mother) or (not self.father and not self.mother)):
			return False
		else:
			return True
	
	def get_age(self): # TODO
		return

	def is_alive(self): #TODO
		return

	def get_level(self): #TODO
		return

	def get_relationship_with(self, relative): # Returns relationship between this object and "relative" arg
		return:

	def str(self):
		temp = "name={}, surn={}, g={}, bd={}, dd={}, f={}, m={}, p={}".format(self.name, self.surname, self.gender, self.birthdate, self.deathdate, self.father, self.mother, self.is_placeholder)
		temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp + temp2



def main():
	print ("test")
	Veli = Person("veli", "deli", "male", date.today(), date.today(), "o", None)
	Veli2 = Person("veli2", "deli", "male", date.today(), date.today(), None, None)
	Ali = Person("ali", "deli", "male", date.today(), date.today(), None, None, Veli, Veli2)
	Fitnat = Person("fitnat", "deli", "female", date.today(), date.today(), None, None, Veli, Veli2)

	asda = Person(name="veledizina")

	print(asda.str())
	print(asda.gender == True)

	#print(Veli.mother.gender)
	print(Fitnat.str())
	#print(type(Fitnat.children))
	Fitnat.add_child(asda)
	print(Fitnat.str())

if __name__ == '__main__':
	main()
