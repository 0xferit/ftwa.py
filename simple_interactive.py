import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt
import ftwa

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	
	FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
	PERSONS = []

	def parse(arg):
    		'Convert a series of zero or more numbers to an argument tuple'
    		return tuple(map(int, arg.split()))
	
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
		temp = ftwa.Person(tuple(map(int, arg.split())))
		print(temp.str())
	
	
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
		print("Nodes of graph: ")
		print(G.nodes())
		print("Edges of graph: ")
		print(G.edges())
		nx.draw(X)
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True




if __name__ == '__main__':
	HelloWorld().cmdloop()
