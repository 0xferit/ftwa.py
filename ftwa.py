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

	SPOUSE, FATHER, MOTHER, CHILD, SIBLING = range(5)

	def get_reverse(r):
		switcher = {
			1: "x",
			2: "y"
		}

		return switcher.get(r, "")

	def get_reverse2(r):
		if r == self(1):
			return self.CHILD
	

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



	def get_relationship_with(self, relative, path=[], rel_path=[]): #TODO
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



	def bfs_paths(graph, start, goal): #TODO
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

	def del_relation(self, p1: Person, r: Relation, p2: Person): #TODO 
		return	

	def get_first_degree_relatives(self, p: Person):
		temp = []
		for relation in self.relation_list:
			if p in relation:
				if relation[0] == p:
					temp.append(relation[2])
				else:
					temp.append(relation[0])

		return temp

	def list_relations(self):
		for relation in self.relation_list:
			print(relation)
					
	def get_level(self, p: Person): #TODO
		print("diagnosing {}".format(p.name))
		for x in self.relation_list:
			print(x[0].name, x[1].name, x[2].name, x[3].name)
		father_rel = self.get_persons_relations_of_a_kind(p, Relation.FATHER)
		mother_rel = self.get_persons_relations_of_a_kind(p, Relation.MOTHER)
		
		print(len(father_rel))
		for x in father_rel:
			print(x[0].name, x[1].name, x[2].name, x[3].name)		
		
		print(len(mother_rel))
		for x in mother_rel:
			print(x[0].name, x[1].name, x[2].name, x[3].name)


		if not father_rel and not mother_rel:
			print("öksüz {}".format(p.name))
			return 0
		if father_rel and  mother_rel:
			return 1 + max(self.get_level(father_rel[2]), self.get_level(mother_rel[2]))
		if  father_rel and not mother_rel: 
			return 1 + self.get_level(father_rel[2])
		else:
			return 1 + self.get_level(mother_rel[2])

	def get_persons_relations(self, p: Person):
		return [rel for rel in self.relation_list if p in rel]	

	def get_persons_relations_of_a_kind(self, p: Person, r: Relation):
		return [rel for rel in self.get_persons_relations(p) if (rel[1] is r or (rel[2] == (Person.get_reverse_relation(r))))]	## BURDA KALDIM	

def main():
	print ("test")
	Veli 	= Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15))	#Çocuk	
	Ali 	= Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15)) # Baba
	Huri 	= Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15)) # Anne
	Deli 	= Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
	
	G = FamilyGraph()
	G.person_list.append(Veli)
	G.person_list.append(Huri)
	
	G.new_relation(Ali, Relation.SPOUSE, Relation.SPOUSE, Huri)
	G.new_relation(Ali, Relation.CHILD, Relation.FATHER, Veli)
	G.new_relation(Ali, Relation.CHILD, Relation.FATHER, Deli)
	G.new_relation(Huri, Relation.CHILD, Relation.MOTHER, Veli)
	G.new_relation(Huri, Relation.CHILD, Relation.MOTHER, Deli)

	print("FDR:{}".format(G.get_first_degree_relatives(Veli)))

	G.list_relations()
	print(len(G.get_persons_relations(Huri)))
	print(G.get_persons_relations_of_a_kind(Huri, Relation.CHILD))

	#print("here {}".format(Relation.get_reverse(Relation.FATHER)))

	print(Person.get_reverse_relation(Relation.FATHER))

if __name__ == '__main__':
	main()
