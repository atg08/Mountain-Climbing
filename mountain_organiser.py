from __future__ import annotations

from mountain import Mountain
from algorithms.mergesort import *
from algorithms.binary_search import *

class MountainOrganiser:

    def __init__(self) -> None:
        self.merged_list = []

    def cur_position(self, mountain: Mountain) -> int:
        
        rank = binary_search(l = self.merged_list,item = mountain, key= lambda a : (a.length, a.name))
        
        return rank
            
    def add_mountains(self, mountains: list[Mountain]) -> None:

        self.merged_list = merge(self.merged_list,mountains,key= lambda x:x)
