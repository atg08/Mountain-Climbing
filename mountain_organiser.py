from __future__ import annotations

from mountain import Mountain
from algorithms.mergesort import *
from algorithms.binary_search import *

class MountainOrganiser:

    def __init__(self) -> None:
        self.merged_list = []

    def cur_position(self, mountain: Mountain) -> int:
        """
        Finds the rank of the provided mountain given all mountains included so far. 

        Args:
        - mountain: Mountain(name: str, difficulty_level: int, length: int)

        Raises:
        - KeyError: if this mountain hasn't been added yet.

        Returns:
        - rank: Difficulty sorted by the total number of mountains and the differential of the mountains

        Complexity: (time complexity will be based on binary search.)
        - Best Case Complexity: O(1), when middle index contains item.
        - Worst Case Complexity: O(log(N)), where N is the total number of mountains included.
        """

        # For finding rank, it used binary_search and based on the key (length and name).
        rank = binary_search(l = self.merged_list,item = mountain, key= lambda a : (a.length, a.name))
        
        return rank
            
    def add_mountains(self, mountains: list[Mountain]) -> None:
        """
        Adds a list of mountains to the organiser.

        Args:
        - mountain: list (Mountain(name: str, difficulty_level: int, length: int))

        Returns:
        - it will add the mountain into self.merged_list using mergesort.

        Complexity: (time complexity will be based on mergesort.)
        - Best/Worst Case:  O(NlogN * comp(T)) N: the length of list, t: length and name.
        """

        # Make the list for temporary, original list + mountains and sort with mergesort.
        self.merged_list = mergesort(l = self.merged_list+ mountains, key= lambda a : (a.length, a.name))