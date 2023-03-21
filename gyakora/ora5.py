from nqueens import NQueens

nq4 = NQueens(4)
print(nq4.initial,nq4.goal)

from libs.search import trial_error

nq4 = NQueens(4)
print(nq4.initial,nq4.goal)
trial_error(nq4)

##### A* algoritmus

#ipari felhasználás, ténylegesen mesterséges intelligenciához kapcsolódik

from libs.node import Node

tmp = [Node((3,2,-1,-1)), Node((3,-1,-1,-1)), Node((1,2,-1,0))]
tmp

def sort_by_heur(items):
  return sorted(items, key = lambda x: sum(x.state))

sort_by_heur(tmp)


nq8 = NQueens(8)
print(astar_search(nq8, sort_by_heur))