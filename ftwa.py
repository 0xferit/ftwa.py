#!/usr/bin/python3

import sys #sys library is importing
import time
import os.path
import argparse
import re
import locale
from enum import Enum
from datetime import date
	

class MetaPerson(type):
    def __iter__(self):
        for attr in dir(Person):
            if not attr.startswith("__"):
                yield attr
	
class Relation(Enum):

	SPOUSE, FATHER, MOTHER, CHILD = range(4)

relation_table = {}		

class Person(metaclass=MetaPerson): #This is our Person object which creates struct to keep information
	@staticmethod
	def is_date(*args):
  		return all(isinstance(arg, date) for arg in args)

	@staticmethod
	def is_person(*args):
		return all(isinstance(arg, Person) for arg in args)
	
	@staticmethod
	def is_none(*args):
		return all(isinstance(None, (date)) for arg in args) 

	def __iter__(self):
		for each in self.__dict__.keys():
			yield self.__getattribute__(each)

	def __init__(self, name=None, surname=None, gender=None, birthdate: date=None, deathdate: date=None, father=None, mother=None, spouse=None, *children):

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
		if self.father == 2:
			if not self.father.name == None:
				print()
				self.get_father().add_child(self)

		self.mother = mother


		self.children = [children]
		

		self.spouse = spouse


	def add_child(self, person):
		temp_tuple = [person]
		self.children.extend(temp_tuple)

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

	def set_spouse(self, person):
		self.spouse = person

	def get_spouse(self):
		return self.spouse

	def is_placeholder(self): #We agreed that the missing information as placeholder
		if self.name and self.surname and self.gender and self.birthdate and self.deathdate and ((self.father and self.mother) or (not self.father and not self.mother)):
			return False
		else:
			return True

	def get_first_degree_relatives(self):
		temp = [x for x in [self.mother, self.father, self.spouse] if x is not None]
		temp2 = [y for y in self.children if y is not None]
		temp.extend(temp2)
		print(type(temp))
		return temp
	
	def get_age(self):
		today = date.today()
		birthdate = self.birthdate
		return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

	def is_alive(self): 
		today = date.today()
		deathdate = self.deathdate
		return (0 > (today.year - deathdate.year - ((today.month, today.day) < (deathdate.month, deathdate.day))))

	def get_level(self):
		if self.father == None and self.father == None:
			return 0
		if not self.father == None and not self.mother == None:
			return 1 + max(self.father.get_level(), self.mother.get_level())
		if not self.father == None and self.mother == None: 
			return 1 + self.father.get_level()
		else:
			return 1 + self.mother.get_level()

	def get_relationship_with(self, relative, path=[], rel_path=[]): # Taslak
		path.append(self)		
		if(self == relative):
			print("kendine eşit {}".format(self.name))
			for p in path:
				print (p.name)
			return rel_path
		else:
			rel_paths = []
			if not self.spouse == None and not self.spouse in path:
				print("spouse:{}".format(self.spouse.str()))
				print("newpath:{}".format(rel_path))
				rel_path.append(Relation.SPOUSE)
				

				rel_paths.append(self.spouse.get_relationship_with(relative, path, rel_path))

			if not self.father == None and not self.father in path:
				print("father:{}".format(self.father.str()))
				print("newpath:{}".format(rel_path))

				rel_path.append(Relation.FATHER)
				rel_paths.append(self.father.get_relationship_with(relative, path, rel_path))

			if not self.mother == None and not self.mother in path:
				print("mother:{}".format(self.mother.str()))
				print("newpath:{}".format(rel_path))

				rel_path.append(Relation.MOTHER)
				rel_path.append(self.mother.get_relationship_with(relative, path, rel_path))

			if not self.children == None:
				for child in self.children:
					if not child in path:
						rel_path.append(Relation.MOTHER)
						rel_paths.append(child.get_relationship_with(relative, path, rel_path))
			else:
				print("boş dönecek")
				
			minimum_path_len = min(len(rp) for rp in rel_paths)
			rel_paths_with_min_len = (rp for rp in rel_paths if len(rp) in minimum_path_len)

	def get_relation(self, relative): # taslak
		current = self
		path = []
		while not current == relative:
			first_degree_relatives = self.get_first_degree_relatives()
			path.append(self)

			for rel in first_degree_relatives:
				temp_path = copy.deepcopy(path)
				if rel == relative:
					temp_path.append(relative)
					return temp_path



	def bfs_paths(graph, start, goal): # taslak
		start = self		
		queue = [(start, [start])]	
		while queue:
			(vertex, path) = queue.pop(0)
			for next in graph[vertex] - set(path):
				if next == goal:
					yield path + [next]
				else:
					queue.append((next, path + [next]))

		

	def str(self):
		temp = "name={}, surn={}, g={}, bd={}, dd={}, f={}, m={}, s={}, p={}".format(self.name, self.surname, self.gender, self.birthdate, self.deathdate, self.father, self.mother, self.spouse, self.is_placeholder())
		#temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp



def main():
	print ("test")
	Veli 	= Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15), None, None, None)	#Çocuk	
	Ali 	= Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15), None, None, None, Veli) # Baba
	Huri 	= Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15), None, None, Ali, Veli) # Anne
	Deli 	= Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15), Ali, Huri, None) # Çocuk
	
	Ali.set_spouse(Huri)

	Veli.set_mother(Huri)
	Veli.set_father(Ali)

	Ali.add_child(Deli)
	Huri.add_child(Deli)
	


if __name__ == '__main__':
	main()
