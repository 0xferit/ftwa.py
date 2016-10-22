#!/usr/bin/python3

import sys #sys library is importing
import time
import os.path
import argparse
import re
import locale
from enum import Enum
from datetime import date
import collections
import copy
	

class MetaPerson(type):
    def __iter__(self):
        for attr in dir(Person):
            if not attr.startswith("__"):
                yield attr
	
class Relation(Enum):

	SPOUSE, FATHER, MOTHER, CHILD, SIBLING = range(5)

	

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

	def __init__(self, name=None, surname=None, gender=None, birthdate: date=None, deathdate: date=None):

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



	def is_placeholder(self): #We agreed that the missing information as placeholder
		if self.name and self.surname and self.gender and self.birthdate:
			return False
		else:
			return True


	
	def get_age(self):
		today = date.today()
		birthdate = self.birthdate
		return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

	def is_alive(self): 
		today = date.today()
		deathdate = self.deathdate
		return (0 > (today.year - deathdate.year - ((today.month, today.day) < (deathdate.month, deathdate.day))))



	def get_relation(self, relative): #TODO
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

		

	def str(self):
		temp = "name={}, surn={}, g={}, bd={}, dd={}, p={}".format(self.name, self.surname, self.gender, self.birthdate, self.deathdate, self.is_placeholder())
		#temp2 = " - children %s" % ', '.join(str(e.name) for e in self.children)
		return temp

	def get_reverse_relation(r: Relation):
		if r == Relation.FATHER:
			return Relation.CHILD
		if r == Relation.MOTHER:
			return Relation.CHILD



class FamilyGraph():
	relation_list = []
	person_list = []

	def new_relation(self, p1: Person, r1: Relation, r2: Relation, p2: Person):
		self.relation_list.append((p1, r1, r2, p2))

	def del_relation(self, p1: Person, r: Relation, r2: Relation, p2: Person): #TODO 
		return	

	def get_first_degree_relatives(self, p: Person):
		temp = []
		for relation in self.relation_list:
			if p in relation:
				if relation[0] == p:
					temp.append(relation[3])
				else:
					temp.append(relation[0])

		return temp

	def list_relations(self):
		for relation in self.relation_list:
			print(relation)
					
	def get_level(self, p: Person): #TODO

		print("------\ndiagnosing {}".format(p.name))
		for x in self.relation_list:
			print(x[0].name, x[1].name, x[2].name, x[3].name)
		father_rel = self.get_persons_relations_of_a_kind(p, Relation.FATHER)
		mother_rel = self.get_persons_relations_of_a_kind(p, Relation.MOTHER)
		
		print("FATHER REL LEN {}".format(len(father_rel)))
		for x in father_rel:
			print(x[0].name, x[1].name, x[2].name, x[3].name)		
		
		print("MOTHER REL LEN {}".format(len(mother_rel)))
		for x in mother_rel:
			print(x[0].name, x[1].name, x[2].name, x[3].name)
		
		father = None
		mother = None

		if father_rel:
			for y in father_rel[0]:
				if y != p and type(y) == type(p):
					father = y
		
		if mother_rel:
			for y in mother_rel[0]:
				if y != p and type(y) == type(p):
					mother = y



		if not father and not mother:
			print("öksüz {}".format(p.name))
			return 0
		if father and  mother:
			return 1 + max(self.get_level(father), self.get_level(mother))
		if  father and not mother: 
			return 1 + self.get_level(father)
		else:
			return 1 + self.get_level(mother)

	def get_persons_relations(self, p: Person):
		#for item in [rel for rel in self.relation_list if p in rel]: print("X {}".format(item))
		#print("exit")
		return [rel for rel in self.relation_list if p in rel]	

	def get_persons_relations_of_a_kind(self, p: Person, r: Relation):
		
		direct = [rel for rel in self.get_persons_relations(p) if rel[1] == r and rel[0] == p]
		reverse = [rel for rel in self.get_persons_relations(p) if rel[2] == r and rel[3] == p]	

	
		if direct:
			return direct
		else:
			return reverse




	def mysearch2(self, start, goal): # finds and returns goal

		path = []
		visited = []

		predecessor = {}

		visit_queue = collections.deque()
		visit_queue.appendleft(start)
		next = visit_queue.pop()

		while next != goal:
					
			visited.append(next)
		
			successors = [x for x in self.get_first_degree_relatives(next) if x not in visited+list(collections.deque(visit_queue))]

			visit_queue.extendleft(successors)

			for s in successors:
				predecessor[s] = next
			next = visit_queue.pop()

		
		path.append(next)
		found = copy.deepcopy(next)

		while next in predecessor:
			path.append(predecessor[next])			
			next = predecessor[next]
			
				
		return path

	
		

def main():
	print ("test")
	Veli 	= Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15))	#Çocuk	
	Ali 	= Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15)) # Baba
	Huri 	= Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15)) # Anne
	Deli 	= Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
	Rıza	= Person("Rıza", "Yanyatan",   "male", date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası

	X 	= Person(name="X", surname="X")
	Y	= Person(name="Y", surname="Y")
	Z	= Person(name="Z", surname="Z")
	
	G = FamilyGraph()
	G.person_list.append(Veli)
	G.person_list.append(Huri)
	G.person_list.append(Deli)
	G.person_list.append(Ali)
	G.person_list.append(Rıza)

	
	G.person_list.append(X)
	G.person_list.append(Y)
	G.person_list.append(Z)
	
	G.new_relation(Ali, Relation.SPOUSE, Relation.SPOUSE, Huri)
	G.new_relation(Ali, Relation.CHILD, Relation.FATHER, Veli)
	G.new_relation(Ali, Relation.CHILD, Relation.FATHER, Deli)
	G.new_relation(Huri, Relation.CHILD, Relation.MOTHER, Veli)
	G.new_relation(Huri, Relation.CHILD, Relation.MOTHER, Deli)
	G.new_relation(Veli, Relation.SIBLING, Relation.SIBLING, Deli)
	G.new_relation(Rıza, Relation.CHILD, Relation.FATHER, Ali)
	
	G.new_relation(Rıza, Relation.CHILD, Relation.FATHER, X)
	G.new_relation(X, Relation.CHILD, Relation.FATHER, Y)
	G.new_relation(Deli, Relation.CHILD, Relation.FATHER, Z)
	


	print("FDR:{}".format(G.get_first_degree_relatives(Veli)))

	G.list_relations()
	print(len(G.get_persons_relations(Huri)))
	print(G.get_persons_relations_of_a_kind(Huri, Relation.CHILD))

	#print("here {}".format(Relation.get_reverse(Relation.FATHER)))

	print(Person.get_reverse_relation(Relation.FATHER))


	print("----------")
	#print (G.mysearch2(Rıza, Z).name)
	for x in G.mysearch2(Rıza, Rıza):
		print(x.name)

if __name__ == '__main__':
	main()
