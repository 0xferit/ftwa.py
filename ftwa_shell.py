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

class FTWA(cmd.Cmd):
		
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
		Fatmagul= ftwa.Person("Fatmagul", "Sensoy", ftwa.Gender.FEMALE, birthdate = date(2000, 1, 1))
		Makbule = ftwa.Person("Makbule", "Huyuguzel", ftwa.Gender.FEMALE, date(1945,1,1))
		Nuri	= ftwa.Person("Nuri", "Camurabatti", ftwa.Gender.MALE, date(1981,1,1))
		Nurbanu	= ftwa.Person("Nurbanu", "Sensoy", ftwa.Gender.FEMALE, date(1982,1,1))

		Asli	= ftwa.Person("Asli",  "Kosasimyok", ftwa.Gender.FEMALE, date(1966,1,1))
		Kerem	= ftwa.Person("Kerem", "Kalkmayan", ftwa.Gender.MALE, date(1978,1,1))
		Mahmut	= ftwa.Person("Mahmut", "Kosasimyok", ftwa.Gender.MALE, date(1950,1,1))
		Emre	= ftwa.Person("Emre", "Durdiyen", ftwa.Gender.MALE, date(1966,1,1))
		Cimcime = ftwa.Person("Cimcime", "Durdiyen", ftwa.Gender.FEMALE, date(1999,1,1))
		Aynur	= ftwa.Person("Aynur", "Kosasimyok", ftwa.Gender.FEMALE, date(1950,1,1))

		Aynur2= ftwa.Person("Aynur", "Kosasimyok")


		self.G.person_list[Veli.uid] = Veli
		self.G.person_list[Ferhan.uid] = Ferhan
		self.G.person_list[Huri.uid] = Huri
		self.G.person_list[Deli.uid] = Deli
		self.G.person_list[Riza.uid] = Riza
		self.G.person_list[Fatmagul.uid] = Fatmagul
		self.G.person_list[Makbule.uid] = Makbule
		self.G.person_list[Nuri.uid] = Nuri
		self.G.person_list[Nurbanu.uid] = Nurbanu
		self.G.person_list[Asli.uid] = Asli
		self.G.person_list[Kerem.uid] = Kerem
		self.G.person_list[Mahmut.uid] = Mahmut
		self.G.person_list[Emre.uid] = Emre
		self.G.person_list[Cimcime.uid] = Cimcime
		self.G.person_list[Aynur.uid] = Aynur
		
		self.G.person_list[Aynur2.uid] = Aynur2


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

		self.G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Asli)
		self.G.new_relation(Aynur, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		self.G.new_relation(Cimcime, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Emre)
		self.G.new_relation(Nuri, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Makbule)
		self.G.new_relation(Nurbanu, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Riza)

		self.G.new_relation(Kerem, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Aynur)
		self.G.new_relation(Asli, ftwa.Relation.PARENT, ftwa.Relation.CHILD, Mahmut)

		self.G.new_relation(Kerem, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Aynur2	)

	def do_load_demo_data(self, arg):
		"For DEMO"

		Ayşe 	= ftwa.Person("Ayşe", 	gender=ftwa.Gender.FEMALE,	birthdate =date(1925, 1, 1)) 
		Erdem 	= ftwa.Person("Erdem", 	gender=ftwa.Gender.MALE, 	birthdate =date(1920, 1, 1)) 
		Erdi 	= ftwa.Person("Erdi", 	gender=ftwa.Gender.MALE, 	birthdate =date(1950, 1, 1)) 
		Sibel 	= ftwa.Person("Sibel", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1949, 1, 1)) 
		Seda	= ftwa.Person("Seda", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1952, 1, 1)) 
		Ali 	= ftwa.Person("Ali", 	gender=ftwa.Gender.MALE, 	birthdate =date(1948, 1, 1)) 
		Ali2 	= ftwa.Person("Ali", 	gender=ftwa.Gender.MALE, 	birthdate =date(1960, 1, 1)) 
		Deniz	= ftwa.Person("Deniz", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1960, 1, 1)) 
		Melis 	= ftwa.Person("Melis", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1961, 1, 1)) 
		Ahmet 	= ftwa.Person("Ahmet", 	gender=ftwa.Gender.MALE, 	birthdate =date(1960, 1, 1)) 
		Güneş 	= ftwa.Person("Güneş", 	gender=ftwa.Gender.MALE, 	birthdate =date(1980, 1, 1)) 
		Seçil 	= ftwa.Person("Seçil", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1975, 1, 1)) 
		Orhan	= ftwa.Person("Orhan", 	gender=ftwa.Gender.MALE, 	birthdate =date(1978, 1, 1)) 
		Derya 	= ftwa.Person("Derya", 	gender=ftwa.Gender.FEMALE, 	birthdate =date(1982, 1, 1))  
		Tolga 	= ftwa.Person("Tolga", 	gender=ftwa.Gender.MALE, 	birthdate =date(1982, 1, 1)) 


		self.G.person_list[Ayşe.uid] = Ayşe
		self.G.person_list[Erdem.uid] = Erdem
		self.G.person_list[Erdi.uid] = Erdi
		self.G.person_list[Sibel.uid] = Sibel

		self.G.person_list[Seda.uid] = Seda
		self.G.person_list[Ali.uid] = Ali
		self.G.person_list[Ali2.uid] = Ali2
		self.G.person_list[Deniz.uid] = Deniz
		self.G.person_list[Melis.uid] = Melis
		self.G.person_list[Ahmet.uid] = Ahmet
		self.G.person_list[Güneş.uid] = Güneş
		self.G.person_list[Seçil.uid] = Seçil
		self.G.person_list[Orhan.uid] = Orhan
		self.G.person_list[Derya.uid] = Derya
		self.G.person_list[Tolga.uid] = Tolga


 
		self.G.new_relation(Ayşe, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Erdem)
		self.G.new_relation(Erdi, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Sibel)
		self.G.new_relation(Seda, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Ali)
		self.G.new_relation(Ali2, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Deniz)
		self.G.new_relation(Melis, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Ahmet)

		self.G.new_relation(Ayşe, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Erdi)
		self.G.new_relation(Ayşe, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Seda)
		self.G.new_relation(Ayşe, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali2)
		self.G.new_relation(Ayşe, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Melis)

		self.G.new_relation(Erdem, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Erdi)
		self.G.new_relation(Erdem, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Seda)
		self.G.new_relation(Erdem, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali2)
		self.G.new_relation(Erdem, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Melis)


		self.G.new_relation(Erdi, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Güneş)
		self.G.new_relation(Sibel, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Güneş)
		self.G.new_relation(Seda, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Seçil)
		self.G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Seçil)
		self.G.new_relation(Seda, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Orhan)
		self.G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Orhan)
		self.G.new_relation(Ali2, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Derya)
		self.G.new_relation(Deniz, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Derya)
		self.G.new_relation(Melis, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Tolga)
		self.G.new_relation(Ahmet, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Tolga)

		self.G.new_relation(Erdi, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Seda)
		self.G.new_relation(Erdi, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali2)
		self.G.new_relation(Erdi, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Melis)
		self.G.new_relation(Seda, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Ali2)
		self.G.new_relation(Seda, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Melis)
		self.G.new_relation(Ali2, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Melis)
		self.G.new_relation(Seçil, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Orhan)






	def do_create(self, arg):
		"Creates person\nUsage: create <name> <surname> <gender> <birthdate> <deathdate>\nName and surname mandatory\nExamples: create Ali Durmaz\n\tcreate name=Ali surname=Durmaz birthdate=1999.1.1"

		temp = ftwa.Person(*parse(arg))
		print("Created {}".format(temp.str()))
		self.G.person_list[temp.uid] = temp

	def do_search(self, arg):
		"Search and retrieve information of a person\nUsage: search <person>"
		try:
			print(self.G.person_list[int(arg[0])].str())
		except:
			print("[ERROR] Not Found!")
			print(self.G.person_list.keys())

	def complete_search(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions

	def do_placeholder(self, arg):#TODO 
		"Queries if a person is a placeholder\nUsage: placeholder <person>"
		try:
			print(self.G.person_list[int(arg[0])].is_placeholder())
		except:
			print("[ERROR] Not Found!")
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
		
		 #p1 = self.G.person_lis		
		print(self.G.get_relation_between(self.G.person_list[int(parse(arg)[0])], self.G.person_list[int(parse(arg)[1])]).name)

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

		relationstr = parse(arg)[2].upper()

		try:
			self.G.new_relation(self.G.person_list[int(parse(arg)[0])], ftwa.Relation[relationstr], ftwa.Person.get_reverse_relation(ftwa.Relation[relationstr]), self.G.person_list[int(parse(arg)[1])])

		except:
			print("[ERROR] Failed To Add Relation!\n{}".format(sys.exc_info()))



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
			print(relation[0], relation[1], relation[2], relation[3])

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
		try:
			del self.G.person_list[int(parse(arg)[0])]
			self.G.fix_relation_table()
			print("Deleted successfully!")
		except:
			print("Not Found! {}".format(sys.exc_info()))
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

		try:
			print(int(parse(arg)[0]))
			self.G.person_list[int(parse(arg)[0])]
		except:
			print("[ERROR] Not Found!")
			return
		if parse(arg)[1] == "name":
			self.G.person_list[int(parse(arg)[0])].set_name(parse(arg)[2])
			self.G.person_list[self.G.person_list[int(parse(arg)[0])].name+self.G.person_list[int(parse(arg)[0])].surname] = self.G.person_list[int(parse(arg)[0])]
			del self.G.person_list[int(parse(arg)[0])]
			print("Successfully updated!")



		if parse(arg)[1] == "surname":
			self.G.person_list[int(parse(arg)[0])].set_surname(parse(arg)[2])
			self.G.person_list[self.G.person_list[int(parse(arg)[0])].name+self.G.person_list[int(parse(arg)[0])].surname] = self.G.person_list[int(parse(arg)[0])]
			del self.G.person_list[int(parse(arg)[0])]
			print("Successfully updated!")
			return
		if parse(arg)[1] == "gender":

			self.G.person_list[int(parse(arg)[0])].set_gender(parse(arg)[2])
			print("Successfully updated!")

		if parse(arg)[1] == "birthdate":

			temp_person = copy.deepcopy(self.G.person_list[int(parse(arg)[0])])
			temp_person.set_birthdate(parse(arg)[2])


			for relation in self.G.get_persons_relations_of_a_kind(self.G.person_list[int(parse(arg)[0])], ftwa.Relation.PARENT):
				if (relation[3].birthdate - temp_person.birthdate).days > 0:
					print ("You can't set birthdate older than parents birthdate")
					return


			for relation in self.G.get_persons_relations_of_a_kind(self.G.person_list[int(parse(arg)[0])], ftwa.Relation.CHILD):
				if (relation[3].birthdate - temp_person.birthdate).days < 0:
					print ("You can't set birthdate younger than children birthdate")
					return


			self.G.person_list[int(parse(arg)[0])].set_birthdate(parse(arg)[2])
			print("Successfully updated!")
		if parse(arg)[1] == "deathdate":

			self.G.person_list[int(parse(arg)[0])].set_deathdate(parse(arg)[2])
			print("Successfully updated!")

		else:
			print("[ERROR] Invalid field: {}".format(parse(arg)[1]))
			self.do_help("update")

			
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
			print(self.G.person_list[int(parse(arg)[0])].get_age())
		except:
			print("[ERROR] Not Found!")	

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
			print(self.G.get_level(self.G.person_list[int(parse(arg)[0])]))
		except:
			print("[ERROR] Not Found!")	

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
				Y.nodes().index(v.uid)
			except:
				Y.add_node(v.uid)
				labels2[v.uid] = v.str_short()

		for rel in self.G.relation_list:
			try:
				Y.edges().index(rel[0], rel[3])
			except:
				Y.add_edge(rel[0], rel[3])
				edgelabels2[rel[0], rel[3]] = r'${}$'.format(rel[1].name)
		

		pos=nx.spring_layout(Y, iterations= 3000)


		if len(parse(arg)) > 0:
			if parse(arg)[0] == "circular":
				pos=nx.circular_layout(Y)
			if parse(arg)[0] == "spectral":
				pos = nx.spectral_layout(Y)
			if parse(arg)[0] == "random":
				pos = nx.random_layout(Y)
			if parse(arg)[0] == "shell":
				pos = nx.shell_layout(Y)
			if parse(arg)[0] == "graphviz":
				pos = nx.graphviz_layout(Y)



		plt.title("Family Graph")
		nx.draw_networkx(G=Y, pos=pos, labels=labels2, font_size=14, style="dashed")
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2, style="dashed")
		#nx.draw_circular(Y)
		
		#plt.axis("off")
		#plt.savefig("family_graph.png") # save as png
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
		plt.show() # display
		

	def do_sub_print(self, arg):
		"Visualizes first-degree relations relations of a node\nUsage: subprint <person>"

		labels2 = {}
		
		edgelabels2 = collections.OrderedDict()

		Y=nx.DiGraph()


		for v in self.G.get_first_degree_relatives(self.G.person_list[int(parse(arg)[0])]):
			try:
				Y.nodes().index(v.uid)
			except:
				Y.add_node(v.uid)
				labels2[v.uid] = v.str_short()

		labels2[int(parse(arg)[0])] = self.G.person_list[int(parse(arg)[0])].str_short()

		for rel in self.G.get_persons_relations(self.G.person_list[int(parse(arg)[0])]):
			try:
				Y.edges().index(rel[0], rel[3])
			except:
				Y.add_edge(rel[0], rel[3])
				edgelabels2[rel[0], rel[3]] = r'${}$'.format(rel[1].name)
		

		pos=nx.spring_layout(Y, iterations= 3000)


		if len(parse(arg)) > 0:
			if parse(arg)[0] == "circular":
				pos=nx.circular_layout(Y)
			if parse(arg)[0] == "spectral":
				pos = nx.spectral_layout(Y)
			if parse(arg)[0] == "random":
				pos = nx.random_layout(Y)
			if parse(arg)[0] == "shell":
				pos = nx.shell_layout(Y)
			if parse(arg)[0] == "graphviz":
				pos = nx.graphviz_layout(Y)



		plt.title("First-Degree Relatives of {}".format(self.G.person_list[int(parse(arg)[0])].str_short()))
		nx.draw_networkx(G=Y, pos=pos, labels=labels2, font_size=14, style="dashed")
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2, style="dashed")
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

	FTWA().cmdloop()
