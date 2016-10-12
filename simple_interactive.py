import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt
import ftwa
from datetime import date

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	
	FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
	PERSONS = []
	
	Veli 	= ftwa.Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15), None, None, None)	#Çocuk	
	Ali 	= ftwa.Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15), None, None, None, Veli) # Baba
	Huri 	= ftwa.Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15), None, None, Ali, Veli) # Anne
	Deli 	= ftwa.Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15), Ali, Huri, None) # Çocuk

	Ali.set_spouse(Huri)

	Veli.set_mother(Huri)
	Veli.set_father(Ali)

	Ali.add_child(Deli)
	Huri.add_child(Deli)

	PERSONS.append(Veli)
	PERSONS.append(Ali)
	PERSONS.append(Huri)
	PERSONS.append(Deli)

	
	def do_greet(self, person):
		"Greet the person"
		if person and person in self.FRIENDS:
			greeting = 'hi, %s!' % person
		elif person:
			greeting = "hello, " + person
		else:
			greeting = 'hello'
		print (greeting)
	
	def complete_greet(self, text, line, begidx, endidx):
		if not text:
			completions = self.FRIENDS[:]
		else:
			completions = [ f
					for f in self.FRIENDS
					if f.startswith(text)
					]
		return completions

	def do_create(self, arg):
		print(*parse(arg))
		temp = ftwa.Person(*parse(arg))
		print(temp.str())
		self.PERSONS.append(temp)

	def do_search(self, arg):
		print()

	def do_list(self, arg):
		for person in self.PERSONS:
			print(person.str())
		
	
	
	def do_print(self, arg):
		G=nx.Graph()

		# adding just one node:
		G.add_node("a", time="5pm")
		G.add_node("b")
		G.add_node("c")
		G.add_node("d")
		# a list of nodes:
		G.add_nodes_from(["b","c"])

		
		G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

		#
		X=nx.Graph()
		X.add_node("a")
		for z in range(5):
			X.add_node(z)
			X.add_edge("a", z)
		
		#
		labels = {}
		labels['AliYanyatan']=r'$AliYanyatan$'
		labels['DeliYanyatan']=r'$DeliYanyatan$'
		labels['HuriYanyatan']=r'$HuriYanyatan$'
		labels['VeliYanyatan']=r'$VeliYanyatan$'
		Y=nx.Graph()

		for person in self.PERSONS:
			try:
				Y.nodes().index(person.name+person.surname)
			except:
				print("person not found, new person created: {}".format(person.name))
				Y.add_node(person.name + person.surname)
				first_degree_relatives = person.get_first_degree_relatives()
				for rel in first_degree_relatives:
					if rel:
						print("inner")
						print("rel: {}".format(rel.name))
						try:
							Y.nodes().index(rel.name + rel.surname)
						except:
							Y.add_node(rel.name+rel.surname)
							Y.add_edge(rel.name+rel.surname, person.name+person.surname)
					

		print("Nodes of graph: ")
		print(Y.nodes())
		print("Edges of graph: ")
		print(Y.edges())
		nx.draw(Y, labels=labels)
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True

def parse(arg):
	return arg.split()


if __name__ == '__main__':
	HelloWorld().cmdloop()
