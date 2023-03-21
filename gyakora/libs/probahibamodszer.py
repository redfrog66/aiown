import numpy as np
from libs.node import Node

while True:
    if problem.goal_test(state.state):
        print("Got it")
        return state

    # az alkalmazható operátorok segítségéve gyártusk le az összes lehetséges utódot
    succesors = state.expand(problem)

    # ha nincs új állapot
    if len(succesors) == 0:
        return 'Unsolvable'

    # random választunk egy újat a legyártott utódok közül
    state = succesors[np.random.randint(0, len(succesors))]
    print(state)
