from __future__ import annotations

from mountain import Mountain
from algorithms.mergesort import *
from algorithms.binary_search import *

class MountainOrganiser:

    def __init__(self) -> None:
        self.merged_list = []

    def cur_position(self, mountain: Mountain) -> int:
        '''
        Finds the rank of the provided mountain given all mountains included so far. 
        See below for an example. 
        
        Raises KeyError if this mountain hasn't been added yet.
        '''
        
        rank = binary_search(l = self.merged_list,item = mountain, key= lambda a : (a.length, a.name))
        
        return rank
            
    def add_mountains(self, mountains: list[Mountain]) -> None:

        '''
        Adds a list of mountains to the organiser
        '''

        self.merged_list = mergesort(l = self.merged_list+ mountains, key= lambda a : (a.length, a.name))