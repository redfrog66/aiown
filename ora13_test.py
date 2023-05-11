import matplotlib as plt

pong.init_pong()

import pickle

with open("agent.pkl","rb") as f:
    pong.agent = pickle.load()