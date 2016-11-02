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
import copy

class HelloWorld(cmd.Cmd):
		
	intro = """Family Tree Warehouse Application 0.1\nWelcome to ftwa shell! Type help or ? to list commands."""
	prompt = "(ftwa) "

	G = ftwa.FamilyGraph()

	def do_load_test_data(self, arg):
		"Loads the test graph"

		ATTRIBUTE_NAMES = ["name", "surname", "gender", "birthdate", "deathdate"] 
	
		Veli 	= ftwa.Person("Veli", "Sensoy",   ftwa.Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) 	
		Ferhan 	= ftwa.Person("Ferhan", "Sensoy",    ftwa.Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) 
		Huri 	= ftwa.Person("Huri", "Sensoy", ftwa.Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) 
		Deli 	= ftwa.Person("Deli", "Sensoy",   ftwa.Gender.MALE, date(2007, 12, 15), date(2075, 12, 15)) 
		Riza	= ftwa.Person("Riza", "Sensoy",   ftwa.Gender.MALE, date(1950, 1, 1), date(2030, 12, 12)) 
		Fatmagul= ftwa.Person("Fatmagül", "Sensoy", ftwa.Gender.FEMALE, birthdate = date(2000, 1, 1))
		Makbule = ftwa.Person("Makbule", "Sensoy", ftwa.Gender.FEMALE, date(1945,1,1))
		Nuri	= ftwa.Person("Nuri", "Camurabatti", ftwa.Gender.MALE, date(1981,1,1))
		Nurbanu	= ftwa.Person("Nurbanu", "Camurabatti", ftwa.Gender.FEMALE, date(1982,1,1))

		Asli	= ftwa.Person("Asli",  "Durdiyen", ftwa.Gender.FEMALE, date(1966,1,1))
		Kerem	= ftwa.Person("Kerem", "Durdiyen", ftwa.Gender.MALE)
		Mahmut	= ftwa.Person("Mahmut", "Kosasimyok", ftwa.Gender.MALE, date(1950,1,1))
		Emre	= ftwa.Person("Emre", "Durdiyen", ftwa.Gender.MALE, date(1966,1,1))
		Cimcime = ftwa.Person("Cimcime", "Durdiyen", ftwa.Gender.FEMALE, date(1999,1,1))
		Aynur	= ftwa.Person("Aynur", "Kosasimyok", ftwa.Gender.FEMALE, date(1950,1,1))




		self.G.person_list[Veli.name+Veli.surname] = Veli
		self.G.person_list[Ferhan.name+Ferhan.surname] = Ferhan
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
		self.G.person_list[Aynur.name+Aynur.surname] = Aynur



		self.G.new_relation(Ferhan, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Huri)
		self.G.new_relation(Ferhan, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
		self.G.new_relation(Ferhan, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
		self.G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
		self.G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
		self.G.new_relation(Veli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Deli)
		self.G.new_relation(Riza, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ferhan)
		self.G.new_relation(Deli, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Fatmagul)
		self.G.new_relation(Nuri, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ferhan)
		self.G.new_relation(Nurbanu, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ferhan)
		self.G.new_relation(Asli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
		self.G.new_relation(Kerem, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Huri)
		self.G.new_relation(Makbule, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ferhan)
		self.G.new_relation(Mahmut, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		#self.G.new_relation(Emre, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)
		self.G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Asli)
		self.G.new_relation(Aynur, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		self.G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Emre)
		self.G.new_relation(Nuri, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Makbule)
		self.G.new_relation(Nurbanu, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Riza)




	def do_create(self, arg):
		"Creates person\nUsage: create <name> <surname> <gender> <birthdate> <deathdate>\nName and surname mandatory\nExamples: create Ali Durmaz\n\tcreate name=Ali surname=Durmaz birthdate=1999.1.1"
		print(type(arg))		
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

	def do_placeholder(self, arg):
		"Queries if a person is a placeholder\nUsage: placeholder <person>"
		print(self.G.person_list[parse(arg)[0]].is_placeholder())

	def complete_placeholder(self, text, line, begidx, endidx):
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
			self.G.person_list[parse(arg)[0]].set_name(parse(arg)[2])
			self.G.person_list[self.G.person_list[parse(arg)[0]].name+self.G.person_list[parse(arg)[0]].surname] = self.G.person_list[parse(arg)[0]]
			del self.G.person_list[parse(arg)[0]]


		if parse(arg)[1] == "surname":
			self.G.person_list[parse(arg)[0]].set_surname(parse(arg)[2])
			self.G.person_list[self.G.person_list[parse(arg)[0]].name+self.G.person_list[parse(arg)[0]].surname] = self.G.person_list[parse(arg)[0]]
			del self.G.person_list[parse(arg)[0]]

		if parse(arg)[1] == "gender":

			self.G.person_list[parse(arg)[0]].set_gender(parse(arg)[2])


		if parse(arg)[1] == "birthdate":

			temp_person = copy.deepcopy(self.G.person_list[parse(arg)[0]])
			temp_person.set_birthdate(parse(arg)[2])


			for relation in self.G.get_persons_relations_of_a_kind(self.G.person_list[parse(arg)[0]], ftwa.Relation.PARENT):
				if (relation[3].birthdate - temp_person.birthdate).days > 0:
					print ("You can't set birthdate older than parents birthdate")
					return


			for relation in self.G.get_persons_relations_of_a_kind(self.G.person_list[parse(arg)[0]], ftwa.Relation.CHILD):
				if (relation[3].birthdate - temp_person.birthdate).days < 0:
					print ("You can't set birthdate younger than children birthdate")
					return


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
		if len(parse(arg)) > 0:
			if parse(arg)[0] == "circular":
				pos=nx.circular_layout(Y)
			if parse(arg)[0] == "spectral":
				pos = nx.spectral_layout(Y)
			if parse(arg)[0] == "random":
				pos = nx.random_layout(Y)



		plt.title("Family Graph")
		nx.draw_networkx(G=Y, pos=pos, labels=labels2, font_size=14)
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2)
		#nx.draw_circular(Y)
		
		#plt.axis("off")
		#plt.savefig("family_graph.png") # save as png
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
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
