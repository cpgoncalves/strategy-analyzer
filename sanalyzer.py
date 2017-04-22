#==============================================================================
# Carlos Pedro Goncalves, 2017
# University of Lisbon
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
#
# STRATEGY ANALYZER - PYTHON MODULE FOR A PERCOLATION-BASED INTELLIGENT SYSTEM 
# FOR DECISION SUPPORT AND STRATEGIC PLANNING
#
# sanalyzer.py: main file with functions that implement the analysis
#
# Copyright (c) 2017 Carlos Pedro Gonçalves
#
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. 
# To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-nd/4.0/.
#
#==============================================================================



import sweb

def initAgent():
    return sweb.Agent([])

def createNode(node_name,node_type):
    if node_type not in {'action','event'}:
        print("Error! Node type must be 'action' or 'event'!")
    else:
        Node = sweb.Node(name=node_name,
                         ntype=node_type,
                         state=0,
                         targets=[],
                         origins=[],
                         reverse_percol=[])
        return Node

def connect(Agent,NodeA,NodeB):
    NodeA.targets = NodeA.targets + [NodeB]
    NodeB.origins = NodeB.origins + [NodeA]
    if NodeA not in Agent.nodes:
        Agent.nodes = Agent.nodes + [NodeA]
    if NodeB not in Agent.nodes:
        Agent.nodes = Agent.nodes + [NodeB]


def plan(Agent,objectives):
    Agent.planObjectives(objectives)
    
 