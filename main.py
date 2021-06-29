class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = 0
        
        
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]



class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        #self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def bfs(self, v):
      for i in self.vert_dict:
        self.vert_dict[i].explored = 0
      self.vert_dict[v].explored = 1
      lista=[]
      Queue = []
      Queue.append(v)
      while(len(Queue)>0):
        w = Queue.pop(0)
        for j in self.vert_dict[w].get_connections():
          if(j.explored==0):
            #print(j.get_id())
            j.explored=1
            Queue.append(j.get_id())
            lista.append(j.get_id())
      return lista
      
    def  parentesco(self,a,b):#funcao que indica a existencia de parentesco usando bfs
      q=[]
      p=[]
      
      for x in self.vert_dict[a].get_connections():
        for i in self.bfs(x.get_id()):
          q.append(i)
      for x in self.vert_dict[b].get_connections():
        for i in self.bfs(x.get_id()):
          p.append(i) 

      if(len(set(q).intersection(p))>0):
        print("true")
      
      else:
        print("false")
         

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('juca')
    g.add_vertex('caju')
    g.add_vertex('oliver')
    g.add_vertex('gin')
    g.add_vertex('marie')
    g.add_vertex('zec')
    g.add_vertex('pedro')
    g.add_vertex('alice')
    g.add_vertex('gina')
    g.add_vertex('bob')
    g.add_vertex('bonnie')
    g.add_vertex('elis')
    g.add_vertex('perf')

    g.add_edge('bob', 'bonnie', 0)  
    g.add_edge('bob', 'gina', 0)
    g.add_edge('alice', 'bonnie', 0)
    g.add_edge('alice', 'gina', 0)
    g.add_edge('bonnie', 'elis', 0)
    g.add_edge('perf', 'elis', 0)
    g.add_edge('caju', 'gin', 0)
    g.add_edge('caju', 'oliver', 0)
    g.add_edge('juca', 'gin', 0)
    g.add_edge('juca', 'oliver', 0)
    g.add_edge('gin', 'pedro', 0)
    g.add_edge('gina', 'pedro', 0)
    g.add_edge('oliver', 'zec', 0)
    g.add_edge('marie', 'zec', 0)

    g.parentesco('elis','pedro')
    g.parentesco('zec','perf')

    
    