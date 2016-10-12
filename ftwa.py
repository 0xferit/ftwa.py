#!/usr/bin/python3

import sys #sys library is importing
import time
import os.path
import argparse
import re
import locale
from enum import Enum
from datetime import date
	
	
class Relation(Enum):
	SPOUSE, FATHER, MOTHER, CHILD = range(4)
		

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
		self.mother = mother
		self.children = [children]
		self.spouse = spouse


	def add_child(self, person):
		temp_tuple = [person]
		self.children.append(temp_tuple)

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
		return temp + temp2
	
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
		temp = "name={}, surn={}, g={}, bd={}, dd={}, f={}, m={}, p={}".format(self.name, self.surname, self.gender, self.birthdate, self.deathdate, self.father, self.mother, self.is_placeholder)
		temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp + temp2



def main():
	print ("test")
	Veli = Person("veli", "deli", "male", date.today(), date.today(), "o", None)
	Veli2 = Person("veli2", "deli", "male", date.today(), date.today(), None, None)
	Ali = Person("ali", "deli", "male", date.today(), date.today(), None, None, None, Veli, Veli2)
	Fitnat = Person("fitnat", "deli", "female", date.today(), date.today(), None, None, Ali, Veli, Veli2)
	Ali.set_spouse(Fitnat)
	asda = Person(name="veledizina")

	print(asda.str())
	print(asda.gender == True)

	#print(Veli.mother.gender)
	print(Fitnat.str())
	#print(type(Fitnat.children))
	Fitnat.add_child(asda)
	print(Fitnat.str())

	#print("Relation F to A:{}".format(Fitnat.get_relationship_with(Ali)))
	#print("Relation F to V:{}".format(Fitnat.get_relationship_with(Veli)))


if __name__ == '__main__':
	main()
