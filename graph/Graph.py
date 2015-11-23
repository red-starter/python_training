class Node:
	def __init__(self, name):
		self.name = name
		self.adjacent = {}
	def __str__(self):
		return str(self.name) + ' neighbours: '+str([x.name for x in self.adjacent])
	def add_adjacent(self,node,weight=0):
		self.adjacent[node] = weight
	def get_weight(self,node):
		return self.adjacent[node]
	def get_name(self):
		return self.name
	def get_adjacent(self):
		return self.adjacent.keys()

class Graph:
	def __init__(self):
		self.nodes = {}
		self.length = 0

	def __iter__(self):
		# alllows us to iterate easily over Graph
		return iter(self.nodes.values())
	def add_node(self,name):
		new_node = Node(name)
		self.length += 1
		self.nodes[name] = new_node
		return new_node
	def get_node(self,name):
		if name in self.nodes:
			return self.nodes[name]
		return None

	def add_edge(self,name1,name2,weight=0):
		if name1 not in self.nodes:
			self.add_node(name1)
		if name2 not in self.nodes:
			self.add_node(name2)
		node1 = self.nodes[name1]
		node2 = self.nodes[name2]
		node1.add_adjacent(node2,weight)
		node2.add_adjacent(node1,weight)

	def get_nodes():
		return self.nodes.values()

if __name__ == '__main__':

    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_adjacent():
            vid = v.get_name()
            wid = w.get_name()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    for v in g:
        print 'g.nodes[%s]=%s' %(v.get_name(), g.nodes[v.get_name()])