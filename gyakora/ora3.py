#####################################################
# HAGYOMÁNYOS REJTVÉNYEK - NEM DEFINIÁLT ALGORITMUSOK
#####################################################

# Csak a probléma definiálásához megadott információkat használják fel
# Példák:
# - Szélességi keresés
# - mélységi keresés
# - egyenletes költségű keresés
# - mélységkorlátozott keresés
# - iteratívan mélyülő mélységi keresés

############
# FIFO
############

from collections import deque

que = deque([1,2,3,4])
for i in range(2):
    print(que.popleft())
print(que)

# HANOI
from hanoi import Hanoi
from libs.search import breadth_first_tree_search

h = Hanoi(3)
print(h.size, h.initial, h.goal)
breadth_first_tree_search(h).solution()

# 3 EDÉNY

from cup3 import Cup3

c = Cup3((5,0,0),[(4,1,0),(4,0,1)])
print(c.initial, c.goal)

breadth_first_tree_search(c).solution()

############
# Mélységi keresés
############

# Verem
stack = [1,2,3,4]

for i in range(2):
  print(stack.pop())

  stack

############
# Hurok probléma
############

from libs.search import depth_first_graph_search #???
#HANOI
h = Hanoi(3)
print(h.size, h.initial, h.goal)

depth_first_graph_search(h).solution()
# EDÉNY
c = Cup3((5,0,0),[(4,1,0),(4,0,1)])
print(c.initial, c.goal)

depth_first_graph_search(c).solution()