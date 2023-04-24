import numpy as np

def minmax(state,game):
    """Min max döntés alapján működő keresés implementációja"""

    # Játékos szabad lépéseinek lekérdezése. Hova léphet?
    player = game.to_move(state)

    def max_value(state):
        # ha a játék végállás akkor vissza adjuk az eredményt
        if game.terminal_test(state):
            return game.utility(state,player)
        
        v = -np.inf
        # Viszza adjuk a minimum értékek közül a legnagyobbat
        for a in game.actions(state):
            v = max(v,min_value(game.result(state,a)))

        return v
    def min_value(state):

        if game.terminal_test(state):
            return game.utility(state,player)
        v = np.inf

        for a in game.actions(state):
            v = min(v,max_value(game.result(state,a)))
        return v

    return max(game.actions(state),key=lambda a: min_value(game.result(state,a)))
    
def alpha_beta_search(state,game):
    """Alfa-béta vágás alapján működő keresés implementációja"""

    # Játékos szabad lépéseinek lekérdezése. Hova léphet?
    player = game.to_move(state)

    def max_value(state,alpha,beta):
        if game.terminal_test(state):
            return game.utility(state,player)
        
        v = -np.inf

        for a in game.actions(state):

            v = max(v,min_value(game.result(state,a),alpha,beta))

            if v >= beta:
                return v
            alpha = max(alpha,v)
        
        return v
    
    def min_value(state,alpha,beta):

        if game.terminal_test(state):
            return game.utility(state,player)
        
        v = np.inf

        for a in game.actions(state):

            v = min(v,max_value(game.result(state,a),alpha,beta))

            if v <= alpha:
                return v
            beta = min(beta,v)

        return v
    
    best_score = -np.inf

    beta = np.inf

    best_action = None

    for a in game.actions(state):

        v = min_value(game.result(state,a),best_score,beta)
        if v > best_score:
            best_score = v
            best_action = a

    return best_action