#coding:utf-8
import networkx as nx
import matplotlib 
matplotlib.use('agg')
import matplotlib.pyplot as plt

import pygraphviz as pgv
# G=nx.DiGraph()


import random

class node:
    right = None
    left = None
    subs = []
    sub_count = 0
    sub_max = 2 #限制最大sub数量
    idx = None
    def __repr__(self):
        return str(self.idx)
    def __init__(self):
        pass

def toss_coin():
    return random.randint(0,1)
def random_idx(length):
    return random.randint(0,length-1)

def generate_tree(count):
    G=pgv.AGraph(directed=True)
    endnodes = []
    root = node()
    allocate_count = 1
    root.idx=allocate_count
    G.add_node(root)
    endnodes.append(root)
    while allocate_count<count:
        end_node_num = len(endnodes)
        idx=random_idx(end_node_num)
        the_node = endnodes[idx]

        new_node = node()
        allocate_count+=1
        new_node.idx=allocate_count
        G.add_node(new_node)
        G.add_edge(the_node,new_node)    
        the_node.subs.append(new_node)
        if len(the_node.subs)==the_node.sub_max:
            del endnodes[idx]
        endnodes.append(new_node)
    G.layout(prog='dot')
    G.draw("zz.png")
    return G,root
def paint_tree(root):
    pass


  
if __name__ == "__main__":
    count = 10
    G,root = generate_tree(count)
    # nx.draw(G,with_labels=True, font_weight='bold')
    # plt.show()
    # G.layout(prog='dot')
    # G.draw("zz.png")
    pass