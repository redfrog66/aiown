from ora8.game import Game
from collections import namedtuple

GameState = namedtuple('GameState','to_move, utility, board, moves')

class TicTacToe(Game):

    def __init__(self,h = 3,v=3,k = 3) -> None:
        self.h = h #sorok száma
        self.v = v #oszlopok száma
        ## hány egymást követő X vagy O kell egy sorban vagy oszlopban vagy átlósan a győzelemhez
        self.k = k
        # A kezdőállapotból elérhető összes lehetséges mozgás
        moves = [(x,y)for x in range(1,h+1) for y in range(1,v+1)]
        #kezdő állapot beállítása
        self.initial = GameState(to_move='X', utility = 0, board = {},moves=moves)

    def actions(self, state):
        return state.moves  # Lehetséges lépések(minden mező ami még nem volt)
    
    def result(self, state, move):
        if move not in state.moves:
            return state # nem lehet illegal lepes
        
        #Készitünk egy másolatot
        board = state.board.copy()
        
        # Beállitjuk az uj lépés (X vagy O)
        board[move] = state.to_move

        # Frissitjük a lehetséges lépések listáját
        moves = list(state.moves)
        moves.remove(move)

        # Állitsuk elő az új állapotot
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board,moves=moves)
    
    def utility(self, state, player):
        """visszaadja az értéket"""
        return state.utility if player =='X' else -state.utility

    def terminal_test(self, state):
        """akkor végső ha nyert vagy nincs üres mező"""
        return state.utility != 0 or len(state.moves) == 0
    
    def display(self, state):
        #lekérjük a táblát. dic(szótár) objektum
        board = state.board

        # Járjuk be a táblát

        for x in range(1,self.h + 1):
            for y in range(1,self.v + 1):
                # Irjuk ki az értéket ha van olyan eleme a szótárnak (táblának) ha  nincs akkor irjunk ki egy pontot
                print(board.get((x,y),'.'), end=' ')
            print()
    
    def compute_utility(self,board,move,player):
        """Ha 'x' nyer ezzel a lépéssel adjon vissza 1-et; ha O akkor -1 et, külömben 0"""
        if (self.k_in_row(board,move,player,(0,1)) or # Oszlopok ellenorzese
            self.k_in_row(board,move,player,(1,0)) or # sorok ellenőrzése
            self.k_in_row(board,move,player,(1,-1)) or # / átló ellenőrzése
            self.k_in_row(board,move,player,(1,1))): # \ átló ellenőrzése
            return +1 if player == 'X' else -1
        else:
            return 0
                
    def k_in_row(self,board,move,player,delta_x_y):
        """Vissza ad egy igazi értéket ha az adott irányba a játékos kigyüjtötte a megfelelő mennyiségü elemet"""

        (delta_x,delta_y) = delta_x_y
        x,y = move
        n = 0 # n a lépések száma a sorban
        while board.get((x,y,)) == player:
            n +=1
            x,y = x+ delta_x,y+delta_y
        x,y = move
        while board.get((x,y,)) == player:
            n +=1
            x,y = x- delta_x,y-delta_y
        n -= 1 #mert a mozgast 2szer szamoltuk
        return n >= self.k
