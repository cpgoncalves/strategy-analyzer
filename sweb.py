#==============================================================================
# Carlos Pedro Goncalves, 2017
# University of Lisbon
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
#
# STRATEGY ANALYZER - PYTHON MODULE FOR A PERCOLATION-BASED INTELLIGENT SYSTEM 
# FOR DECISION SUPPORT AND STRATEGIC PLANNING
#
# sweb.py: class file that supports the strategic analysis
#
# Copyright (c) 2017 Carlos Pedro Gonçalves
#
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. 
# To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-nd/4.0/.
#
#==============================================================================


class Node:
    
    def __init__(self,name,ntype,state,targets,origins,reverse_percol):
        self.name = name
        self.ntype = ntype
        self.state = state
        self.targets = targets
        self.origins = origins
        self.reverse_percol = reverse_percol
        
    def checkTargets(self):
        for Target in self.targets:
            if Target.state == 1:
                return 1
        
            
class Agent:
    
    def __init__(self,nodes):
        self.nodes = nodes
        
    def reverseCheck(self):
        num = 0
        for Node in self.nodes:
            if Node.state == 0:
                if Node.checkTargets() == 1:
                    num += 1
        return num

    def resetNodes(self):
        for Node in self.nodes:
            if Node.state == 1:
                Node.state = 0
    
    def reversePercolateNode(self,Node):
        self.resetNodes()
        Node.state = 1
        num = self.reverseCheck()
        while num != 0:
            for OtherNode in self.nodes:
                if OtherNode.state == 0:
                    if OtherNode.checkTargets() == 1:
                        OtherNode.state = 1
                        Node.reverse_percol = Node.reverse_percol + [OtherNode]
            num = self.reverseCheck()
    
    def evaluate(self,value,element,objectives,eval_type,file):
        if eval_type == 'action':
            if element[4] == value:
                file.write("\n\nAction: "+str(element[0].name))
                print("\nAction:",element[0].name)
                file.write("\nBase Score: "+str(element[1]))
                print("Base Score:",element[1])
                file.write("\nTactical Openings Score: "+str(element[2]))
                print("Tactical Openings Score:", element[2])
                file.write("\nEvent Openings Score: "+str(element[3]))
                print("Event Openings Score:", element[3])
                file.write("\n\nLeading to the Strategic Objectives:")
                print("\nLeading to the Strategic Objectives:")
                for Node in element[5]:
                    file.write("\n"+Node.name)
                    print(Node.name)
                if element[2] != 0:
                    file.write("\n\nLeading to the Tactical Openings:")
                    print("\nLeading to the Tactical Openings:")
                    for Node in element[6]:
                        if Node not in objectives:
                            file.write("\n"+Node.name)
                            print(Node.name)
                        else:
                            file.write("\n"+Node.name+" (Objective)")
                            print(Node.name, "(Objective)")
                if element[3] != 0:
                    file.write("\n\nLeading to the Events:")
                    print("\nLeading to the Events:")
                    for Node in element[7]:
                        if Node not in objectives:
                            file.write("\n"+Node.name)
                            print(Node.name)
                        else:
                            file.write("\n"+Node.name+" (Objective)")
                            print(Node.name, "(Objective)")
        else:
            if element[4] == value:
                file.write("\n\nEvent: "+str(element[0].name))
                print("\nEvent:", element[0].name)
                file.write("\nBase Score: "+str(element[1]))
                print("Base Score:",element[1])
                file.write("\nTactical Openings Score: "+str(element[2]))
                print("Tactical Openings Score:", element[2])
                file.write("\nEvent Openings Score: "+str(element[3]))
                print("Event Openings Score:", element[3])
                file.write("\n\nLeading to the Strategic Objectives:")
                print("\nLeading to the Strategic Objectives:")
                for Node in element[5]:
                    file.write("\n"+Node.name)
                    print(Node.name)
                if element[2] != 0:
                    file.write("\n\nLeading to the Tactical Openings:")
                    print("\nLeading to the Tactical Openings:")
                    for Node in element[6]:
                        if Node not in objectives:
                            file.write("\n"+Node.name)
                            print(Node.name)
                        else:
                            file.write("\n"+Node.name+" (Objective)")
                            print(Node.name, "(Objective)")
                if element[3] != 0:
                    file.write("\n\nLeading to the Events:")
                    print("\nLeading to the Events:")
                    for Node in element[7]:
                        if Node not in objectives:
                            file.write("\n"+Node.name)
                            print(Node.name)
                        else:
                            file.write("\n"+Node.name+" (Objective)")
                            print(Node.name, "(Objective)")
        

    def planObjectives(self,objectives):
        actions = []
        events = []
        base_scores = []
        reverse_percolation = []
        actions_scores = []
        events_scores = []
        
        analysis=open("Analysis Report.txt","w")
        for Objective in objectives:
            if len(Objective.origins) == 0:
                analysis.write("\n\nObjective does not have sources in the web!")
                print("\nObjective does not have sources in the web!")
            else:
                self.reversePercolateNode(Objective) 
                reverse_percolation = reverse_percolation + Objective.reverse_percol
        reverse_percolation = list(set(reverse_percolation))
        
        for Node in reverse_percolation:
            self.reversePercolateNode(Node)
            node_base_score = 0
            strategic_targets = []
            for Objective in objectives:
                if len(Objective.origins) != 0:
                    if Node in Objective.reverse_percol:
                        node_base_score += 1
                        strategic_targets.append(Objective)
                        
            base_scores.append(tuple([Node,node_base_score,strategic_targets]))    
        
        for element in base_scores:
            Node = element[0]
            base_score = element[1]
            strategic_targets = element[2]
            tactical_horizon = []
            event_horizon = []
            tactical_score = 0
            event_score = 0
            total_score = 0
            for OtherNode in reverse_percolation:
                if OtherNode != Node:
                    if Node in OtherNode.reverse_percol:
                        if OtherNode.ntype == 'action':
                            tactical_score += 1
                            tactical_horizon.append(OtherNode)
                        else:
                            event_score += 1
                            event_horizon.append(OtherNode)
            total_score = 2 * base_score + tactical_score + event_score
            if Node.ntype == 'action':
                actions.append(tuple([Node,base_score,tactical_score,event_score,total_score,strategic_targets,tactical_horizon,event_horizon]))
                actions_scores.append(total_score)
            else:
                events.append(tuple([Node,base_score,tactical_score,event_score,total_score,strategic_targets,tactical_horizon,event_horizon]))
                events_scores.append(total_score)
        
        actions_scores = sorted(list(set(actions_scores)), key=int, reverse=True)
        events_scores = sorted(list(set(events_scores)), key=int, reverse=True)
        
        len_actions = len(actions_scores)
        len_events = len(events_scores)
        
        analysis.write("\n\n")
        print("\n")
        analysis.write("Actions Analysis:")
        print("\nActions Analysis:")
        
        if len_actions > 1:
            for t in range(0,len_actions):
                for element in actions:
                    self.evaluate(actions_scores[t],element,objectives,eval_type='action',file=analysis)
        else:
            for element in actions:
                self.evaluate(actions_scores[0],element,objectives,eval_type='action',file=analysis)
                
        analysis.write("\n\n")
        print("\n")
        analysis.write("\n\nEvents Analysis:")
        print("\nEvents Analysis:")
        
        if len_events > 1:
            for t in range(0,len_events):
                for element in events:
                    self.evaluate(events_scores[t],element,objectives,eval_type='event',file=analysis)
        else:
            for element in events:
                self.evaluate(events_scores[0],element,objectives,eval_type='event',file=analysis)
