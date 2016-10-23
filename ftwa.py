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

	SPOUSE, PARENT, CHILD, SIBLING = range(4)
	
class Gender(Enum):
	MALE, FEMALE = range(2)

class ComplexRelation(Enum):

	OGUL, KIZ, ERKEK_KARDES, KIZ_KARDES, ABLA, AGABEY, AMCA, HALA, DAYI, TEYZE, YEGEN, KUZEN, ENISTE, YENGE, KAYINVALIDE, KAYINPEDER, GELIN, DAMAT, BACANAK, BALDIZ, ELTI, KAYINBIRADER, BABA, ANNE, KARI, KOCA, DEDE, ANNEANNE, BABAANNE, TANIMSIZ, GORUMCE, TORUN = range(32)
	
ILLEGAL_MARRIAGE_RULES =  [ComplexRelation.TEYZE, ComplexRelation.HALA, ComplexRelation.AMCA, ComplexRelation.DAYI, ComplexRelation.DEDE, ComplexRelation.ANNEANNE, ComplexRelation.BABAANNE]

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

	def __init__(self, name=None, surname=None, gender: Gender=None, birthdate: date=None, deathdate: date=None):

		self.name = None
		self.surname = None
		self.gender = None
		self.birthdate = None
		self.deathdate = None

		self.set_gender(gender)
		self.name = name
		self.surname = surname
		self.set_birthdate(birthdate)
		self.set_deathdate(deathdate)

	def set_birthdate(self, d: date):
		
		if not isinstance(d, date):
			if not d == None:
				try:
					date_str = re.split("\.|-",d)
					results = list(map(int, date_str))
					d = date(results[0], results[1], results[2])
				except:
					raise TypeError
			else:
				self.birthdate = None
				return

		if not self.deathdate == None:
			if (self.deathdate -d).days < 0:
				self.birthdate = d
			else:
				print("[ERROR] Deathdate < Birthdate!")
		else:
			self.birthdate = d
			

	def set_deathdate(self, d: date):
		if not isinstance(d, date):
			if not d == None:
				try:
					date_str = re.split("\.|-",d)
					results = list(map(int, date_str))
					d = date(results[0], results[1], results[2])
				except:
					raise TypeError
			else:
				self.deathdate = None
				return

		if not self.birthdate == None:
			if (self.birthdate -d).days < 0:
				self.deathdate = d
			else:
				print("[ERROR] Deathdate < Birthdate!")
		else:
			self.deathdate = d
	
	def set_gender(self, g: Gender):
		if not isinstance(g, Gender):
			try:
				g = Gender[g.upper()]
				self.gender = g
			except:
				self.gender = None
		else:

			self.gender = g


	def set_name(self, name: str):
		self.name = name

	def set_surname(self, surname: str):
		self.surname = surname



	def is_placeholder(self): 
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
		if not self.deathdate:
			return "N/A - Deathdate Record Missing!"
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
		return temp

	def get_reverse_relation(r: Relation):
		if r == Relation.PARENT:
			return Relation.CHILD

		if r == Relation.CHILD:
			return Relation.PARENT

		else:
			return r



