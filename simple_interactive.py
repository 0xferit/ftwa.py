import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt
import ftwa
from datetime import date
import collections

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	
	FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
	PERSONS = []
	
	Veli 	= ftwa.Person("Veli", "Yanyatan",   ftwa.Gender.MALE, date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
	Ali 	= ftwa.Person("Ali", "Yanyatan",    ftwa.Gender.MALE, date(1980, 12, 15), date(2055, 12, 15)) # Baba
	Huri 	= ftwa.Person("Huri", "Yanyatan", ftwa.Gender.FEMALE, date(1983, 12, 15), date(2075, 12, 15)) # Anne
	Deli 	= ftwa.Person("Deli", "Yanyatan",   ftwa.Gender.MALE, date(2007, 12, 15), date(2075, 12, 15)) # Çocuk
	Riza	= ftwa.Person("Riza", "Yanyatan",   ftwa.Gender.MALE, date(1970, 1, 1), date(2030, 12, 12)) # Dede, Ali'nin babası
	Fatmagul= ftwa.Person("Fatmagul", "Yanyatan", ftwa.Gender.FEMALE, birthdate = date(2000, 1, 1))

	G = ftwa.FamilyGraph()

	G.person_list[Veli.name+Veli.surname] = Veli
	G.person_list[Ali.name+Ali.surname] = Ali
	G.person_list[Huri.name+Huri.surname] = Huri
	G.person_list[Deli.name+Deli.surname] = Deli
	G.person_list[Riza.name+Riza.surname] = Riza
	G.person_list[Fatmagul.name+Fatmagul.surname] = Fatmagul

	G.new_relation(Ali, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Huri)
	G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
	G.new_relation(Ali, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
	G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Veli)
	G.new_relation(Huri, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Deli)
	G.new_relation(Veli, ftwa.Relation.SIBLING, ftwa.Relation.SIBLING, Deli)
	G.new_relation(Riza, ftwa.Relation.CHILD, ftwa.Relation.PARENT, Ali)
	G.new_relation(Deli, ftwa.Relation.SPOUSE, ftwa.Relation.SPOUSE, Fatmagul)

	
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
			completions = self.FRIENDS[:]
		else:
			completions = [ f
					for f in self.FRIENDS
					if f.startswith(text)
					]
		return completions

	def do_create(self, arg):
		"Creates person"
		print(*parse(arg))
		temp = ftwa.Person(*parse(arg))
		print(temp.str())
		self.G.person_list.append(temp)

	def do_search(self, arg):
		try:
			print(self.G.person_list[parse(arg)[0]].str())
		except:
			print("Not Found!")

	def list(self, arg):
		for key in self.G.person_list.keys():
			print((self.G.person_list[key]).str())

	def do_list(self, arg):
		for k, v in self.G.person_list.items():
			print(k, v.str())
	
	def do_relation(self, arg):
		"Prints relation between two persons"
		print(self.G.get_relation_between(self.G.person_list[parse(arg)[0]], self.G.person_list[parse(arg)[1]]))
	
	
	def do_print(self, arg):

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
		

		
		pos=nx.spring_layout(Y, iterations=500, scale=3.0)

		print(Y.edges())


		nx.draw(Y, pos, labels=labels2, arrows= True)
		nx.draw_networkx_edge_labels(Y,pos, edgelabels2)
	
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True

def parse(arg):
	return arg.split()


if __name__ == '__main__':
	HelloWorld().cmdloop()
