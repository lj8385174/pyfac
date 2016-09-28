# -*- coding:utf-8 -*-
# This is a Guassian node
# So the message type is Guassian type

from  builtins import range
from functools import reduce
import numpy as np

class gNode(object):
    def __init__(self,name):
        self.enabled = True
        self.nbrs = []
        self.incoming = []
        self.outgoing = []
        self.oldoutgoing = []
        self.name = name 