class FamilyGraph():
	relation_list = []
	person_list = {}

	def fix_relation_table(self):

		keys = self.person_list.keys()
		items = self.person_list.items()
		pool = []
		todelete = []
		for k, v in self.person_list.items():
			pool.append(v)

		for x in pool:
			print(x.name)

		for rel in self.relation_list:
			if rel[0] not in pool:
				print("0 not in pool {}".format(rel[0].name))
				todelete.append(rel)
			elif rel[3] not in pool:
				print("3 not in pool {}".format(rel[3].name))
				todelete.append(rel)

		self.relation_list = [x for x in self.relation_list if x not in todelete]
				

	def new_relation(self, p1: Person, r1: Relation, r2: Relation, p2: Person):
		if ((not p1.is_placeholder() and p1.get_age() < 18) or (not p2.is_placeholder() and p2.get_age() < 18)) and r1 == Relation.SPOUSE:
			print("[WARNING] Marriage between {} and {} is a child marriage!".format(p1.name, p2.name))

		
		if r1 == Relation.CHILD:
			if not self.is_older_than(p1, p2):
				print("[ERROR] Impossible Birthdates/Deathdates! {} can't be parent of {}".format(p1.name, p2.name))
				return

		if r2 == Relation.CHILD:
			if not self.is_older_than(p2, p1):
				print("[ERROR] Impossible Birthdates/Deathdates! {} can't be parent of {}".format(p2.name, p1.name))
				return

		if r1 == Relation.SPOUSE or r2 == Relation.SPOUSE:
			if self.get_relation_between(p1, p2) in ILLEGAL_MARRIAGE_RULES:
				print("[ERROR] Illegal Marriage! {} can't be spouse of {} because their relation is {}".format(p1.name, p2.name, self.get_relation_between(p1, p2)))
				return

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

		
					
	def get_level(self, p: Person):

		father_rel = self.get_persons_relations_of_a_kind(p, Relation.PARENT)		
		
		father = None

		if father_rel:
			for y in father_rel[0]:
				if y != p and type(y) == type(p):
					father = y
		if not father:
			return 0
		else:
			return 1 + self.get_level(father)

	def get_persons_relations(self, p: Person):

		return [rel for rel in self.relation_list if p in rel]	

	def get_persons_relations_of_a_kind(self, p: Person, r: Relation):
		
		direct = [rel for rel in self.get_persons_relations(p) if rel[1] == r and rel[0] == p]
		reverse = [rel for rel in self.get_persons_relations(p) if rel[2] == r and rel[3] == p]	

	
		if direct:
			return direct
		else:
			return reverse




	def mysearch2(self, start, goal): # finds shortest path between nodes

		path = []
		visited = []

		predecessor = {}
		length = 0
		visit_queue = collections.deque()
		visit_queue.appendleft(start)
		length+=1

		next = visit_queue.pop()
		length-=1
		while next != goal and length > -1:
					
			visited.append(next)
		
			successors = [x for x in self.get_first_degree_relatives(next) if x not in visited+list(collections.deque(visit_queue))]

			visit_queue.extendleft(successors)
			length += len(successors)
			for s in successors:
				predecessor[s] = next

			if length > 0:
				next = visit_queue.pop()
			
			else:
				return []
			length-=1

			

		
		path.append(next)
		found = copy.deepcopy(next)

		while next in predecessor:
			path.append(predecessor[next])			
			next = predecessor[next]
			
		path.reverse()		
	
		return path

	def node_path_to_edge_path(self, path):
		relation_path = []
		for x in range(1, len(path)):

			relations1 = self.get_persons_relations(path[x-1])


			relations2 = self.get_persons_relations(path[x])


			c3 = list(set(relations1).intersection(relations2))
			
			if path[x-1] == c3[0][0]:
				relation_path.append(c3[0][1])
			else:
				relation_path.append(c3[0][2])
		return relation_path
	
	
	def translate_path_to_relation(self, relation_path, nodes):


#------------------------1. DEGREE RELATIONS------------------------------------

		if len(relation_path) == 1:

			if relation_path[0] == Relation.SIBLING:
				if nodes[1].gender == Gender.MALE:
					if  self.is_older_than(nodes[0], nodes[1]):
						return ComplexRelation.ERKEK_KARDES
					else:
						return ComplexRelation.AGABEY
				else:
					if  self.is_older_than(nodes[0], nodes[1]):
						return ComplexRelation.KIZ_KARDES
					else:
						return ComplexRelation.ABLA

			if relation_path[0] == Relation.PARENT:
				if nodes[1].gender == Gender.MALE:
					return ComplexRelation.BABA
				else:
					return ComplexRelation.ANNE

			if relation_path[0] == Relation.SPOUSE:
				if nodes[1].gender == Gender.MALE:
					return ComplexRelation.KOCA
				else:
					return ComplexRelation.KARI


			if relation_path[0] == Relation.CHILD:
				if nodes[1].gender == Gender.MALE:
					return ComplexRelation.OGUL
				else:
					return ComplexRelation.KIZ

