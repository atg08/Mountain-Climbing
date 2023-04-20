from __future__ import annotations

from mountain import Mountain
from algorithms.mergesort import *

class MountainOrganiser:

    def __init__(self) -> None:
        self.merged_list = []

    def cur_position(self, mountain: Mountain) -> int:
        for item in self.merged_list:
            if item == mountain:
                return self.merged_list.index(item)
            
    def add_mountains(self, mountains: list[Mountain]) -> None:

        if self.merged_list == []:
            self.merged_list = mountains

        else:
            self.merged_list = merge(self.merged_list,mountains)
