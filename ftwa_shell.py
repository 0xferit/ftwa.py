#!/usr/bin/python3

import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt
import ftwa
from datetime import date
import collections
import re
import sys
import logging

class HelloWorld(cmd.Cmd):
		
	intro = """Family Tree Warehouse Application 0.1\nWelcome to ftwa shell! Type help or ? to list commands."""
	prompt = "(ftwa) "

	G = ftwa.FamilyGraph()

	def do_load_test_data(self, arg):
		"Loads an hardcoded family graph for testing"

		ATTRIBUTE_NAMES = ["name", "surname", "gender", "birthdate", "deathdate"] 
	
		Veli 	= ftwa.Person("Veli", "Yanyatan",   ftwa.Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
		Ali 	= ftwa.Person("Ali", "Yanyatan",    ftwa.Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) # Baba
		Huri 	= ftwa.Person("Huri", "Yanyatan", ftwa.Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) # Anne
		Deli 	= ftwa.Person("Deli", "Yanyatan",   ftwa.Gender.MALE, date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
		Riza	= ftwa.Person("Riza", "Yanyatan",   ftwa.Gender.MALE, date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası
		Fatmagul= ftwa.Person("Fatmagül", "Yanyatan", ftwa.Gender.FEMALE, birthdate = date(2000, 1, 1))
		Makbule = ftwa.Person("Makbule", "Yanyatan", ftwa.Gender.FEMALE, date(1945,1,1))
		Nuri	= ftwa.Person("Nuri", "Yanyatan", ftwa.Gender.MALE)
		Nurbanu	= ftwa.Person("Nurbanu", "Yanyatan", ftwa.Gender.FEMALE)
		Asli	= ftwa.Person("Asli",  "Yanyatan", ftwa.Gender.FEMALE, date(1966,1,1))
		Kerem	= ftwa.Person("Kerem", "Yanyatan", ftwa.Gender.MALE)
		Mahmut	= ftwa.Person("Mahmut", "Devrik", ftwa.Gender.MALE, date(1950,1,1))
		Emre	= ftwa.Person("Emre", "Bitmez", ftwa.Gender.MALE)
		Cimcime = ftwa.Person("Cimcime", "Yanyatan", ftwa.Gender.FEMALE, date(1999,1,1))
		Pamela	= ftwa.Person("Pamela", "Canisi", ftwa.Gender.FEMALE, date(1950,1,1))
		Duran	= ftwa.Person("Duran", "Yanyatan", ftwa.Gender.MALE)



		self.G.person_list[Veli.name+Veli.surname] = Veli
		self.G.person_list[Ali.name+Ali.surname] = Ali
		self.G.person_list[Huri.name+Huri.surname] = Huri
		self.G.person_list[Deli.name+Deli.surname] = Deli
		self.G.person_list[Riza.name+Riza.surname] = Riza
		self.G.person_list[Fatmagul.name+Fatmagul.surname] = Fatmagul
		self.G.person_list[Makbule.name+Makbule.surname] = Makbule
		self.G.person_list[Nuri.name+Nuri.surname] = Nuri
		self.G.person_list[Nurbanu.name+Nurbanu.surname] = Nurbanu
		self.G.person_list[Asli.name+Asli.surname] = Asli
		self.G.person_list[Kerem.name+Kerem.surname] = Kerem
		self.G.person_list[Mahmut.name+Mahmut.surname] = Mahmut
		self.G.person_list[Emre.name+Emre.surname] = Emre
		self.G.person_list[Cimcime.name+Cimcime.surname] = Cimcime
		self.G.person_list[Pamela.name+Pamela.surname] = Pamela
		self.G.person_list[Duran.name+Duran.surname] = Duran


		self.G.new_relation(Ali, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Huri)
		self.G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
		self.G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
		self.G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
		self.G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
		self.G.new_relation(Veli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Deli)
		self.G.new_relation(Riza, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali)
		self.G.new_relation(Deli, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Fatmagul)
		self.G.new_relation(Nuri, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali)
		self.G.new_relation(Nurbanu, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali)
		self.G.new_relation(Asli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
		self.G.new_relation(Kerem, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
		self.G.new_relation(Makbule, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali)
		self.G.new_relation(Mahmut, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		self.G.new_relation(Emre, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)
		self.G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Asli)
		self.G.new_relation(Pamela, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		self.G.new_relation(Duran, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)



	def do_create(self, arg):
		"Creates person\nUsage: create <name> <surname> <gender> <birthdate> <deathdate> name and surname mandatory\nExamples: create Ali Durmaz\ncreate name=Ali surname=Durmaz birthdate=1999.1.1"
		print(*parse(arg))
		temp = ftwa.Person(*parse(arg))
		print(temp.str())
		self.G.person_list[temp.name+temp.surname] = temp

	def do_search(self, arg):
		"Search and retrieve information of a person\nUsage: search <person>"
		try:
			print(self.G.person_list[parse(arg)[0]].str())
		except:
			print("Not Found!")

	def complete_search(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions


	def do_list(self, arg):
		"Lists persons and their informations\nUsage: <list>"
		for k, v in self.G.person_list.items():
			print(k, v.str())
		print("{} record".format(len(self.G.person_list)))
	
	def do_relation(self, arg):
		"Prints relation between two persons\nUsage: relation <person1> <person2>"
		print(self.G.get_relation_between(self.G.person_list[parse(arg)[0]], self.G.person_list[parse(arg)[1]]))

	def complete_relation(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions

	def do_relate(self, arg):
		"Adds new primitive relation (CHILD, PARENT, SIBLING, SPOUSE)\nUsage: relate <person1> <person2> <relation1>"
		person1str = parse(arg)[0]
		person2str = parse(arg)[1]
		relationstr = parse(arg)[2].upper()

		try:
			self.G.new_relation(self.G.person_list[person1str], ftwa.Relation[relationstr], ftwa.Person.get_reverse_relation(ftwa.Relation[relationstr]), self.G.person_list[person2str])

		except:
			print("[ERROR] Failed To Add Relation!")



	def complete_relate(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions
		
	
	def do_alive(self, arg):
		"Lets you know where the person is dead or alive\nUsage: alive <person>"
		
		print(self.G.person_list[parse(arg)[0]].is_alive())

	def do_list_relations(self, arg):
		"Lists relations"
		for relation in self.G.relation_list:
			print(relation[0].name, relation[1], relation[2], relation[3].name)

		print("{} record".format(len(self.G.relation_list)))

	def complete_list_relations(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions


	def complete_alive(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions	

	def do_delete(self, arg):
		"Search and delete person and it's relations\nUsage: delete <person>"

		del self.G.person_list[parse(arg)[0]]
		self.G.fix_relation_table()

	def complete_delete(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions

	def do_update(self, arg):
		"Updates name, surname, gender, birthdate or deathdate.\nUsage: update <person> <field> <new_value>\nExample: update AliYanyatan gender female"
		if parse(arg)[1] == "name":
			self.G.person_list[parse(arg)[0]].set_name(parse(arg)[1])

		if parse(arg)[1] == "surname":
			self.G.person_list[parse(arg)[0]].set_surname(parse(arg)[1])

		if parse(arg)[1] == "gender":

				self.G.person_list[parse(arg)[0]].set_gender(parse(arg)[2])


		if parse(arg)[1] == "birthdate":

			self.G.person_list[parse(arg)[0]].set_birthdate(parse(arg)[2])

		if parse(arg)[1] == "deathdate":

			self.G.person_list[parse(arg)[0]].set_deathdate(parse(arg)[2])


	def complete_update(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions		

	def do_age(self, arg):
		"Get age of person\nUsage: age <person>"
		try:
			print(self.G.person_list[parse(arg)[0]].get_age())
		except:
			print("Not Found!")	

	def complete_age(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions

	def do_level(self, arg):
		"Get level of person. Returns longest parental path distance\nUsage: level <person>"
		try:
			print(self.G.get_level(self.G.person_list[parse(arg)[0]]))
		except:
			print("Not Found!")	

	def complete_level(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions


	
	def do_print(self, arg):
		"Visualizes the family graph\nUsage: print"

		labels2 = {}
		
		edgelabels2 = collections.OrderedDict()

		Y=nx.DiGraph()


		for k, v in self.G.person_list.items():
			try:
				Y.nodes().index(v.name + v.surname)
			except:
				Y.add_node(v.name + v.surname)
				labels2[v.name + v.surname] = v.name + v.surname

		for rel in self.G.relation_list:
			try:
				Y.edges().index(rel[0].name+rel[0].surname, rel[3].name+rel[3].surname)
			except:
				Y.add_edge(rel[0].name+rel[0].surname, rel[3].name+rel[3].surname)
				edgelabels2[rel[0].name+rel[0].surname, rel[3].name+rel[3].surname] = r'${}$'.format(rel[1].name)
		

		
		pos=nx.spring_layout(Y)



		nx.draw_networkx(G=Y, pos=pos, labels=labels2, font_size=16) # FONT SIZE BURAYA OLMUYO
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2)
		
		#plt.axis("off")
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_exit(self, line):
		"Exits from ftwa shell"
		return True

	def do_EOF(self, arg):
		"CTRL+D  interrupt"
		return True

def parse(arg):
	return arg.split()


if __name__ == '__main__':

	HelloWorld().cmdloop()