#------------------------2. DEGREE RELATIONS------------------------------------

		if len(relation_path) == 2:
			
			
			if relation_path[0] == Relation.SIBLING:
				if nodes[0].gender == Gender.FEMALE:
					if nodes[1].gender == Gender.MALE:
						if relation_path[1] == Relation.SPOUSE:
							if nodes[2].gender == Gender.FEMALE:
								return ComplexRelation.ELTI
					else:
						if relation_path[1] == Relation.CHILD:
							return ComplexRelation.YEGEN
				else:
					if nodes[1].gender == Gender.MALE:

						if relation_path[1] == Relation.SPOUSE:
							if nodes[2].gender == Gender.MALE:
								return ComplexRelation.TANIMSIZ
							else:
								return ComplexRelation.YENGE

						if relation_path[1] == Relation.PARENT:

							if nodes[2].gender == Gender.MALE:

								return ComplexRelation.TANIMSIZ
							else:
								return ComplexRelation.TANIMSIZ

						if relation_path[1] == Relation.CHILD:
							return ComplexRelation.YEGEN
						
					if nodes[1].gender == Gender.FEMALE:

						if relation_path[1] == Relation.SPOUSE:

							if nodes[2].gender == Gender.MALE:
								return ComplexRelation.ENISTE
							else:
								return ComplexRelation.TANIMSIZ


						if relation_path[1] == Relation.CHILD:
							return ComplexRelation.YEGEN



#----------------------------------------------------------------------------------------

			if relation_path[0] == Relation.PARENT:

				if nodes[1].gender == Gender.MALE:

					if relation_path[1] == Relation.SIBLING:
						if nodes[2].gender == Gender.MALE:

							return ComplexRelation.AMCA
						else:
							return ComplexRelation.HALA

					if relation_path[1] == Relation.PARENT:
						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.DEDE
						else:
							return ComplexRelation.BABAANNE
						
				if nodes[1].gender == Gender.FEMALE:
					if relation_path[1] == Relation.SIBLING:
						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.DAYI
						else:
							return ComplexRelation.TEYZE
					if relation_path[1] == Relation.PARENT:
						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.DEDE
						else:
							return ComplexRelation.ANNEANNE

#--------------------------------------------------------------------------------------

			if relation_path[0] == Relation.SPOUSE:

				if nodes[1].gender == Gender.MALE:

					if relation_path[1] == Relation.PARENT:

						if nodes[2].gender == Gender.MALE:

							return ComplexRelation.KAYINPEDER
						else:
							return ComplexRelation.KAYINVALIDE

					if relation_path[1] == Relation.SIBLING:

						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.TANIMSIZ
						else:
							return ComplexRelation.GORUMCE
						
				if nodes[1].gender == Gender.FEMALE:

					if relation_path[1] == Relation.SIBLING:

						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.KAYINBIRADER
						else:
							return ComplexRelation.BALDIZ

					if relation_path[1] == Relation.PARENT:

						if nodes[2].gender == Gender.MALE:
							return ComplexRelation.KAYINPEDER
						else:
							return ComplexRelation.KAYINVALIDE

#--------------------------------------------------------------------------------------


			if relation_path[0] == Relation.CHILD:

				if relation_path[1] == Relation.CHILD:
					return ComplexRelation.TORUN
				if relation_path[1] == Relation.SPOUSE:
					if nodes[2].gender == Gender.MALE:
						return ComplexRelation.DAMAT
					else:
						return ComplexRelation.GELIN

#------------------------3. DEGREE RELATIONS-------------------------------------------

		if len(relation_path) == 3:

			if relation_path[0] == Relation.PARENT:

				if relation_path[1] == Relation.SIBLING:

					if relation_path[2] == Relation.CHILD:
						return ComplexRelation.KUZEN

			if nodes[0].gender == Gender.MALE:
				if relation_path[0] == Relation.SPOUSE:
					if nodes[1].gender == Gender.FEMALE:
						if relation_path[1] == Relation.SIBLING:
							if nodes[2].gender == Gender.FEMALE:
								if relation_path[2] == Relation.SPOUSE:
									return ComplexRelation.BACANAK	
		
			

		else:
			return ComplexRelation.TANIMSIZ
		




	def get_relation_between(self, p1: Person, p2: Person):
		path = self.mysearch2(p1, p2)
		rel_path = self.node_path_to_edge_path(path)
		complex_rel = self.translate_path_to_relation(rel_path, path)
		
		return complex_rel

	def is_older_than(self, p1, p2): 
		if(p1.birthdate == None):
			return False
		if(p2.birthdate == None):
			return True
		
		bd1 = p1.birthdate
		bd2 = p2.birthdate
		return (0 > (bd1.year - bd2.year - ((bd1.month, bd1.day) < (bd2.month, bd2.day))))
		


