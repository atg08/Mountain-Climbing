from mountain import Mountain
from algorithms.binary_search import *

class MountainManager:

    def __init__(self) -> None:
        self.mountain_list : list[Mountain] = []

    def add_mountain(self, mountain: Mountain):
        # Add a mountain to the manager
        mountain_index = binary_search(l = self.mountain_list, item = mountain, key = lambda x : (x.difficulty_level, x.name), is_insert = True)

        self.mountain_list.insert(mountain_index,mountain)

    def remove_mountain(self, mountain: Mountain): 
        # Remove a mountain from the manager 
        
        mountain_index = binary_search(l = self.mountain_list, item = mountain, key = lambda x: (x.difficulty_level, x.name))

        del self.mountain_list[mountain_index]

    def edit_mountain(self, old: Mountain, new: Mountain): 

        self.remove_mountain(mountain = old)
        self.add_mountain(mountain = new)

    def mountains_with_difficulty(self, diff: int):
        # Return a list of all mountains with this difficulty.

        same_diff_mountain : list[Mountain] = []

        for diff_index in range(len(self.mountain_list)):
            if self.mountain_list[diff_index].difficulty_level == diff:
                same_diff_mountain.append(self.mountain_list[diff_index])

        return same_diff_mountain
    
    def group_by_difficulty(self):
        # Returns a list of lists of all mountains, grouped by and sorted by ascending difficulty.
        
        index_diff = 0
        grouped_list_diff : list[list[Mountain]] = []

        while (index_diff < len(self.mountain_list)):
            
            grouped_list : list[Mountain] = self.mountains_with_difficulty(self.mountain_list[index_diff].difficulty_level)
            index_diff += len(grouped_list)
    
            grouped_list_diff.append(grouped_list)
        
        return grouped_list_diff
       