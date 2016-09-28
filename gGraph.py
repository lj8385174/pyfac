# -*- coding:utf-8 -*-

# ggraph class to implement acyclic factor graph with Guassian Message

from gNode import *

class gGraph(object):
    def __init__(self):
        self.vars = []   #store var nodes
        self.varNames = {}   #store var names, key is name and value is index 
        self.facts =[]   #store factor nodes 
        self.factNames = {}
        self.connections = []  # store connections, index is varnode's index, the values is a list of connected factor nodes
        self.factConnections =[] # store connections, index is factnodes's index, the values is a list of connected varnodes
        pass

    def addVarNode(self,gvarnode):
        # Add a var node class
        self.vars.append(gvarnode)
        # TODO: check if the key gvarnode.name already exists
        self.varNames[gvarnode.name]= len(self.vars)-1
        self.connections.append([])
    
    def addFactNode(self,gfactnode):
        # Add a fact node class
        self.facts.append(gfactnode)
        # TODO: check if the key gfactnode.name already exists
        self.factNames[gfactnode.name]= len(self.facts)-1
        self.factConnections.append([])

    def findVarNodebyName(self,name):
        # find the index of the a Var node
        return self.varNames[name]

    def findFactNodebyName(self,name):
        # find the index of the a Fact node
        return self.factNames[name]
    
    def connect(self,varname,factnames):
        # connect a varnames with a series of var factnames
        # factornames should be a List

        varIndex  = self.findVarNodebyName(varname)

        for factname in factnames:
            factIndex = self.findFactNodebyName(factname)
            if factIndex in self.connections[varIndex]:
                raise Exception('the same connection already exists!')
            self.connections[varIndex].append(factIndex)

            if varIndex in self.factConnections[factIndex]:
                raise Exception('the same connection already exists in factConnections!')
            self.factConnections[factIndice].append(varIndex)

    def factConnect(self,factname,varnames):
        # connect a factname with a series of var varnames
        # varnames should be a List
        factIndex  = self.findVarNodebyName(factname)

        for varname in varnames:
            varindex = self.findFactNodebyName(varname)
            if factIndex in self.connections[varindex]:
                raise Exception('the same connection already exists!')
            self.connections[varindex].append(factIndex)

            if varIndex in self.factConnections[factIndex]:
                raise Exception('the same connection already exists in factConnections!')
            self.factConnections[factIndex].append(varIndex)

    def marginalSchedule(self,varname):
        # genrate a schedule 
        # schedule is a list of connection with every step
        # connection is represented by a pair of digits(list)
        varIndex = self.findVarNodebyName(varname)
        rootConnectionsFactIndices = self.connections[varIndex]
        schedule =[]
        for rootConnectionsFactIndex in rootConnectionsFactIndices:
            schedule.append([rootConnectionsFactIndex,varIndex])
        


    def marginal(self,varname):
        # calculate the marginal distribution
        schedule = self.marginalSchedule(varname)
