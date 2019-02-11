from copy import deepcopy

class Graph:
    """This graph structure is based on a dictionary and contain basic methods 
    like adding or removing vertice, edge and coloring vertex."""
    def __init__(self, graph_dict = None, directed = False):
        if graph_dict == None:
            graph_dict = {}
        else:
            self.__directed = directed
            self.__graph_dict = graph_dict
    
    def vertices(self):
        vertex = list(self.__graph_dict.keys())
        for v in self.__graph_dict:
            for n in self.__graph_dict[v]:
                vertex.append(n)
        return set(vertex)
    
    def edges(self):
        return self.generate_edges()
    
    def generate_edges(self):
        edges = []
        for v in self.__graph_dict:
            for n in self.__graph_dict[v]:
                if(self.__directed == True):
                    edges.append({v, n})
                elif(self.__directed == False and {v,n} not in edges):
                    edges.append({v, n})
        return edges
    
    def is_empty(self):
        return self.__graph_dict == {}
    
    def __str__(self):
        result = ""
        for v in self.__graph_dict:
            result += str(v) + ": "
            for n in self.__graph_dict[v]:
                result += str(n) + ", "
        return result
    
    def add_vertex(self, v):
        if v in self.__graph_dict:
            raise ValueError("This vertice already exist in graph")
        else:
            self.__graph_dict[v] = []
    
    def add_edge(self, v1, v2):
        if(v1 in self.__graph_dict and v2 not in self.__graph_dict):
            self.add_vertex(v2)
        if(self.__directed):
            if(v1 in self.__graph_dict and v2 in self.__graph_dict[v1]):
                raise ValueError("This edge already exist in graph")
            elif(v1 in self.__graph_dict):
                self.__graph_dict[v1].append(v2)         
            else:
                self.__graph_dict[v1] = [v2]
        else:
            if(v1 in self.__graph_dict):
                self.__graph_dict[v1].append(v2)
                self.__graph_dict[v2].append(v1)
            else:
                self.__graph_dict[v1] = [v2]
                self.__graph_dict[v2] = [v1]
    
    def remove_vertex(self, v):
        if(self.is_empty()):
            raise ValueError("Graph is empty.")
        elif(v not in self.__graph_dict):
            raise ValueError("The vertice not exist in graph.")
        else:
            for k in self.__graph_dict.keys():
                if(v in self.__graph_dict[k]):
                    del self.__graph_dict[k][self.__graph_dict[k].index(v)]
            del self.__graph_dict[v]
    
    def remove_edge(self, v1, v2):
        if(self.is_empty()):
            raise ValueError("Graph is empty.")
        elif(v1 not in self.__graph_dict or v2 not in self.__graph_dict[v1]):
            raise ValueError("The vertice not exist in graph.")
        else:
            del self.__graph_dict[v1][self.__graph_dict[v1].index(v2)]
            if(not self.__directed):
                del self.__graph_dict[v2][self.__graph_dict[v2].index(v1)]
    
    def vertice_degree(self):
        """The method returns dictionary contains degree each vertex in graph."""
        if(self.is_empty()):
            raise ValueError("Graph is empty.")
        else:
            if(self.__directed):
                degrees = {}
                l = list(self.__graph_dict.values())
                flatter = []
                for x in l:
                    for y in x:
                        flatter.append(y)

                for k in self.__graph_dict.keys():
                    degrees[k] = len(self.__graph_dict[k])
                    if(k in flatter):
                         degrees[k] += flatter.count(k)
                return degrees

            else:
                degrees = {}
                for k in self.__graph_dict.keys():
                    degrees[k] = len(self.__graph_dict[k])
                return degrees
    
    def neighbours(self, v):
        return self.__graph_dict.get(v)
    
    def SL_algorithm(self):
        copy_of_graph = Graph(deepcopy(self.__graph_dict))
        stack = []
        while(not copy_of_graph.is_empty()):
            v_min = min((copy_of_graph.vertice_degree()).items(), key=lambda x:x[1])[0]
            stack.append(v_min)
            copy_of_graph.remove_vertex(v_min)
        return stack

    def greedily_coloring(self, stack):
        color_of_vertex = {}
        n = len(self.__graph_dict)
        while(stack != []):
            c = [False] * n
            ver = stack.pop()
            neighbour = self.__graph_dict[ver]
            for x in neighbour:
                if(x in color_of_vertex):
                    c[color_of_vertex.get(x)] = True
            color = 0
            while(c[color] == True):
                color += 1
            color_of_vertex[ver] = color
        return color_of_vertex
    
    def display_graph(self, color_of_vertex):
        """Visualization of the result."""
        import matplotlib.pyplot
        import networkx
        G = networkx.Graph()
        color_set = ['#FF0000', '#32CD32', '#FFD700', '#6B8E23', '#40E0D0', '#BA55D3', '#C0C0C0', '#A0522D', '#6A5ACD']
        color_map = []
        for k in self.__graph_dict.keys():
            G.add_node(k)
            for v in self.__graph_dict[k]:
                G.add_edge(k,v)
        for x in G.node:
            color_map.append(color_set[color_of_vertex[x]])
        networkx.draw(G, node_color = color_map, with_labels = True)
        matplotlib.pyplot.show()

    def vertex_coloring(self, display = False):
        """This function returns dictionary of vertices and their color, the function uses SL algorithm and greedily coloring. 
        The Result visualization uses the networkx and matplotlib libraries."""
        stack = self.SL_algorithm()
        color_of_vertex = self.greedily_coloring(stack)
        if(display):
            self.display_graph(color_of_vertex)
            return color_of_vertex
        else:      
            return color_of_vertex

import unittest
class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph({1: [2,3], 2: [1, 3], 3: [1, 2, 4], 4:[3]})
        self.g2 = Graph({1: [3], 2: [1, 3], 3: [4]}, True)
    
    def test_vertice(self):
        self.assertEqual(self.g1.vertices(), {1, 2, 3, 4})
        self.assertEqual(self.g2.vertices(), {1, 2, 3, 4})
    
    def test_edge(self):
        self.assertEqual(self.g1.edges(), [{1,2}, {1,3}, {2,3}, {3,4}])
    
    def test_add(self):
        self.g1.add_vertex(5)
        self.assertEqual(self.g1.vertices(), {1, 2, 3, 4, 5})
        self.g2.add_edge(4,5)
        self.assertEqual(self.g2.vertices(), {1, 2, 3, 4, 5})
    
    def test_remove(self):
        self.g1.remove_vertex(3)
        self.assertEqual(self.g1.vertices(), {1, 2, 4})
        self.g2.remove_edge(3,4)
        self.assertEqual(self.g2.vertices(), {1, 2, 3})
    
    def test_vertex_degree(self):
        self.assertEqual(self.g1.vertice_degree(), {1:2, 2:2, 3:3, 4:1})
        self.assertEqual(self.g2.vertice_degree(), {1:2, 2:2, 3:3})
    
    def test_coloring(self):
        self.assertEqual(self.g1.vertex_coloring(), {3:0, 2:1, 1:2, 4:1})

if(__name__ == "__main__"):
    unittest.main()
