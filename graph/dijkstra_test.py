import Graph as G
import dijkstra as D 

import unittest as U 

class TestDijkstra(U.TestCase):

	def test_1(self):
		g = G.Graph()
		g.add_node('a')
		g.add_node('b')
		g.add_edge('a','b')

		self.assertEqual(D.search(g.get_node('a'),g.get_node('b')),['a','b'])

	def test_2(self):
		g = G.Graph() 
		g.add_node('a')
		g.add_node('b')
		g.add_node('c')
		g.add_node('d')
		g.add_node('e')
		g.add_node('f')

		# shortest path a-b-d-e-c-f
		g.add_edge('a', 'b', 1)  
		g.add_edge('b', 'd', 1)
		g.add_edge('d', 'e', 1)
		g.add_edge('c', 'e', 1)
		g.add_edge('c', 'f', 1)
		g.add_edge('a', 'c', 100)
		g.add_edge('c', 'd', 100)
		g.add_edge('b', 'e', 100)
		g.add_edge('e', 'f', 100)

		start = g.get_node('a')
		end = g.get_node('f')

		self.assertEqual(D.search(start,end),['a','b','d','e','c','f'])

if __name__ == '__main__':
	U.main()