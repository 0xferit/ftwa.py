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
	
	Veli 	= ftwa.Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15)) #Çocuk	
	Ali 	= ftwa.Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15)) # Baba
	Huri 	= ftwa.Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15)) # Anne
	Deli 	= ftwa.Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15)) # Çocuk


	THE_GRAPH = ftwa.FamilyGraph()

	THE_GRAPH.person_list.append(Veli)
	THE_GRAPH.person_list.append(Ali)
	THE_GRAPH.person_list.append(Huri)
	THE_GRAPH.person_list.append(Deli)

	THE_GRAPH.new_relation(Veli, ftwa.Relation.SPOUSE, Huri)
	THE_GRAPH.new_relation(Veli, ftwa.Relation.CHILD, Ali)
	THE_GRAPH.new_relation(Veli, ftwa.Relation.CHILD, Deli)
	THE_GRAPH.new_relation(Huri, ftwa.Relation.CHILD, Ali)
	THE_GRAPH.new_relation(Huri, ftwa.Relation.CHILD, Deli)

	
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
		self.THE_GRAPH.person_list.append(temp)

	def do_search(self, arg):
		print()

	def do_list(self, arg):
		for person in self.THE_GRAPH.person_list:
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
		labels['AliYanyatan']=r'$Ali Yanyatan$'
		labels['DeliYanyatan']=r'$Deli Yanyatan$'
		labels['HuriYanyatan']=r'$Huri Yanyatan$'
		labels['VeliYanyatan']=r'$Veli Yanyatan$'
		
		edgelabels = collections.OrderedDict()
		
		edgelabels2 = collections.OrderedDict()

		edgelabels2['HuriYanyatan', 'DeliYanyatan']=r'$x$'
		edgelabels2['HuriYanyatan', 'VeliYanyatan']=r'$x$'
		edgelabels2['HuriYanyatan', 'AliYanyatan']=r'$x$'
		edgelabels2['DeliYanyatan', 'VeliYanyatan']=r'$x$'
		edgelabels2['VeliYanyatan', 'AliYanyatan']=r'$x$'

		print(edgelabels2['HuriYanyatan', 'DeliYanyatan'])
		
		edgelabels3 = collections.OrderedDict()
		edgelabels3['HuriYanyatan', 'AliYanyatan']=r'$x$'
		
		Y=nx.Graph()

		#for person in self.THE_GRAPH.person_list:
		#	try:
		#		Y.nodes().index(person.name+person.surname)
		#	except:
		#		print("person not found, new person created: {}".format(person.name))
		#		Y.add_node(person.name + person.surname)
		#		first_degree_relatives = self.THE_GRAPH.get_first_degree_relatives(person)
		#		for rel in first_degree_relatives:
		#			if rel:
		#				print("inner")
		#				print("rel: {}".format(rel.name))
		#				try:
		#					Y.nodes().index(rel.name + rel.surname)
		#				except:
		#					Y.add_node(rel.name+rel.surname)
		#					Y.add_edge(rel.name+rel.surname, person.name+person.surname)

		for person in self.THE_GRAPH.person_list:
			try:
				Y.nodes().index(person.name + person.surname)
			except:
				Y.add_node(person.name + person.surname)

		for rel in self.THE_GRAPH.relation_list:
			try:
				Y.edges().index(rel[0].name+rel[0].surname, rel[2].name+rel[2].surname)
			except:
				Y.add_edge(rel[0].name+rel[0].surname, rel[2].name+rel[2].surname)
				#edgelabels[rel[0].name+rel[0].surname, rel[2].name+rel[2].surname] = r'$x$'
		
		for edge in Y.edges():
			edgelabels[edge]=r'$asd$'
		
		pos=nx.spring_layout(G)
		print("keys\n{}".format(dict(edgelabels)))
		print("Nodes of graph: ")
		print(Y.nodes())
		print("Edges of graph: ")
		print(Y.edges())
		nx.draw(Y, labels=labels)
		#nx.draw_networkx_edge_labels(G,pos, dict(edgelabels))
		#nx.draw(Y)		
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True

def parse(arg):
	return arg.split()


if __name__ == '__main__':
	HelloWorld().cmdloop()
