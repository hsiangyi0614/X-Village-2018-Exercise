#method1
class shape():
    def set_edge(self):
        self.edge = int(input("enter a number : "))
    def display(self):
        for i in range(1,self.edge+1):
            print(i*'*')
x = shape()
x.set_edge()
'''
set_edge(self,edge_arg)
set_edge(x,5):
    x.edge=5
'''
x.display()
#method2
class shape():
    def set_edge(self,edge_arg):
        self.edge = edge_arg
    def display(self):
        for i in range(1,self.edge+1):
            print(i*'*')
x = shape()
x.set_edge(5)
'''
set_edge(self,edge_arg)
set_edge(x,5):
    x.edge=5
'''
x.display()
