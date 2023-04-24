class Game:
    """Hasonló a probléma osztályhoz"""

    def actions(self,state):
        """MEgendegett mozgások listája"""
        raise NotImplementedError

    def result(self,state,move):
        """Vissza adja az állapotot, mely a mozgás eredménye"""
        raise NotImplementedError

    def utility(self,state,player):
        """végső állapot eredménye"""
        raise NotImplementedError

    def terminal_test(self,state):
        """True amikor ez a játék végső állapota"""
        return not self.actions(state)

    def to_move(self,state):
        """adja vissza a játékost akinek a lépése ebben az állapotban van"""
        return state.to_move

    def display(self,state):
        """toString basically"""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self,*players):
        """N-személyes játék játszása"""

        #kezdő állapot
        state = self.initial

        # Végső lépésig tart a játék
        while True:
            # Veszünk egy játékost
            for player in players:
                # Adjon egy lépést a választott játékos
                move = player(self,state)
                # Kérjük vissza annak eredményét, hogy hogyan módosul a játék
                # játékos lépést elvégezzük
                state = self.result(state,move)
                if self.terminal_test(state):
                    # Ha a lépés előállítja a végső állaptot, visszaadjuk a nyertest
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))