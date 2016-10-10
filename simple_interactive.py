import cmd
import networkx as nx
import tkinter
import matplotlib.pyplot as plt

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	
	FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
	
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
	
	
	def do_print(self, arg):
		G=nx.Graph()

		# adding just one node:
		G.add_node("a")
		# a list of nodes:
		G.add_nodes_from(["b","c"])

		print("Nodes of graph: ")
		print(G.nodes())
		print("Edges of graph: ")
		print(G.edges())
		G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])
		nx.draw(G)
		plt.savefig("simple_path.png") # save as png
		plt.show() # display
	
	def do_EOF(self, line):
		return True




if __name__ == '__main__':
	HelloWorld().cmdloop()
