from mountain import Mountain
from algorithms.mergesort import *

class MountainManager:

    def __init__(self) -> None:
        self.manager_list = []      # for add mountain
        self.difficulty_list = []   # for checking difficulty
        self.grouped_list = []      # for return confirm list

    def add_mountain(self, mountain: Mountain):
        # Add a mountain to the manager
        self.manager_list.append(mountain)

    def remove_mountain(self, mountain: Mountain):
        # Remove a mountain from the manager
        for inner_list in self.grouped_list:
            for inner_index in range(len(inner_list)):
                if inner_list[inner_index] == mountain:
                    if len(inner_list) == 1:
                        self.grouped_list.remove(inner_list)
                    else: 
                        self.grouped_list[inner_list].pop(inner_index)

    def edit_mountain(self, old: Mountain, new: Mountain): 
        for inner_list in self.grouped_list:
            for inner_index in range(len(inner_list)):
                if inner_list[inner_index] == old:
                    inner_list[inner_index] == new

    def mountains_with_difficulty(self, diff: int):
        # Return a list of all mountains with this difficulty.
        self.difficulty_list = [index for index in self.manager_list if index.difficulty_level == diff]
        return self.difficulty_list
    
    def group_by_difficulty(self):
        # Returns a list of lists of all mountains, grouped by and sorted by ascending difficulty.
        
        difficulty_counter = []
        
        self.manager_list = mergediff(self.manager_list[:len(self.manager_list) // 2],
                                      self.manager_list[len(self.manager_list) // 2:])
    
        for i in range(len(self.manager_list)):
            if self.manager_list[i].difficulty_level not in difficulty_counter:
                difficulty_counter.append(self.manager_list[i].difficulty_level)

        for j in difficulty_counter: 
            sub_list = []
            for i in range(len(self.manager_list)):
                if self.manager_list[i].difficulty_level == j:
                    sub_list.append(self.manager_list[i])
            self.grouped_list.append(sub_list)

        self.manager_list = []
        return self.grouped_list
       