import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

from graphviz import Digraph

dot = Digraph(comment='Collatz-by-kimmy')

dot.node('1')
dot.node('2')
dot.node('4')
dot.node('8')
dot.node('16')
dot.node('3')
dot.node('10')
dot.node('5')

dot.edge('1', '2')
dot.edge('16', '8', constraint='false')


print(dot.source)
dot.render('Collatz-by-kimmy', view=True)
