from mountain import Mountain
from algorithms.mergesort import *

class MountainManager:

    def __init__(self) -> None:
        self.manager_list = []
        self.difficulty_list = []
        self.grouped_list = []

    def add_mountain(self, mountain: Mountain):
        # Add a mountain to the manager
        self.manager_list.append(mountain)

    def remove_mountain(self, mountain: Mountain):
        # Remove a mountain from the manager
        # for i in self.manager_list:
        #     if i == mountain:
        #         del mountain
        raise NotImplementedError

    def edit_mountain(self, old: Mountain, new: Mountain):
         for i in range(self.manager_list):
            for j in i:
                if self.manager_list[i][j] == old:
                    self.manager_list[i][j] = new

    def mountains_with_difficulty(self, diff: int):
        # Return a list of all mountains with this difficulty.
        self.difficulty_list = []
        for i in range(len(self.manager_list)):
            if self.manager_list[i].difficulty_level == diff:
                self.difficulty_list.append(self.manager_list[i])
        
        return self.difficulty_list

    def group_by_difficulty(self):
        # Returns a list of lists of all mountains, grouped by and sorted by ascending difficulty.
  
        self.manager_list = mergediff(self.manager_list[:len(self.manager_list) // 2],
                                      self.manager_list[len(self.manager_list) // 2:])
        
        '''
            [
            Mountain(name='m1', difficulty_level=2, length=2),
            Mountain(name='m2', difficulty_level=2, length=9),
            Mountain(name='m3', difficulty_level=3, length=6),
            Mountain(name='m4', difficulty_level=3, length=1), 
            Mountain(name='m5', difficulty_level=4, length=6), 
            Mountain(name='m6', difficulty_level=7, length=3), 
            Mountain(name='m7', difficulty_level=7, length=7), 
            Mountain(name='m8', difficulty_level=7, length=8), 
            Mountain(name='m9', difficulty_level=7, length=6)
            ]
        '''
        
        



