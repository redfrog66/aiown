import numpy as np
from libs.node import Node
from libs.problem import Problem
from collections import deque

##################
# próbahibamódszer
##################

def trial_error(problem):
    state = Node(problem.initial)

    while True:
        # A ciklus leáll, amikor a probléma megoldódott
        if problem.goal_test(state.state):
            return state

        # Az operátorok segítségével gyártsuk le az összes lehetséges utódot
        succesors = state.expand(problem)
        # nincs új állapot
        if len(succesors) == 0:
            return 'Unsolvable'

        # random választunk egy újat a legyártott utódok közül
        state = succesors[np.random.randint(0, len(succesors))]
        print(state)


##################
# hegymászós
##################

def hill_climbing_for_3Cup(problem, heuristic):
    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            return state

        # az összes lehetőséget megkeressük
        succesors = state.expand(problem)

        # keresünk egy jobb állapotot heurisztikának megfelelően
        test_succesors = []
        for s_test in succesors:
            if heuristic(state.state) >= heuristic(s_test.state):
                test_succesors.append(s_test)

        if len(test_succesors) == 0:
            return 'Unsolvable'

        state = test_succesors[np.random.randint(0, len(test_succesors))]
        print(state)

##################
# First In First Out
##################

def breadth_first_tree_search(problem: Problem) -> Node:
    # kezdő állaot kiolvasása és FIFO sorba helyezése
    frontier = deque([Node(problem.initial)])

    # Amíg nem értük el a határt
    while frontier:
        # legszélsőbb elem kiemelése
        node: Node = frontier.popleft()
        print(node)

        # ha cél állapotban vagyunk, akkor vége
        if problem.goal_test(node.state):
            return node

        # a kiemelt elemből az összes új állapot legyártása az operátorok segítségével
        frontier.extend(node.expand(problem))

##################
# verem
##################
def depth_first_tree_search(problem: Problem) -> Node:
    # kezdő elem verembe helyezése
    frontier = [Node(problem.initial)]
    # halmaz deklarálása a már bejárt elemekhez
    explored = set()

    # Amíg tudunk mélyebbre menni
    while frontier:
        # legfelső elem kiemelése a veremből
        node = frontier.pop()
        print(node)

        # ha cél állapotban vagyunk, akkor vége
        if problem.goal_test(node.state):
            return node

        # állapot feljegyzése hogy tudjuk már jártunk itt
        explored.add(node.state)

        # verem bővítése a még be nem járt elemekkel
        frontier.extend(child for child in node.expand(problem) if child.state not in explored and child not in frontier)

##################
# A star search
##################

def best_first_graph_search(problem: Problem, f=None) -> Node:
    # kezdőállapot
    node: Node = Node(problem.initial)
    # prioritásos (heurisztika szerint rendezett) sor
    frontier = []
    # kezdőállapot felvétele a prioritásos sorba
    frontier.append(node)
    # halmaz a már vizsgált elemekre
    explored = set()

    # amig van elemunk
    while frontier:
        # elem kivétele a verem tetejéről
        node = frontier.pop()

        # ha a cél állapotban vagyunk vége
        if problem.goal_test(node.state):
            return node
        # feldolgozott elemek bővítése
        explored.add(node)

        # operátorral legyártott gyerek elemek bejárása
        for child in node.expand(problem):
            # ha még nem dolgoztuk fel
            if child.state not in explored and child not in frontier:
                frontier.append(child)

        # rendezzük a listát (a sort) a heurisztikának megfelelően
        frontier = f(frontier)
        print(node.state)


def astar_search(problem: Problem, f=None) -> Node:
    """
    Az A* algoritmus egy olyan A-algoritmusfajta, mely garantálja az optimális megoldás előállítását
    h*(n) : az n-ből valamely célcsúcsba jutás optimális költsége.
    g*(n) : a startcsúcsból n -be jutás optimális költsége
    f*(n)=g*(n)+h*(n) : értelemszerűen a startból n-en keresztül valamely célcsócsba jutás költsége
    """
    return best_first_graph_search(problem, f)