import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt
import ftwa
from datetime import date
import collections
import re

class HelloWorld(cmd.Cmd):
		
	intro = """Family Tree Warehouse Application 0.1\nWelcome to ftwa shell! Type help or ? to list commands."""
	misc_header = """asda"""
	prompt = "(ftwa) "

	G = ftwa.FamilyGraph()

	def do_load_test_data(self, arg):
		"Loads an hardcoded family graph for testing"
		FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
		PERSONS = []
		ATTRIBUTE_NAMES = ["name", "surname", "gender", "birthdate", "deathdate"] 
	
		Veli 	= ftwa.Person("Veli", "Yanyatan",   ftwa.Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
		Ali 	= ftwa.Person("Ali", "Yanyatan",    ftwa.Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) # Baba
		Huri 	= ftwa.Person("Huri", "Yanyatan", ftwa.Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) # Anne
		Deli 	= ftwa.Person("Deli", "Yanyatan",   ftwa.Gender.MALE, date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
		Riza	= ftwa.Person("Riza", "Yanyatan",   ftwa.Gender.MALE, date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası
		Fatmagul= ftwa.Person("Fatmagül", "Yanyatan", ftwa.Gender.FEMALE, birthdate = date(2000, 1, 1))
		Makbule = ftwa.Person("Makbule", "Yanyatan", ftwa.Gender.FEMALE)
		Nuri	= ftwa.Person("Nuri", "Yanyatan", ftwa.Gender.MALE)
		Nurbanu	= ftwa.Person("Nurbanu", "Yanyatan", ftwa.Gender.FEMALE)
		Asli	= ftwa.Person("Asli",  "Yanyatan", ftwa.Gender.FEMALE)
		Kerem	= ftwa.Person("Kerem", "Yanyatan", ftwa.Gender.MALE)
		Mahmut	= ftwa.Person("Mahmut", "Devrik", ftwa.Gender.MALE)
		Emre	= ftwa.Person("Emre", "Bitmez", ftwa.Gender.MALE)
		Cimcime = ftwa.Person("Cimcime", "Yanyatan", ftwa.Gender.FEMALE)
		Pala	= ftwa.Person("Pala", "Tosbağa", ftwa.Gender.MALE)
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
		self.G.person_list[Pala.name+Pala.surname] = Pala
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
		self.G.new_relation(Pala, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Huri)
		self.G.new_relation(Duran, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Asli)


	
	def greet(self, person):
		"Greet the person"
		if person and person in self.FRIENDS:
			greeting = 'hi, %s!' % person
		elif person:
			greeting = "hello, " + person
		else:
			greeting = 'hello'
		print (greeting)
	
	def greet(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions

	def do_create(self, arg):
		"Creates person"
		print(*parse(arg))
		temp = ftwa.Person(*parse(arg))
		print(temp.str())
		self.G.person_list[temp.name+temp.surname] = temp

	def do_search(self, arg):
		"Search and retrieve information of a person\nUsage: search person"
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
		"Lists persons and their informations\nUsage: list"
		for k, v in self.G.person_list.items():
			print(k, v.str())
	
	def do_relation(self, arg):
		"Prints relation between two persons"
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
	
	def do_alive(self, arg):
		"Lets you know where the person is dead or alive\nUsage: alive person"
		try:
			print(self.G.person_list[parse(arg)[0]].is_alive())
		except:
			print("Not Found!")

	def complete_alive(self, text, line, begidx, endidx):
		if not text:
			completions = self.G.person_list[:]
		else:
			completions = [ f
					for f in self.G.person_list
					if f.startswith(text)
					]
		return completions	

	def do_update(self, arg):
		if parse(arg)[1] == "name":
			self.G.person_list[parse(arg)[0]].set_name(parse(arg)[1])

		if parse(arg)[1] == "surname":
			self.G.person_list[parse(arg)[0]].set_surname(parse(arg)[1])

		if parse(arg)[1] == "gender":
			g = ftwa.Gender(parse(arg)[2])
			self.G.person_list[parse(arg)[0]].set_gender(parse(arg)[1])

		if parse(arg)[1] == "birthdate":
			date_str = re.split("\.|-",parse(arg)[2])
			for x in date_str:
				print(x)
			results = list(map(int, date_str))
			bd = date(results[0], results[1], results[2])
			self.G.person_list[parse(arg)[0]].set_birthdate(bd)

		if parse(arg)[1] == "deathdate":
			date_str = re.split("\.|-",parse(arg)[2])
			for x in date_str:
				print(x)
			results = list(map(int, date_str))
			dd = date(results[0], results[1], results[2])
			self.G.person_list[parse(arg)[0]].set_birthdate(dd)


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
		"Get age of person\nUsage: age person"
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
		"Get level of person. Returns longest parental path distance\nUsage: level person"
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

		print(Y.edges())


		nx.draw(Y, pos, labels=labels2) # FONT SIZE BURAYA OLMUYO
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2)
	
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True

def parse(arg):
	return arg.split()


if __name__ == '__main__':

	HelloWorld().cmdloop()