def main():
	Veli 	= Person("Veli", "Yanyatan",   Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
	Ali 	= Person("Ali", "Yanyatan",    Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) # Baba
	Huri 	= Person("Huri", "Yanyatan", Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) # Anne
	Deli 	= Person("Deli", "Yanyatan",   Gender.MALE, date(1999, 12, 15), date(2075, 12, 15)) # Çocuk
	Riza	= Person("Riza", "Yanyatan",   Gender.MALE, date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası
	Fatmagul= Person("Fatmagül", "Yanyatan", Gender.FEMALE, birthdate = date(1999, 1, 1))
	Makbule = Person("Makbule", "Yanyatan", Gender.FEMALE, date(1945,1,1))
	Nuri	= Person("Nuri", "Yanyatan", Gender.MALE)
	Nurbanu	= Person("Nurbanu", "Yanyatan", Gender.FEMALE)
	Asli	= Person("Asli",  "Yanyatan", Gender.FEMALE, date(1966,1,1))
	Kerem	= Person("Kerem", "Yanyatan", Gender.MALE)
	Mahmut	= Person("Mahmut", "Devrik", Gender.MALE, date(1950,1,1))
	Emre	= Person("Emre", "Bitmez", Gender.MALE)
	Cimcime = Person("Cimcime", "Yanyatan", Gender.FEMALE, date(1999,1,1))
	Pamela	= Person("Pamela", "Canisi", Gender.FEMALE, date(1950,1,1))
	Duran	= Person("Duran", "Yanyatan", Gender.MALE)

	G = FamilyGraph()

	G.person_list[Veli.name+Veli.surname] = Veli
	G.person_list[Ali.name+Ali.surname] = Ali
	G.person_list[Huri.name+Huri.surname] = Huri
	G.person_list[Deli.name+Deli.surname] = Deli
	G.person_list[Riza.name+Riza.surname] = Riza
	G.person_list[Fatmagul.name+Fatmagul.surname] = Fatmagul
	G.person_list[Makbule.name+Makbule.surname] = Makbule
	G.person_list[Nuri.name+Nuri.surname] = Nuri
	G.person_list[Nurbanu.name+Nurbanu.surname] = Nurbanu
	G.person_list[Asli.name+Asli.surname] = Asli
	G.person_list[Kerem.name+Kerem.surname] = Kerem
	G.person_list[Mahmut.name+Mahmut.surname] = Mahmut
	G.person_list[Emre.name+Emre.surname] = Emre
	G.person_list[Cimcime.name+Cimcime.surname] = Cimcime
	G.person_list[Pamela.name+Pamela.surname] = Pamela
	G.person_list[Duran.name+Duran.surname] = Duran


	G.new_relation(Ali, Relation.SPOUSE, Relation.SPOUSE, Huri)
	G.new_relation(Ali, Relation.CHILD, Relation.PARENT, Veli)
	G.new_relation(Ali, Relation.CHILD, Relation.PARENT, Deli)
	G.new_relation(Huri, Relation.CHILD, Relation.PARENT, Veli)
	G.new_relation(Huri, Relation.CHILD, Relation.PARENT, Deli)
	G.new_relation(Veli, Relation.SIBLING, Relation.SIBLING, Deli)
	G.new_relation(Riza, Relation.CHILD, Relation.PARENT, Ali)
	G.new_relation(Deli, Relation.SPOUSE, Relation.SPOUSE, Fatmagul)
	G.new_relation(Nuri, Relation.SIBLING, Relation.SIBLING, Ali)
	G.new_relation(Nurbanu, Relation.SIBLING, Relation.SIBLING, Ali)
	G.new_relation(Asli, Relation.SIBLING, Relation.SIBLING, Huri)
	G.new_relation(Kerem, Relation.SIBLING, Relation.SIBLING, Huri)
	G.new_relation(Makbule, Relation.CHILD, Relation.PARENT, Ali)
	G.new_relation(Mahmut, Relation.CHILD, Relation.PARENT, Huri)
	G.new_relation(Emre, Relation.SPOUSE, Relation.SPOUSE, Asli)
	G.new_relation(Cimcime, Relation.PARENT, Relation.CHILD, Asli)
	G.new_relation(Pamela, Relation.CHILD, Relation.PARENT, Huri)
	G.new_relation(Duran, Relation.SPOUSE, Relation.SPOUSE, Asli)

	print("AA")
	print("ggggg {}".format(G.get_relation_between(Huri, Deli)))
	print("ggggg {}".format(G.get_relation_between(Huri, Fatmagul)))
	print("ggggg {}".format(G.get_relation_between(Deli, Fatmagul)))
	print("ggggg {}".format(G.get_relation_between(Fatmagul, Deli)))

if __name__ == '__main__':
	main()
