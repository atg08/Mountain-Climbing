from __future__ import annotations

from mountain import Mountain
from data_structures.hash_table import LinearProbeTable
from algorithms.mergesort import mergesort , merge
from algorithms.binary_search import binary_search

class MountainOrganiser:

    def __init__(self) -> None:
        self.sorted_mountain_list : list[Mountain] = []


    def cur_position(self, mountain: Mountain) -> int:
        rank = binary_search (l = self.sorted_mountain_list, item = mountain, key = lambda a : (a.length , a.name))
        return rank


    def add_mountains(self, mountains: list[Mountain]) -> None:
        temp_sort = mergesort(l = mountains, key = lambda a : (a.length , a.name))
        self.sorted_mountain_list = merge(l1 = temp_sort , l2 = self.sorted_mountain_list , key = lambda a : (a.length , a.name))
 
        
