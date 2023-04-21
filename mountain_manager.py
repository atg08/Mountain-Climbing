from mountain import Mountain
from algorithms import mergesort

class MountainManager:

    def __init__(self) -> None:
        self.manager_list = []
        self.difficulty_list = []

    def add_mountain(self, mountain: Mountain):
        # Add a mountain to the manager
        self.manager_list.append(mountain)
        return self.manager_list

    def remove_mountain(self, mountain: Mountain):
        # Remove a mountain from the manager
        for i in self.manager_list:
            if i == mountain:
                del mountain

    def edit_mountain(self, old: Mountain, new: Mountain):
         for i in range(self.manager_list):
            if self.manager_list[i] == old:
                self.manager_list[i] = new

    def mountains_with_difficulty(self, diff: int):
        # Return a list of all mountains with this difficulty.
        self.difficulty_list = []
        for i in range(len(self.manager_list)):
            if self.manager_list[i].difficulty_level == diff:
                self.difficulty_list.append((self.manager_list[i]))
    
        return self.difficulty_list

    def group_by_difficulty(self):
        # Returns a list of lists of all mountains, grouped by and sorted by ascending difficulty.
        raise NotImplementedError