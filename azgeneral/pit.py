import Arena
from MCTS import MCTS
from antiaz.AntiazGame import AntiazGame, display
from antiaz.AntiazPlayers import *
from antiaz.pytorch.NNet import NNetWrapper as NNet

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

g = AntiazGame(9)

# all players
rp = RandomPlayer(g).play

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./temp/','best.pth.tar')
args1 = dotdict({'numMCTSSims': 24, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


#n2 = NNet(g)
#n2.load_checkpoint('/dev/8x50x25/','best.pth.tar')
#args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
#mcts2 = MCTS(g, n2, args2)
#n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

arena = Arena.Arena(n1p, rp, g, display=display)
print(arena.playGames(100, verbose=True))


#random 27:73 sim120
#random 25:75 sim24
#random 44:56 sim6

